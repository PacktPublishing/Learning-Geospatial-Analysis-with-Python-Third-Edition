"""Merge multiple shapefiles"""

# https://github.com/GeospatialPython/Learn/raw/master/footprints.zip

import glob
import shapefile
files = glob.glob("footprints_*shp")
with shapefile.Writer("Merged") as w:
    r = None
    for f in files:
        r = shapefile.Reader(f)
        if not w.fields:
            w.fields = list(r.fields)
        for rec in r.records():
            w.record(*list(rec))
        for s in r.shapes():
            w._shapeparts(parts=[s.points], shapeType=s.shapeType)
