import numpy as np
from pydicom.multival import MultiValue
from prepare_dataset import prepare_dataset

from dicomrt import add_rois

patient_name = 'PatientName'

for s in range(20):
    ds = prepare_dataset()
    ds.PatientName = patient_name
    ds.SliceLocation = s + 1
    ds.InstanceNumber = s + 1
    ds.ImagePositionPatient = MultiValue(float, (-70, -70, s+1))

    # distinguish difference slices
    sop_instance_uid = '1.3.12.2.1107.5.2.19.45214.20170607102609' + '%.11d' % np.random.uniform(1, 10000)
    ds.SOPInstanceUID = sop_instance_uid    

    num_rois = np.random.randint(2, 5)
    rois = []
    for i in range(num_rois):
        num_contours = np.random.randint(2, 10)
        contours = [np.random.uniform(10, 20, size=(np.random.randint(10, 100), 3)) for _ in range(num_contours)]
        rois.append(
            dict(
                name = f'roi-{i+1}',
                contours=contours))
    ds = add_rois(ds, rois)
    ds.WindowCenter = 500
    ds.WindowWidth = 1000
    ds.Rows = 160
    ds.Columns = 160
    ds.PixelData = np.random.uniform(0, 1000, size=(160, 160)).astype(np.uint16).tobytes()
    ds.save_as('example/slice-%.2d.dcm' % (s+1), write_like_original=False)
