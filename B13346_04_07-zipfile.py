# Unzip a shapefile with a for loop

# https://github.com/GeospatialPython/Learning/raw/master/hancock.zip

import zipfile
zip = open("hancock.zip", "rb")
zipShape = zipfile.ZipFile(zip)
for fileName in zipShape.namelist():
    out = open(fileName, "wb")
    out.write(zipShape.read(fileName))
    out.close()
