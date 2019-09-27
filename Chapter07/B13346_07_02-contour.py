"""
Use GDAL and OGR to create a contour shapefile
"""

# http://git.io/vYwUX

import gdal
import ogr

# Elevation DEM
source = "dem.asc"
# Output shapefile
target = "contour"

ogr_driver = ogr.GetDriverByName('ESRI Shapefile')
ogr_ds = ogr_driver.CreateDataSource(target + ".shp")
ogr_lyr = ogr_ds.CreateLayer(target, geom_type=ogr.wkbLineString25D)
field_defn = ogr.FieldDefn('ID', ogr.OFTInteger)
ogr_lyr.CreateField(field_defn)
field_defn = ogr.FieldDefn('ELEV', ogr.OFTReal)
ogr_lyr.CreateField(field_defn)

# gdal.ContourGenerate() arguments
# Band srcBand,
# double contourInterval,
# double contourBase,
# double[] fixedLevelCount,
# int useNoData,
# double noDataValue,
# Layer dstLayer,
# int idField,
# int elevField

ds = gdal.Open('dem.asc')
gdal.ContourGenerate(ds.GetRasterBand(1), 400, 10, [], 0, 0, ogr_lyr, 0, 1)
