import pydicom
import numpy as np

import matplotlib
import matplotlib.pyplot as plt


rtstruct = pydicom.dcmread('/usr/local/MATLAB/R2022b/toolbox/images/imdata/rtstruct.dcm')
# rtstruct = pydicom.dcmread('example/slice-01.dcm', force=True)

nrois = len(rtstruct.ROIContourSequence)

fig, axes = plt.subplots(1, nrois, figsize=(nrois*4, 4), subplot_kw={'projection': '3d'})

for i, roi in enumerate(rtstruct.ROIContourSequence):
    for idx, c in enumerate(roi.ContourSequence):
        c = np.array(c.ContourData).reshape(-1, 3)
        color = np.array(roi.ROIDisplayColor).astype(np.float64).reshape(1, -1) / 255
        axes[i].scatter(c[:, 0], c[:, 1], c[:, 2], s=0.5, marker='.', c=color)
        axes[i].set_title(f'ROI#{i+1}')

plt.tight_layout()
plt.savefig('ROIs.jpg')

