import folium
import requests
import json

m = folium.Map()
url = "https://api.myjson.com/bins/3ztvz"

folium.GeoJson(json.loads(requests.get(url).text),name='geojson').add_to(m)

m.save("map.html")