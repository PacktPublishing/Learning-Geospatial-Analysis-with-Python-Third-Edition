"""Rasterize a shapefile and account for polygon holes"""

import shapefile
import pngcanvas

# Open the extracted islands
r = shapefile.Reader("extract.shp")

# Setup the world to pixels conversion
xdist = r.bbox[2] - r.bbox[0]
ydist = r.bbox[3] - r.bbox[1]
iwidth = 800
iheight = 600
xratio = iwidth/xdist
yratio = iheight/ydist
polygons = []

# Loop through all shapes
for shape in r.shapes():
    # Loop through all parts to catch
    # polygon holes!
    for i in range(len(shape.parts)):
        pixels = []
        pt = None
        if i < len(shape.parts)-1:
            pt = shape.points[shape.parts[i]:shape.parts[i+1]]
        else:
            pt = shape.points[shape.parts[i]:]
        for x, y in pt:
            px = int(iwidth - ((r.bbox[2] - x) * xratio))
            py = int((r.bbox[3] - y) * yratio)
            pixels.append([px, py])
        polygons.append(pixels)

# Set up the output canvas
c = pngcanvas.PNGCanvas(iwidth, iheight)

# Loop through the polygons and draw them
for p in polygons:
    c.polyline(p)

# Save the image
with open("extract.png", "wb") as f:
    f.write(c.dump())
    f.close()
