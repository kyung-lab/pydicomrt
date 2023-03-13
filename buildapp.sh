rm -rf dist build
pyinstaller --onefile  -F --hiddenimport=pydicom.encoders.gdcm --hiddenimport=pydicom.encoders.pylibjpeg --hiddenimport=PIL._tkinter_finder rtconvert.py
