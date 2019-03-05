# Parse KML and count placemarks

# http://kml-samples.googlecode.com/svn/trunk/kml/time/time-stamp-point.kml

from xml.dom import minidom
kml = minidom.parse("time-stamp-point.kml")
Placemarks = kml.getElementsByTagName("Placemark")
# Count placemarks
print(len(Placemarks))
# Check the first one
print(Placemarks[0])
print(Placemarks[0].toxml())
# Extract the coordinates
coordinates = Placemarks[0].getElementsByTagName("coordinates")
point = coordinates[0].firstChild.data
print(point)
# Extract x, y, z values as floats
x, y, z = point.split(",")
print(x)
print(y)
print(z)
x = float(x)
y = float(y)
z = float(z)
print(x, y, z)
# Use list comprehensions for efficiency
x, y, z = [float(c) for c in point.split(",")]
print(x, y, z)
