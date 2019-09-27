# Numpy/gdalnumeric - Read an image, extract a band, save a new image

# https://github.com/GeospatialPython/Learning/raw/master/SatImage.zip

from osgeo import gdalnumeric
srcArray = gdalnumeric.LoadFile("SatImage.tif")
band1 = srcArray[0]
gdalnumeric.SaveArray(band1, "band1.jpg", format="JPEG")
