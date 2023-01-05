import numpy as np
from pydicom.dataset import Dataset
from pydicom.sequence import Sequence
from pydicom.multival import MultiValue


def add_rois(ds, rois):
    ds.ROIContourSequence = Sequence()
    ds.StructureSetROISequence = Sequence()

    for i, roi in enumerate(rois):
        roi_ds = Dataset()
        roi_contours = roi['contours']
        roi_ds.ReferencedROINumber = i + 1
        roi_ds.ROIDisplayColor = np.random.uniform(low=0, high=255, size=(3,)).astype(np.uint8).tolist()
        roi_ds.ContourSequence = Sequence()
        # each ROI comprises several `contours`
        for c in roi_contours:
            # each contour is a N*3 sequence that is the 3D coordinates of N vertices
            assert isinstance(c, np.ndarray) and c.ndim == 2 and c.shape[1] == 3
            contour = Dataset()
            N = 100
            contour.ContourData = MultiValue(float, c.flatten().tolist())
            contour.ContourGeometricType = 'CLOSED_PLANAR'
            roi_ds.ContourSequence.append(contour)

        structure_set_roi_ds = Dataset()
        if 'name' in roi:
            structure_set_roi_ds.ROIName = roi['name']
        else:
            structure_set_roi_ds.ROIName = f'ROI{i}'
        structure_set_roi_ds.ReferencedROINumber = 1
        structure_set_roi_ds.ROINumber = i + 1
        ds.ROIContourSequence.append(roi_ds)
        ds.StructureSetROISequence.append(structure_set_roi_ds)
    return ds