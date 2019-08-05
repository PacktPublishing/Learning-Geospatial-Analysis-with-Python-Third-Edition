"""Attribute selection for subset"""

# https://github.com/GeospatialPython/Learn/raw/master/MS_UrbanAnC10.zip

import shapefile

# Create a reader instance
r = shapefile.Reader("MS_UrbanAnC10")
# Create a writer instance
w = shapefile.Writer(r.shapeType)
# Copy the fields to the writer
w.fields = list(r.fields)
# Grab the geometry and records from all features
# with the correct population
selection = []
for rec in enumerate(r.records()):
    if rec[1][15] < 5000:
        selection.append(rec)
# Add the geometry and records to the writer
for rec in selection:
    w._shapes.append(r.shape(rec[0]))
    w.records.append(rec[1])
# Save the new shapefile
w.save("MS_Urban_Subset")
