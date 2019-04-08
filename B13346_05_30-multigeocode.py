"""Multiprocessing geocoding"""

# Import our geocoding module
from geopy.geocoders import Nominatim
# Import the multiprocessing module
import multiprocessing as mp

# Create our geocoder
g = Nominatim()

# Create a function to geocode an individual address
def gcode(address):
	location = g.geocode(address)
	print("Geocoding: {}".format(address))
	return location

# Our list of cities to process
cities = ["New Orleans, LA", "Biloxi, MS", "Memphis, TN", 
			"Atlanta, GA", "Little Rock, AR", "Destin, FL"]

# Create our processor pool counting all of the processors
# on the machine.
pool = mp.Pool(processes=mp.cpu_count())

# Map our cities list to the geocoding function
# and allow the processor pool to split it
# across processors
results = pool.map(gcode, cities)

# Now print the results
print(results)

# [Location(New Orleans, Orleans Parish, Louisiana, USA, (29.9499323, -90.0701156, 0.0)), 
# Location(Biloxi, Harrison County, Mississippi, USA, (30.374673, -88.8459433348286, 0.0)), 
# Location(Memphis, Shelby County, Tennessee, USA, (35.1490215, -90.0516285, 0.0)), 
# Location(Atlanta, Fulton County, Georgia, USA, (33.7490987, -84.3901849, 0.0)), 
# Location(Little Rock, Arkansas, USA, (34.7464809, -92.2895948, 0.0)), 
# Location(Destin, Okaloosa County, Florida, USA, (30.3935337, -86.4957834, 0.0))]

	