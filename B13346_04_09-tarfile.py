# Extract a shapefile from a gzipped tar archive

# https://github.com/GeospatialPython/Learning/raw/master/hancock.zip

import tarfile
tar = tarfile.open("hancock.tar.gz", "r:gz")
tar.extractall()
tar.close()
