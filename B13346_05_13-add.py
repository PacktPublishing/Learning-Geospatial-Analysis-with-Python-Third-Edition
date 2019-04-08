"""Add a feature to a shapefile"""

# https://github.com/GeospatialPython/Learn/raw/master/ep202009_5day_026.zip

import shapefile

# Polygon shapefile we are updating.
file_name = "ep202009.026_5day_pgn.shp"
# Create a shapefile reader
r = shapefile.Reader(file_name)
# Copy the shapefile type to a Writer object
w = shapefile.Writer(r.shapeType)
# Copy over the existing dbf fields
w.fields = list(r.fields)
# Copy over the existing dbf records
w.records.extend(r.records())
# Copy over the existing polygons
w._shapes.extend(r.shapes())
# Add a new polygon
w.poly(parts=[[[-104, 24], [-104, 25], [-103, 25], [-103, 24], [-104, 24]]])
# Add a new dbf record
w.record("STANLEY", "TD", "091022/1500", "27", "21", "48", "ep")
# Overwrite the old shapefile or change the name and make a copy
w.save(file_name)
