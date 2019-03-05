# Create a polygon buffer with shapely
from shapely import wkt, geometry
wktPoly = "POLYGON((0 0, 4 0, 4 4, 0 4, 0 0))"
poly = wkt.loads(wktPoly)
print(poly.area)
buf = poly.buffer(5.0)
print(buf.area)
