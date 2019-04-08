"""Split a shapefile"""

import shapefile
import utm

r = shapefile.Reader("footprints_se")
w = shapefile.Writer(r.shapeType)
w.fields = list(r.fields)
for sr in r.shapeRecords():
    utmPoints = []
    for p in sr.shape.points:
        x, y, band, zone = utm.from_latlon(p[1], p[0])
        utmPoints.append([x, y])
area = abs(shapefile.signed_area(utmPoints))
if area <= 100:
    w._shapes.append(sr.shape)
    w.records.append(sr.record)
w.save("footprints_185")
# Verify changes
r = shapefile.Reader("footprints_se")
subset = shapefile.Reader("footprints_185")
print(r.numRecords)
print(subset.numRecords)
