"""Choropleth thematic map"""
import math
import shapefile

try:
    import Image
    import ImageDraw
except:
    from PIL import Image, ImageDraw


def world2screen(bbox, w, h, x, y):
    """convert geospatial coordinates to pixels"""
    minx, miny, maxx, maxy = bbox
    xdist = maxx - minx
    ydist = maxy - miny
    xratio = w/xdist
    yratio = h/ydist
    px = int(w - ((maxx - x) * xratio))
    py = int((maxy - y) * yratio)
    return (px, py)

# Open our shapefile
inShp = shapefile.Reader("GIS_CensusTract_poly")
iwidth = 600
iheight = 400

# PIL Image
img = Image.new("RGB", (iwidth, iheight), (255, 255, 255))

# PIL Draw module for polygon fills
draw = ImageDraw.Draw(img)

# Get the population AND area index
pop_index = None
area_index = None

# Shade the census tracts
for i, f in enumerate(inShp.fields):
    if f[0] == "POPULAT11":
        # Account for deletion flag
        pop_index = i-1
    elif f[0] == "AREASQKM":
        area_index = i-1

# Draw the polygons
for sr in inShp.shapeRecords():
    density = sr.record[pop_index]/sr.record[area_index]
    weight = min(math.sqrt(density/80.0), 1.0) * 50
    R = int(205 - weight)
    G = int(215 - weight)
    B = int(245 - weight)
    pixels = []
    for x, y in sr.shape.points:
        (px, py) = world2screen(inShp.bbox, iwidth, iheight, x, y)
        pixels.append((px, py))
    draw.polygon(pixels, outline=(255, 255, 255), fill=(R, G, B))

img.save("choropleth.png")
