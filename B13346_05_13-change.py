"""Convert a shapefile from lat/lon to UTM"""
import shapefile
import utm
r = shapefile.Reader("NYC_MUSEUMS_GEO")
w = shapefile.Writer(r.shapeType)
w.fields = list(r.fields)
w.records.extend(r.records())
for s in r.iterShapes():
    lon, lat = s.points[0]
    y, x, zone, band = utm.from_latlon(lat, lon)
    w.point(x, y)
w.save("NYC_MUSEUMS_UTM")
