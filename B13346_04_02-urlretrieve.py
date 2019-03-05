# Retrieve a file using urllib
import urllib.request
import urllib.parse
import urllib.error
url = "https://github.com/GeospatialPython/Learning/raw/master/hancock.zip"
fileName = "hancock.zip"
urllib.request.urlretrieve(url, fileName)
