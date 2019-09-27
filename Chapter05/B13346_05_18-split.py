"""Split a shapefile"""

import shapefile
import utm

r = shapefile.Reader("footprints_se")
with shapefile.Writer("footprints_185", r.shapeType) as w:
    w.fields = list(r.fields)
    for sr in r.shapeRecords():
        utmPoints = []
        for p in sr.shape.points:
            x, y, band, zone = utm.from_latlon(p[1], p[0])
            utmPoints.append([x, y])
    area = abs(shapefile.signed_area(utmPoints))
    if area <= 100:
        w.poly([sr.shape.points])
        w.record(*list(sr.record))
# Verify changes
r = shapefile.Reader("footprints_se")
subset = shapefile.Reader("footprints_185")
print(r.numRecords)
print(subset.numRecords)
