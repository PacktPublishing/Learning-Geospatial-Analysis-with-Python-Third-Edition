import math
import re

def dd2dms(lat, lon):
        latf, latn = math.modf(lat)
        lonf, lonn = math.modf(lon)
        latd = int(latn)
        latm = int(latf * 60)
        lats = (lat - latd - latm / 60) * 3600.00
        lond = int(lonn)
        lonm = int(lonf * 60)
        lons = (lon - lond - lonm / 60) * 3600.00
        compass = {
            'lat': ('N','S'),
            'lon': ('E','W')
        }
        lat_compass = compass['lat'][0 if latd >= 0 else 1]
        lon_compass = compass['lon'][0 if lond >= 0 else 1]
        return '{}º {}\' {:.2f}" {}, {}º {}\' {:.2f}" {}'.format(abs(latd), 
        	abs(latm), abs(lats), lat_compass, abs(lond), 
        	abs(lonm), abs(lons), lon_compass)

def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction == 'E' or direction == 'N':
        dd *= -1
    return dd;