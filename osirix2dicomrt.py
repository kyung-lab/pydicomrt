import pydicom, re
import os, sys, shutil
from glob import glob
import os.path as osp
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from vlkit.medical import read_dicom_data, read_dicoms

from rt_utils import RTStructBuilder
from rt_utils.utils import Polygon2D


def parse_osirixsr_roi(bytes):
    results = re.findall('{\d+\.\d+, \d+\.\d+}', str(bytes))
    data = []
    data = []
    for r in results:
        d = re.search('\d+\.\d+, \d+\.\d+', r).group().split(', ')
        d = [float(i) for i in d]
        data.append(d)
    return np.array(data)


series_name = 't2_tse_tra_320'
study_dir = 'data/study'


series = read_dicoms(osp.join(study_dir, series_name))
osirix_sr = read_dicoms(osp.join(study_dir, 'OsiriX_ROI_SR'))

h, w = series[0].pixel_array.shape

sop2index = dict()
for idx, s in enumerate(series):
    sop2index[s.SOPInstanceUID] = idx


polygons = [[Polygon2D(coords=[], h=h, w=w)],]*len(series)

rtstruct  = RTStructBuilder.create_new(dicom_series_path=osp.join(study_dir, series_name))

for sr in osirix_sr:
    ref_sop = sr.ContentSequence[0].ReferencedSOPSequence[0].ReferencedSOPInstanceUID
    ref_index = sop2index[ref_sop]
    # print(ref_index)
    roi = parse_osirixsr_roi(sr.EncapsulatedDocument)
    print(roi.shape)
    polygons[ref_index] = [Polygon2D(coords=roi.flatten().tolist(), h=h, w=w)]

rtstruct.add_roi(polygon=polygons)

rtstruct.save('data/study/t2_tse_tra_320/new_rt_struct.dcm')