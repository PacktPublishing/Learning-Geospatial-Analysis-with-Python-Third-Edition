import os
import folium
from folium.plugins import HeatMap

f = open('bear_sightings.csv', 'r')
lines = f.readlines()
lines.pop(0)
data = []
bears = [list(map(float, l.strip().split(','))) for l in lines]

m = folium.Map([32.75, -89.52], tiles='stamentoner', zoom_start=7, max_zoom=7, min_zoom=7)

HeatMap(bears, max_zoom=16, radius=22, min_opacity=1, blur=30).add_to(m)

m.save('heatmap.html')