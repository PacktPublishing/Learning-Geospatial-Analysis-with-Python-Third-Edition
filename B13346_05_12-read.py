"""Open a shapefile for reading"""

# https://github.com/GeospatialPython/Learn/raw/master/MSCities_Geo_Pts.zip

import shapefile

r = shapefile.Reader("MSCities_Geo_Pts")
print(r)
print(r.bbox)
print(r.shapeType)
print(r.numRecords)
print(r.fields)
print([item[0] for item in r.fields[1:]])
print(r.record(2))
print(r.record(2)[4])
fieldNames = [item[0] for item in r.fields[1:]]
name10 = fieldNames.index("NAME10")
print(name10)
print(r.record(2)[name10])
rec = r.record(2)
print(rec)
zipRec = zip(fieldNames, rec)
print(list(zipRec))
for z in zipRec:
    if z[0] == "NAME10":
        print(z[1])
for rec in enumerate(r.records()[:3]):
    print(rec[0] + 1, ": ", rec[1])
counter = 0
for rec in r.iterRecords():
    counter += 1
print(counter)
geom = r.shape(0)
print(geom.points)
