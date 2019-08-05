"""Shapefile spatial query"""

# https://github.com/GeospatialPython/Learn/raw/master/roads.zip

import shapefile

# Create a reader instance for our US Roads shapefile
r = shapefile.Reader("roadtrl020")
# Create a writer instance copying the reader's shapefile type
w = shapefile.Writer(r.shapeType)
# Copy the database fields to the writer
w.fields = list(r.fields)
# Our selection box that contains Puerto Rico
xmin = -67.5
xmax = -65.0
ymin = 17.8
ymax = 18.6
# Iterate through the shapes and attributes at the same time
for road in r.iterShapeRecords():
    # Shape geometry
    geom = road.shape
    # Database attributes
    rec = road.record
    # Get the bounding box of the shape (a single road)
    sxmin, symin, sxmax, symax = geom.bbox
    # Compare it to our Puerto Rico bounding box.
    # go to the next road as soon as a coordinate is outside the box
    if sxmin < xmin:
        continue
    elif sxmax > xmax:
        continue
    elif symin < ymin:
        continue
    elif symax > ymax:
        continue
    # Road is inside our selection box.
    # Add it to the new shapefile
    w._shapes.append(geom)
    w.records.append(rec)
# Save the new shapefile! (.shp, .shx, .dbf)
w.save("Puerto_Rico_Roads")
