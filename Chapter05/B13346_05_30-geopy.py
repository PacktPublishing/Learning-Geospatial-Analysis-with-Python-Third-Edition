"""Geocode with geopy"""

# The following code may help with errors on some platforms but it is insecure
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

from geopy.geocoders import Nominatim
g = Nominatim()
location = g.geocode("88360 Diamondhead Dr E, Diamondhead, MS 39525")
print(location.raw)

# {'lon': '-89.3462139', 'osm_type': 'node',
# 'type': 'yes', 'place_id': '25470846',
# 'display_name': 'NVision Solutions Inc.,
# 88360, Diamondhead Drive East, Diamondhead,
# Hancock County, Mississippi, 39520,
# United States of America', 'boundingbox':
# ['30.3961462', '30.3962462', '-89.3462639',
# '-89.3461639'], 'licence': 'Data ©
# OpenStreetMap contributors, ODbL 1.0.
# http://www.openstreetmap.org/copyright', 'osm_id':
# '2470309304', 'importance': 0.421,
# 'class': 'office', 'lat': '30.3961962'}

rev = g.reverse("{},{}".format(location.latitude, location.longitude))
print(rev)

# Location(88360, Diamondhead Drive East, Diamondhead,
# Hancock County, Mississippi, 39525,
# United States of America, (30.39614105,
# -89.3463617900784, 0.0))

print(location.raw)
