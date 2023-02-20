import pydicom
import os.path as osp
from glob import glob


def is_osirix_sr(ds):
    return hasattr(ds, "EncapsulatedDocument")


def osirix_get_reference_uid(ds):
    return ds.ContentSequence[0].ReferencedSOPSequence[0].ReferencedSOPInstanceUID


def read_dicoms(input, return_path=False):
    assert osp.isdir(input)
    dicoms = sorted(glob(f"{input}/**/*.dcm"))
    results = []
    for d in dicoms:
        ds = pydicom.dcmread(d)
        ds.fullpath = d
        results.append(ds)
    return results


def group_study_into_series(dicoms):
    """
    group dicoms of the same study into different series according to their `SeriesInstanceUID`
    """
    series = dict()
    for ds in dicoms:
        if ds.SeriesInstanceUID not in series:
            series[ds.SeriesInstanceUID] = [ds]
        else:
            series[ds.SeriesInstanceUID].append(ds)
    return series


def build_SOPInstanceUID_lookup_table(dicoms):
    SOPInstanceUID_lookup_table = dict()
    for ds in dicoms:
        SOPInstanceUID_lookup_table[ds.SOPInstanceUID] = ds
    return SOPInstanceUID_lookup_table


def find_osirix_sr(dicoms):
    """
    find OsirixSR files from given list of dicom files
    """
    return [ds for ds in dicoms if is_osirix_sr(ds)]
