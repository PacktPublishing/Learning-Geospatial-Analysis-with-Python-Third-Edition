# Examine Data with Fiona

# https://github.com/GeospatialPython/Learning/raw/master/GIS_CensusTract.zip

import fiona
import pprint

# Open a shapefile
f = fiona.open("GIS_CensusTract_poly.shp")
# Check the type of driver
print(f.driver)
# Get the crs
print(f.crs)
# Get the boudning box
print(f.bounds)
# Look at the database schema
pprint.pprint(f.schema)
# Count the number of eatures
print(len(list(f)))
# Print the geometry and fields as geojson
pprint.pprint(f[1])


 