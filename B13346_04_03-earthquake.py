# Read data from a url - in this case recent USGS earthquakes
import urllib.request
import urllib.parse
import urllib.error
url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv"
earthquakes = urllib.request.urlopen(url)
# Read the first two earthquakes
print(earthquakes.readline())
# Iterate through the rest
for record in earthquakes:
    print(record)
