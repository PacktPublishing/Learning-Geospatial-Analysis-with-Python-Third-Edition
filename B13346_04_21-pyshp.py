# Examine a shapefile with pyshp

# https://github.com/GeospatialPython/Learning/raw/master/point.zip

import shapefile
shp = shapefile.Reader("point")
for feature in shp.shapeRecords():
    point = feature.shape.points[0]
    rec = feature.record[0]
    print(point[0], point[1], rec)
