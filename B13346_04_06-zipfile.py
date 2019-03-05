# Unzip a shapefile

# https://github.com/GeospatialPython/Learning/raw/master/hancock.zip

import zipfile
zip = open("hancock.zip", "rb")
zipShape = zipfile.ZipFile(zip)
shpName, shxName, dbfName = zipShape.namelist()
shpFile = open(shpName, "wb")
shxFile = open(shxName, "wb")
dbfFile = open(dbfName, "wb")
shpFile.write(zipShape.read(shpName))
shxFile.write(zipShape.read(shxName))
dbfFile.write(zipShape.read(dbfName))
shpFile.close()
shxFile.close()
dbfFile.close()
