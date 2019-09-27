"""Vincenty ellipsoid distance measurement formula"""
from math import atan2, cos, sin, degrees

lon1 = -90.212452861859035
lat1 = 32.316272202663704
lon2 = -88.952170968942525
lat2 = 30.438559624660321

angle = atan2(cos(lat1)*sin(lat2)-sin(lat1) *
              cos(lat2)*cos(lon2-lon1), sin(lon2-lon1)*cos(lat2))

# Avoid negative bearing by adding 360 and then using modulo
bearing = (degrees(angle) + 360) % 360

print(bearing)
