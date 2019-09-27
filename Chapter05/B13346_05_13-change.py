"""Convert a shapefile from lat/lon to UTM"""
import shapefile
import utm
r = shapefile.Reader("NYC_MUSEUMS_GEO")
with shapefile.Writer("NYC_MUSEUMS_UTM", shapeType=1) as w:
    w.fields = list(r.fields)
    for rec in r.records():
        w.record(*list(rec))
    for s in r.iterShapes():
        lon, lat = s.points[0]
        y, x, zone, band = utm.from_latlon(lat, lon)
        w.point(x, y)

# Add a prj file
from urllib.request import urlopen
prj = urlopen('http://spatialreference.org/ref/epsg/26918/esriwkt/')
with open('NYC_MUSEUMS_UTM.prj', 'w') as f:
    f.write(str(prj.read()))
