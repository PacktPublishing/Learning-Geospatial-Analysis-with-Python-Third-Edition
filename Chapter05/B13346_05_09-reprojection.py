"""Reproject a shapefile"""

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_LAMBERT.zip

import ogr
import osr
import os
import shutil

# Source and target file names
srcName = "NYC_MUSEUMS_LAMBERT.shp"
tgtName = "NYC_MUSEUMS_GEO.shp"

# Target spatial reference
tgt_spatRef = osr.SpatialReference()
tgt_spatRef.ImportFromEPSG(4326)
# Account for the flipped axis change in the latest GDAL
tgt_spatRef.SetAxisMappingStrategy(0)

# Source shapefile
driver = ogr.GetDriverByName("ESRI Shapefile")
src = driver.Open(srcName, 0)
srcLyr = src.GetLayer()

# Source spatial reference
src_spatRef = srcLyr.GetSpatialRef()

# Target shapefile -
# delete if it's already
# there.
if os.path.exists(tgtName):
    driver.DeleteDataSource(tgtName)
tgt = driver.CreateDataSource(tgtName)
lyrName = os.path.splitext(tgtName)[0]
tgtLyr = tgt.CreateLayer(lyrName, geom_type=ogr.wkbPoint)

# Layer definition
featDef = srcLyr.GetLayerDefn()

# Spatial Transform
trans = osr.CoordinateTransformation(src_spatRef, tgt_spatRef)

# Reproject and copy features
srcFeat = srcLyr.GetNextFeature()
while srcFeat:
    geom = srcFeat.GetGeometryRef()
    geom.Transform(trans)
    feature = ogr.Feature(featDef)
    feature.SetGeometry(geom)
    tgtLyr.CreateFeature(feature)
    feature.Destroy()
    srcFeat.Destroy()
    srcFeat = srcLyr.GetNextFeature()
src.Destroy()
tgt.Destroy()

# Create the prj file
tgt_spatRef.MorphToESRI()
prj = open(lyrName + ".prj", "w")
prj.write(tgt_spatRef.ExportToWkt())
prj.close()

# Just copy dbf contents over rather
# than rebuild the dbf using the
# ogr API since we're not changing
# anything.
srcDbf = os.path.splitext(srcName)[0] + ".dbf"
tgtDbf = lyrName + ".dbf"
shutil.copyfile(srcDbf, tgtDbf)
