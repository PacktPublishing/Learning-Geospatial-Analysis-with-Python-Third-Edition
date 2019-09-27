# Parse KML using ElementTree

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
tree = ET.ElementTree(file="time-stamp-point.kml")
ns = "{http://www.opengis.net/kml/2.2}"
placemark = tree.find(".//{}Placemark".format(ns))
coordinates = placemark.find("./{}Point/{}coordinates".format(ns, ns))
print(coordinates.text)
