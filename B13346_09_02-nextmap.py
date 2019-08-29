import urllib.request
import urllib.parse
import urllib.error
from xml.dom import minidom
import time


def nextbus(a, r, c="vehicleLocations", e=0):
    """Returns the most recent latitude and
    longitude of the selected bus line using
    the NextBus API (nbapi)
    Arguments: a=agency, r=route, c=command,
    e=epoch timestamp for start date of track,
    0 = the last 15 minutes
    """
    nbapi = "http://webservices.nextbus.com"
    nbapi += "/service/publicXMLFeed?"
    nbapi += "command={}&a={}&r={}&t={}".format(c, a, r, e)
    xml = minidom.parse(urllib.request.urlopen(nbapi))
    # If more than one vehicle, just get the first  
    bus = xml.getElementsByTagName("vehicle")[0]
    if bus:  
        at = bus.attributes
        return(at["lat"].value, at["lon"].value)
    else:
        return (False, False)


def nextmap(a, r, mapimg):
    """Plots a nextbus location on a map image
    and saves it to disk using the OpenStreetMap
    Static Map API (osmapi)"""
    # Fetch the latest bus location
    lat, lon = nextbus(a, r)
    if not lat:
        return False

    osmapi = "https://www.mapquestapi.com/staticmap/v4/getmap?type=map&"
    # Use a red, pushpin marker to pin point the bus
     osmapi += "mcenter={},{}|&".format(lat, lon)
    # Set the zoom level (between 1-18, higher=lower scale)
     osmapi += "zoom=18&"
    # Center the map around the bus location
     osmapi += "center={},{}&".format(lat, lon)
    # Set the map image size
     osmapi += "&size=1500,1000"
    # Add our API key
    osmapi += "&key=YOUR_API_KEY_HERE"
     

    # Request the static map
    img = urllib.request.urlopen(osmapi)
    # Save the map image
    with open("{}.png".format(mapimg), "wb") as f:
        f.write(img.read())
    return True

# Nextbus API agency and bus line variables
agency = "lametro"
route = "2"

# Name of map image to save as PNG
nextimg = "nextmap"

# Number of updates we want to make
requests = 1

# How often we want to update (seconds)
freq = 5

# Map the bus location every few seconds
for i in range(requests):
    success = nextmap(agency, route, nextimg)
    if not success:
        print("No data available.")
        continue
    print("Saved map {} at {}".format(i, time.asctime()))
    time.sleep(freq)
