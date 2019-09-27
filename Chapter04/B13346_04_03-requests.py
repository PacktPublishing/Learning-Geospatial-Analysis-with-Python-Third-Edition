# Retrieve a file using requests
import requests
url = "https://github.com/GeospatialPython/Learning/raw/master/hancock.zip"
fileName = "hancock.zip"
r = requests.get(url)
with open(fileName, 'wb') as f:
    f.write(r.content)
