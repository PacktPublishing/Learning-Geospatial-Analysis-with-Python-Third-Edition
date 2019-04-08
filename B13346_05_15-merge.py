"""Merge multiple shapefiles"""

# https://github.com/GeospatialPython/Learn/raw/master/footprints.zip

import glob
import shapefile
files = glob.glob("footprints_*shp")
w = shapefile.Writer()
r = None
for f in files:
    r = shapefile.Reader(f)
    w._shapes.extend(r.shapes())
    w.records.extend(r.records())
w.fields = list(r.fields)
w.save("Merged")
