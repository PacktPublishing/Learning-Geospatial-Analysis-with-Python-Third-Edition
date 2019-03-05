# Open a raster with gdal

# https://github.com/GeospatialPython/Learning/raw/master/SatImage.zip

from osgeo import gdal
raster = gdal.Open("SatImage.tif")
print(raster.RasterCount)
print(raster.RasterXSize)
print(raster.RasterYSize)
