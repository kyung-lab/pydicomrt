info = dicominfo("example/slice-01.dcm");
% info = dicominfo("rtstruct.dcm");
contour = dicomContours(info);
figure
plotContour(contour)