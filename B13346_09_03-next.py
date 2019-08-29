import sys
import urllib.request
import urllib.parse
import urllib.error
from xml.dom import minidom
import math
try:
    import Image
except:
    from PIL import Image


def nextbus(a, r, c="vehicleLocations", e=0):
    """Returns the most recent latitude and
    longitude of the selected bus line using
    the NextBus API (nbapi)"""
    nbapi = "http://webservices.nextbus.com"
    nbapi += "/service/publicXMLFeed?"
    nbapi += "command=%s&a=%s&r=%s&t=%s" % (c, a, r, e)
    xml = minidom.parse(urllib.request.urlopen(nbapi))
    # If more than one vehicle, just get the first

    bus = xml.getElementsByTagName("vehicle")[0]
    if bus:
        at = bus.attributes
        return(at["lat"].value, at["lon"].value)
    else:
        return (False, False)


def ll2m(lon, lat):
    """Lat/lon to meters"""
    x = lon * 20037508.34 / 180.0
    y = math.log(math.tan((90.0 + lat) *
                 math.pi / 360.0)) / (math.pi / 180.0)
    y = y * 20037508.34 / 180
    return (x, y)


def wms(minx, miny, maxx, maxy, service, lyr, img, w, h):
    """Retrieve a wms map image from
    the specified service and saves it as a PNG."""
    wms = service
    wms += "?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&"
    wms += "LAYERS=%s" % lyr
    wms += "&STYLES=&"
    wms += "SRS=EPSG:900913&"
    wms += "BBOX=%s,%s,%s,%s&" % (minx, miny, maxx, maxy)
    wms += "WIDTH=%s&" % w
    wms += "HEIGHT=%s&" % h
    wms += "FORMAT=image/png"
    wmsmap = urllib.request.urlopen(wms)
    with open(img + ".png", "wb") as f:
        f.write(wmsmap.read())

# Nextbus agency and route ids
agency = "roosevelt"
route = "shuttle"

# NOAA OpenStreetMap WMS service
basemap = "http://ows.mundialis.de/services/service"

# Name of the WMS street layer
streets = "osm"

# Name of the basemap image to save
mapimg = "basemap"

# OpenWeatherMap.org WMS Service
weather = "http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi"

# If the sky is clear over New York,
# use the following url which contains
# a notional precipitation sample:
# weather = "http://git.io/vl4r1"

# WMS weather layer
weather_layer = "nexrad-n0r"

# Name of the weather image to save
skyimg = "weather"

# Name of the finished map to save
final = "next-weather"

# Transparency level for weather layer
# when we blend it with the base map.
# 0 = invisible, 1 = no transparency
opacity = .5

# Pixel width and height of the

# output map images
w = 600
h = 600

# Pixel width/height of the the

# bus marker icon
icon = 30

# Get the bus location

lat, lon = nextbus(agency, route)
if not lat:
    print("No bus data available.")
    print("Please try again later")
    sys.exit()

# Convert strings to floats
lat = float(lat)
lon = float(lon)

# Convert the degrees to Web Mercator
# to match the NOAA OSM WMS map
x, y = ll2m(lon, lat)

# Create a bounding box 1600 meters
# in each direction around the bus
minx = x - 1600
maxx = x + 1600
miny = y - 1600
maxy = y + 1600

# Download the street map
wms(minx, miny, maxx, maxy, basemap, streets, mapimg, w, h)

# Download the weather map
# wms(minx, miny, maxx, maxy, weather, weather_layer, skyimg, w, h)
wms(minx, miny, maxx, maxy, weather, weather_layer, skyimg, w, h)

# Open the basemap image in PIL
im1 = Image.open("basemap.png")

# Open the weather image in PIL
im2 = Image.open("weather.png")

# Convert the weather image mode
# to "RGB" from an indexed PNG
# so it matches the basemap image
im2 = im2.convert(im1.mode)

# Create a blended image combining
# the base map with the weather map
im3 = Image.blend(im1, im2, opacity)

# Open up the bus icon image to
# use as a location marker.
# http://git.io/vlgHl  
im4 = Image.open("busicon.png")

# Shrink the icon to the desired
# size
im4.thumbnail((icon, icon))

# Use the blended map image
# and icon sizes to place
# the icon in the center of
# the image since the map
# is centered on the bus
# location.
w, h = im3.size
w2, h2 = im4.size

# Paste the icon in the center of the image
center_width = int((w/2)-(w2/2))
center_height = int((h/2)-(h2/2))
im3.paste(im4, (center_width, center_height), im4)

# Save the finished map
im3.save(final + ".png")
