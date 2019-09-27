# Add a shapefile to a tar archive

# https://github.com/GeospatialPython/Learning/raw/master/hancock.zip

import tarfile
tar = tarfile.open("hancock.tar.gz", "w:gz")
tar.add("hancock.shp")
tar.add("hancock.shx")
tar.add("hancock.dbf")
tar.close()
