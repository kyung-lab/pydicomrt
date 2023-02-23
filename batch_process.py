import pydicom, re
import os, sys, shutil
from glob import glob
import os.path as osp
import numpy as np
from warnings import warn
from copy import deepcopy

from rt_utils import RTStructBuilder
from rt_utils.utils import Polygon2D
from osirix_parser import OsirixSRParser

from dicom_utils import (read_dicoms,
                         group_study_into_series,
                         find_osirix_sr,
                         osirix_get_reference_uid,
                         build_SOPInstanceUID_lookup_table)


# all_sstudies = glob('/media/hdd1/IDX_MiaoHaoxinReviewed_12152022/IDX_MiaoHaoxinReviewed_12152022/*')
all_sstudies = glob('/media/hdd1/Code/dicomrt/OsiriX_SR_Annotation/examples/DICOM/*')


osirix_parser = OsirixSRParser()

processed = 0
missed_no_associated = 0

for study in all_sstudies:
    dicoms = read_dicoms(study)
    # 
    SOPInstanceUID_lookup_table = build_SOPInstanceUID_lookup_table(dicoms)
    series_instance_uid2series = group_study_into_series(dicoms)
    # find out all Osirix SR files
    osirix_sr = find_osirix_sr(dicoms)

    # check if associated SeriesInstanceUID exists
    associated_exist = True
    for osx in osirix_sr:
        if osirix_get_reference_uid(osx) not in SOPInstanceUID_lookup_table:
            warn(f"{osirix_get_reference_uid(osx)} doest not exist.")
            associated_exist = False
    if not associated_exist:
        missed_no_associated += 1
        continue

    # assign Osirix SR into series
    # since the Osirix SR ROIs might be annotated in difference series
    series_instance_uid2osirixsr = dict()
    for osx in osirix_sr:
        series_instance_uid = SOPInstanceUID_lookup_table[osirix_get_reference_uid(osx)].SeriesInstanceUID
        if series_instance_uid in series_instance_uid2osirixsr:
            series_instance_uid2osirixsr[series_instance_uid].append(osx)
        else:
            series_instance_uid2osirixsr[series_instance_uid] = [osx]

    for series_instance_uid, osirix_sr in series_instance_uid2osirixsr.items():
        series = series_instance_uid2series[series_instance_uid]
        tmp_dir = osp.join(study, 'tmp')
        os.makedirs(tmp_dir, exist_ok=True)
        for ds in series:
            ds = deepcopy(ds)
            fn = osp.basename(ds.fullpath)
            delattr(ds, 'fullpath')
            if not hasattr(ds, 'StudyID'):
                ds.StudyID = osp.split(study)[-1]
            ds.save_as(osp.join(tmp_dir, fn))
        #
        try:
            rtstruct  = RTStructBuilder.create_new(dicom_series_path=tmp_dir)
        except:
            print(f"Cannot create RTStructure for {tmp_dir}")
            continue
        h, w = series[0].pixel_array.shape
        polygons = [[Polygon2D(coords=[], h=h, w=w)],] * len(series)
        for osx in osirix_sr:
            instance_number = int(SOPInstanceUID_lookup_table[osirix_get_reference_uid(osx)].InstanceNumber)
            roi = osirix_parser(osx)
            polygons[instance_number-1] = [Polygon2D(coords=roi.flatten().tolist(), h=h, w=w)]
        rtstruct.add_roi(polygon=polygons)
        save_path = osp.join(study, "RTStructure", f'{series[0].SeriesDescription}_rtstruct.dcm')
        os.makedirs(osp.dirname(save_path), exist_ok=True)
        print(f"Saved structure set to \"{save_path}\"")
        rtstruct.save(save_path)
        shutil.rmtree(tmp_dir)