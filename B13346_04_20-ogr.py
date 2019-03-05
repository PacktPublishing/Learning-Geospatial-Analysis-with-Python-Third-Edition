# Examine a shapefile with ogr

# https://github.com/GeospatialPython/Learning/raw/master/point.zip

from osgeo import ogr
shp = ogr.Open("point.shp")
layer = shp.GetLayer()
feature = layer.GetNextFeature()
while feature:
    geometry = feature.GetGeometryRef()
    print(geometry.GetX(), geometry.GetY(), feature.GetField("FIRST_FLD"))
    feature = layer.GetNextFeature()
