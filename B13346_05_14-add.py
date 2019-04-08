"""Add a dbf field and column"""
import shapefile
r = shapefile.Reader("NYC_MUSEUMS_UTM")
w = shapefile.Writer(r.shapeType)
w.fields = list(r.fields)
w.records.extend(r.records())
w.field("LAT", "F", 8, 5)
w.field("LON", "F", 8, 5)
geo = shapefile.Reader("NYC_MUSEUMS_GEO")
for i in range(geo.numRecords):
    lon, lat = geo.shape(i).points[0]
    w.records[i].extend([lat, lon])
w._shapes.extend(r.shapes())
w.save("NYC_MUSEUMS_UTM")
