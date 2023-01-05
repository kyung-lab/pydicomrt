# Coded version of DICOM file '../dce-matlab/torch/data/test-data/10042_1_Lp19Vuc0/20181107/t2_tse_tra_320_p2_8/IM-7914-0001.dcm'
# Produced by pydicom codify utility script
import pydicom
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.sequence import Sequence
def prepare_dataset():
    # File meta info data elements
    file_meta = FileMetaDataset()
    file_meta.FileMetaInformationGroupLength = 196
    file_meta.FileMetaInformationVersion = b'\x00\x01'
    file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.4'
    file_meta.MediaStorageSOPInstanceUID = '1.3.12.2.1107.5.2.19.45214.2017060710260923631337773'
    file_meta.TransferSyntaxUID = '1.2.840.10008.1.2.1'
    file_meta.ImplementationClassUID = '1.2.276.0.7230010.3.0.3.6.0'
    file_meta.ImplementationVersionName = 'OFFIS_DCMTK_360'

    # Main data elements
    ds = Dataset()
    ds.add_new((0x0008, 0x0000), 'UL', 1062)
    ds.SpecificCharacterSet = 'ISO_IR 100'
    ds.ImageType = ['ORIGINAL', 'PRIMARY', 'M', 'NORM', 'DIS2D']
    ds.InstanceCreationDate = '20170607'
    ds.InstanceCreationTime = '102609.421000'
    ds.SOPClassUID = '1.2.840.10008.5.1.4.1.1.4'
    ds.SOPInstanceUID = '1.3.12.2.1107.5.2.19.45214.2017060710260923631337773'
    ds.StudyDate = '20181107'
    ds.SeriesDate = '20181107'
    ds.AcquisitionDate = '20181107'
    ds.ContentDate = '20181107'
    ds.StudyTime = '100219.195000'
    ds.SeriesTime = '102609.241000'
    ds.AcquisitionTime = '102447.872500'
    ds.ContentTime = '102609.421000'
    ds.AccessionNumber = 'A_51892E22'
    ds.Modality = 'MR'
    ds.Manufacturer = 'SIEMENS'
    ds.InstitutionName = 'MP3 MRI'
    ds.InstitutionAddress = 'Medical Plaza B-130 300,Los Angeles,Los Angeles,US,90095'
    ds.ReferringPhysicianName = 'HOLDEN^STUART'
    ds.StationName = 'RADMP3MR03'
    ds.StudyDescription = 'MRI PROSTATE W WO CONTRAST'

    # Procedure Code Sequence
    procedure_code_sequence = Sequence()
    ds.ProcedureCodeSequence = procedure_code_sequence

    # Procedure Code Sequence: Procedure Code 1
    procedure_code1 = Dataset()
    procedure_code1.add_new((0x0008, 0x0000), 'UL', 74)
    procedure_code1.CodeValue = 'IMG5563'
    procedure_code1.CodingSchemeDesignator = 'GEIIS'
    procedure_code1.CodingSchemeVersion = '0'
    procedure_code1.CodeMeaning = 'MRI PROSTATE W WO CONTRAST'
    procedure_code_sequence.append(procedure_code1)

    ds.SeriesDescription = 't2_tse_tra_320_p2'
    ds.InstitutionalDepartmentName = ''
    ds.PerformingPhysicianName = ''
    ds.OperatorsName = ''
    ds.ManufacturerModelName = 'Skyra'

    # Referenced Image Sequence
    refd_image_sequence = Sequence()
    ds.ReferencedImageSequence = refd_image_sequence

    # Referenced Image Sequence: Referenced Image 1
    refd_image1 = Dataset()
    refd_image1.add_new((0x0008, 0x0000), 'UL', 94)
    refd_image1.ReferencedSOPClassUID = '1.2.840.10008.5.1.4.1.1.4'
    refd_image1.ReferencedSOPInstanceUID = '1.3.12.2.1107.5.2.19.45214.2017060710160058519030910'
    refd_image_sequence.append(refd_image1)

    # Referenced Image Sequence: Referenced Image 2
    refd_image2 = Dataset()
    refd_image2.add_new((0x0008, 0x0000), 'UL', 94)
    refd_image2.ReferencedSOPClassUID = '1.2.840.10008.5.1.4.1.1.4'
    refd_image2.ReferencedSOPInstanceUID = '1.3.12.2.1107.5.2.19.45214.2017060710151935256630338'
    refd_image_sequence.append(refd_image2)

    # Referenced Image Sequence: Referenced Image 3
    refd_image3 = Dataset()
    refd_image3.add_new((0x0008, 0x0000), 'UL', 94)
    refd_image3.ReferencedSOPClassUID = '1.2.840.10008.5.1.4.1.1.4'
    refd_image3.ReferencedSOPInstanceUID = '1.3.12.2.1107.5.2.19.45214.2017060710153735477130365'
    refd_image_sequence.append(refd_image3)

    ds.add_new((0x0010, 0x0000), 'UL', 218)
    ds.PatientName = '10042_1_LP19VUC0'
    ds.PatientID = '10042_1_LP19VUC0'
    ds.IssuerOfPatientID = '001R41:20090813:023040546:015090'
    ds.PatientBirthDate = '19000101'
    ds.PatientSex = ''
    ds.PatientBirthName = ''
    ds.PatientAge = ''
    ds.PatientSize = None
    ds.PatientWeight = None
    ds.PatientAddress = ''
    ds.PatientMotherBirthName = ''
    ds.CountryOfResidence = ''
    ds.PatientTelephoneNumbers = ''
    ds.EthnicGroup = ''
    ds.SmokingStatus = 'UNKNOWN'
    ds.PregnancyStatus = 4
    ds.PatientReligiousPreference = ''
    ds.add_new((0x0018, 0x0000), 'UL', 418)
    ds.BodyPartExamined = 'PROSTATE'
    ds.ScanningSequence = 'SE'
    ds.SequenceVariant = ['SK', 'SP', 'OSP']
    ds.ScanOptions = ''
    ds.MRAcquisitionType = '2D'
    ds.SequenceName = '*tse2d1_25'
    ds.AngioFlag = 'N'
    ds.SliceThickness = '3.0'
    ds.RepetitionTime = '3000.0'
    ds.EchoTime = '101.0'
    ds.NumberOfAverages = '2.0'
    ds.ImagingFrequency = '123.167241'
    ds.ImagedNucleus = '1H'
    ds.EchoNumbers = '1'
    ds.MagneticFieldStrength = '3.0'
    ds.SpacingBetweenSlices = '3.6'
    ds.NumberOfPhaseEncodingSteps = '651'
    ds.EchoTrainLength = '25'
    ds.PercentSampling = '97.0'
    ds.PercentPhaseFieldOfView = '100.0'
    ds.PixelBandwidth = '200.0'
    ds.DeviceSerialNumber = '45214'
    ds.SoftwareVersions = 'syngo MR E11'
    ds.ProtocolName = 't2_tse_tra_320_p2'
    ds.TransmitCoilName = 'Body'
    ds.AcquisitionMatrix = [0, 320, 310, 0]
    ds.InPlanePhaseEncodingDirection = 'ROW'
    ds.FlipAngle = '160.0'
    ds.VariableFlipAngleFlag = 'N'
    ds.SAR = '1.3155575586909'
    ds.dBdt = '0.0'
    ds.PatientPosition = 'FFS'
    ds.add_new((0x0020, 0x0000), 'UL', 332)
    ds.StudyInstanceUID = '1.2.840.114350.2.300.2.798268.2.279815471.1'
    ds.SeriesInstanceUID = '1.3.12.2.1107.5.2.19.45214.2017060710231030893037697.0.0.0'
    ds.StudyID = '281595921'
    ds.SeriesNumber = '8'
    ds.AcquisitionNumber = '1'
    ds.InstanceNumber = '1'
    ds.ImagePositionPatient = [-74.939758300781, -70.845703125, 1.3340110778809]
    ds.ImageOrientationPatient = [1, 0, 0, 0, 1, 0]
    ds.FrameOfReferenceUID = '1.3.12.2.1107.5.2.19.45214.2.20170607101340696.0.0.0'
    ds.PositionReferenceIndicator = ''
    ds.SliceLocation = '1.3340110778809'
    ds.add_new((0x0028, 0x0000), 'UL', 168)
    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = 'MONOCHROME2'
    ds.Rows = 320
    ds.Columns = 320
    ds.PixelSpacing = [0.625, 0.625]
    ds.BitsAllocated = 16
    ds.BitsStored = 12
    ds.HighBit = 11
    ds.PixelRepresentation = 0
    ds.SmallestImagePixelValue = 0
    ds.LargestImagePixelValue = 951
    ds.WindowCenter = '585.0'
    ds.WindowWidth = '1172.0'
    ds.WindowCenterWidthExplanation = 'Algo1'
    ds.add_new((0x0032, 0x0000), 'UL', 110)
    ds.RequestingService = 'UROENDO S140'

    # Requested Procedure Code Sequence
    requested_procedure_code_sequence = Sequence()
    ds.RequestedProcedureCodeSequence = requested_procedure_code_sequence

    # Requested Procedure Code Sequence: Requested Procedure Code 1
    requested_procedure_code1 = Dataset()
    requested_procedure_code1.add_new((0x0008, 0x0000), 'UL', 58)
    requested_procedure_code1.CodeValue = '97482'
    requested_procedure_code1.CodingSchemeDesignator = 'L'
    requested_procedure_code1.CodeMeaning = 'MRI PROSTATE W WO CONTRAST'
    requested_procedure_code_sequence.append(requested_procedure_code1)

    ds.add_new((0x0040, 0x0000), 'UL', 112)
    ds.PerformedProcedureStepStartDate = '20170607'
    ds.PerformedProcedureStepStartTime = '100219.315000'
    ds.PerformedProcedureStepID = 'E2931476'
    ds.PerformedProcedureStepDescription = 'MRI PROSTATE W WO CONTRAST'
    ds.CommentsOnThePerformedProcedureStep = ''
    ds.FillerOrderNumberImagingServiceRequest = '43250157'
    # ds.PixelData = # XXX Array of 204800 bytes excluded

    ds.file_meta = file_meta
    ds.is_implicit_VR = False
    ds.is_little_endian = True
    return ds