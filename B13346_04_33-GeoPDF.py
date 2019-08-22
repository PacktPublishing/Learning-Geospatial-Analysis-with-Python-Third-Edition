from geopdf import GeoCanvas
from reportlab.pdfbase.pdfdoc import PDFString, PDFArray
# Creat a canvas with a name for our pdf.
canvas = GeoCanvas('SimpleGIS.pdf')
# Draw a rectangle to represent the State boundary
canvas.rect(100, 400, 400, 250, stroke=1)
# DATA MODEL
# All layers will have a name, 1+ points, and population count
NAME = 0
POINTS = 1
POP = 2
# Create the state layer
state = ["COLORADO", [[-109, 37], [-109, 41], [-102, 41], [-102, 37]], 5187582]
# Cities layer list
# city = [name, [point], population]
cities = []
# Add Denver
cities.append(["DENVER", [-104.98, 39.74], 634265])
# Add Boulder
cities.append(["BOULDER", [-105.27, 40.02], 98889])
# Add Durango
cities.append(["DURANGO", [-107.88, 37.28], 17069])
# MAP GRAPHICS RENDERING
map_width = 400
map_height = 250
# State Bounding Box
# Use Python min/max function to get state bounding box
minx = 180
maxx = -180
miny = 90
maxy = -90
for x, y in state[POINTS]:
if x < minx:
    minx = x
elif x > maxx:
    maxx = x
if y < miny:
    miny = y
elif y > maxy:
    maxy = y
# Get earth distance on each axis
dist_x = maxx - minx
dist_y = maxy - miny
# Scaling ratio each axis
# to map points from world to screen
x_ratio = map_width / dist_x
y_ratio = map_height / dist_y
def convert(point):
    """Convert lat/lon to screen coordinates"""
    lon = point[0]
    lat = point[1]
    x = map_width - ((maxx - lon) * x_ratio)
    y = map_height - ((maxy - lat) * y_ratio)
    # Python turtle graphics start in the middle of the screen
    # so we must offset the points so they are centered
    x = x + 100
    y = y + 400
    return [x, y]
# Set up our map labels
canvas.setFont("Helvetica", 20)
canvas.drawString(250, 500, "COLORADO")
# Use smaller text for cities
canvas.setFont("Helvetica", 8)
# Draw points and label the cities
for city in cities:
pixel = convert(city[POINTS])
print(pixel)
# Place a point for the city
canvas.circle(pixel[0], pixel[1], 5, stroke=1, fill=1) 
# Label the city
canvas.drawString(pixel[0] + 10, pixel[1], city[NAME] + ", Population: " + str(city[POP]))
# A series of registration point pairs (pixel x, pixel y, x, y)
# to spatially enable the PDF. We only need to do the state boundary.
# The cities will be contained with in it.
registration = PDFArray([
PDFArray(map(PDFString, ['100', '400', '{}'.format(minx), '{}'.format(maxy)])),
PDFArray(map(PDFString, ['500', '400', '{}'.format(maxx), '{}'.format(maxy)])),
PDFArray(map(PDFString, ['100', '150', '{}'.format(minx), '{}'.format(miny)])),
PDFArray(map(PDFString, ['500', '150', '{}'.format(maxx), '{}'.format(miny)]))
])
# Add the map registration
canvas.addGeo(Registration=registration)
# Save our geopdf
canvas.save()