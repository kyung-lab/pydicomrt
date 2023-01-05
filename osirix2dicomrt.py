import pydicom, re
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

d = pydicom.dcmread('data/OsiriX_ROI_SR/IM-0002-0000-0001.dcm')


# print(type(d.EncapsulatedDocument))
# print(d.EncapsulatedDocument)

reg = re.compile('{*.*, *.*}')

osirix_sr = str(d.EncapsulatedDocument)

print(osirix_sr)
print('----')
results = re.findall('{\d+\.\d+, \d+\.\d+}', osirix_sr)

data = []

for r in results:
    d = re.search('\d+\.\d+, \d+\.\d+', r).group().split(', ')
    d = [float(i) for i in d]
    data.append(d)

data = np.stack(data)
plt.scatter(data[:, 0], data[:, 1])
plt.savefig('test.png')

