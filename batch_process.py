import pydicom, re
import os, sys, shutil
from glob import glob
import os.path as osp
import numpy as np
from warnings import warn
# import matplotlib
# matplotlib.use('agg')
# import matplotlib.pyplot as plt

from rt_utils import RTStructBuilder
from rt_utils.utils import Polygon2D
from osirix_parser import OsirixSRParser

from dicom_utils import (read_dicoms,
                         group_study_into_series,
                         find_osirix_sr,
                         osirix_get_reference_uid,
                         build_SOPInstanceUID_lookup_table)


all_sstudies = glob('/media/hdd1/IDX_MiaoHaoxinReviewed_12152022/IDX_MiaoHaoxinReviewed_12152022/*')

osirix_parser = OsirixSRParser()

for study in all_sstudies:
    dicoms = read_dicoms(study)
    SOPInstanceUID_lookup_table = build_SOPInstanceUID_lookup_table(dicoms)
    series = group_study_into_series(dicoms)
    # find out all Osirix SR files
    osirix_sr = find_osirix_sr(dicoms)

    # check if associated SeriesInstanceUID exists
    associated_exist = True
    for osx in osirix_sr:
        if osirix_get_reference_uid(osx) not in SOPInstanceUID_lookup_table:
            warn(f"{osirix_get_reference_uid(osx)} doest not exist.")
            associated_exist = False
    if not associated_exist:
        continue

    # check if all the dicoms associated to Osirix_SRs belong to the same series!
    associated_same_series = True
    for i in range(len(osirix_sr)):
        if  SOPInstanceUID_lookup_table[osirix_get_reference_uid(osirix_sr[i])].SeriesInstanceUID != \
                SOPInstanceUID_lookup_table[osirix_get_reference_uid(osirix_sr[0])].SeriesInstanceUID:
            associated_same_series = False
            warn(f"{osirix_sr[0].fullpath} -> {SOPInstanceUID_lookup_table[osirix_get_reference_uid(osirix_sr[0])].fullpath} v.s. {osirix_sr[i].fullpath} -> {SOPInstanceUID_lookup_table[osirix_get_reference_uid(osirix_sr[i])].fullpath}")
    if not associated_same_series:
        continue

    # find all dicoms associated to Osirix_SRs
    associated_dicoms = series[SOPInstanceUID_lookup_table[osirix_get_reference_uid(osirix_sr[0])].SeriesInstanceUID]
    series_description = SOPInstanceUID_lookup_table[osirix_get_reference_uid(osirix_sr[0])].SeriesDescription
    associated_dirname = osp.dirname(associated_dicoms[0].fullpath)

    all_in_folder = True
    # check if all associated dicoms are under the same folder
    for ds in associated_dicoms:
        if associated_dirname != osp.dirname(ds.fullpath):
            all_in_folder = False
    # check if all associated dicoms have 'StudyID'
    has_study_id = all([hasattr(ds, 'StudyID') for ds in associated_dicoms])
    # if not, assign a StudyID to them
    if not has_study_id:
        for ds in dicoms:
            if hasattr(ds, 'StudyID'):
                study_id = ds.StudyID
                break
    for ds in associated_dicoms:
        ds.StudyID = study_id

    # if not in standard format, copy and save to a new folder
    if not (all_in_folder and has_study_id):
        new_associated_dirname =associated_dirname+'_reorganized'
        os.makedirs(new_associated_dirname, exist_ok=True)
        for ds in associated_dicoms:
            fullpath = ds.fullpath
            dirname, basename = osp.split(fullpath)
            new_fullpath = osp.join(new_associated_dirname, basename)
            delattr(ds, 'fullpath')
            ds.save_as(new_fullpath)
            ds.fullpath = new_fullpath
        associated_dirname = new_associated_dirname

    rtstruct  = RTStructBuilder.create_new(dicom_series_path=associated_dirname)
    h, w = associated_dicoms[0].pixel_array.shape
    polygons = [[Polygon2D(coords=[], h=h, w=w)],]*len(associated_dicoms)
    for osx in osirix_sr:
        instance_number = int(SOPInstanceUID_lookup_table[osirix_get_reference_uid(osx)].InstanceNumber)
        roi = osirix_parser(osx)
        polygons[instance_number-1] = [Polygon2D(coords=roi.flatten().tolist(), h=h, w=w)]
    rtstruct.add_roi(polygon=polygons)
    save_path = osp.join(study, series_description+'structure_set', 'rtstruct.dcm')
    os.makedirs(osp.dirname(save_path), exist_ok=True)
    print(f"Saved structure set to \"{save_path}\"")
    rtstruct.save(save_path)

