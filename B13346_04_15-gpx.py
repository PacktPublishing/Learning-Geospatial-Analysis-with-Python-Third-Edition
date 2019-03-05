# Parse broken GPX data with BeautifulSoup

# https://github.com/GeospatialPython/Learning/raw/master/broken_data.gpx

from bs4 import BeautifulSoup
gpx = open("broken_data.gpx")
soup = BeautifulSoup(gpx.read(), features="xml")
# Check the first track point
print(soup.trkpt)
# Find the rest of the track points and count them
tracks = soup.findAll("trkpt")
print(len(tracks))
# Save the fixed xml file
fixed = open("fixed_data.gpx", "w")
fixed.write(soup.prettify())
fixed.close()
