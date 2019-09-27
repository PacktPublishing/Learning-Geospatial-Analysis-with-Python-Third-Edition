"""Add fields to a shapefile"""

import shapefile

r = shapefile.Reader('NYC_MUSEUMS_UTM')
with shapefile.Writer('NYC_MUSEUMS_UTM', r.shapeType) as w:
    w.fields = list(r.fields)
    w.field('LAT','F',8,5)
    w.field('LON','F',8,5)
    for i in range(len(r.shapes())):
        lon, lat = r.shape(i).points[0]
        w.point(lon, lat)
        w.record(*list(r.record(i)), lat, lon)

