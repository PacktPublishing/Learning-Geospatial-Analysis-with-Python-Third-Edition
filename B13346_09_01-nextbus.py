import urllib.request
import urllib.parse
import urllib.error
from xml.dom import minidom

# Nextbus API command mode
command = "vehicleLocations"

# Nextbus customer to query
agency = "lametro"

# Bus we want to query
route = "2"

# Time in milliseconds since the

# 1970 epoch time.  All tracks
# after this time will be returned.
# 0 only returns data for the last
# 15 minutes
epoch = "0"

# Build our query url
#
# webservices base url
url = "http://webservices.nextbus.com"
# web service path
url += "/service/publicXMLFeed?"
# service command/mode
url += "command=" + command
# agency

url += "&a=" + agency
url += "&r=" + route
url += "&t=" + epoch

# Access the REST URL
feed = urllib.request.urlopen(url)

if feed:
    # Parse the xml feed
    xml = minidom.parse(feed)
    # Get the vehicle tags
    vehicles = xml.getElementsByTagName("vehicle")
    # Get the most recent one. Normally there will
    # be only one.
    if vehicles:
        bus = vehicles.pop()
        # Print the bus latitude and longitude
        att = bus.attributes
        print(att["lon"].value, ",", att["lat"].value)
    else:
        print("No vehicles found.")
