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
    
def dms2dd(lat, lon):
    lat_deg, lat_min, lat_sec, lat_dir = re.split('[^\d\.A-Z]+', lat)
    lon_deg, lon_min, lon_sec, lon_dir = re.split('[^\d\.A-Z]+', lon)
    lat_dd = float(lat_deg) + float(lat_min)/60 + float(lat_sec)/(60*60);
    lon_dd = float(lon_deg) + float(lon_min)/60 + float(lon_sec)/(60*60);
    if lat_dir == 'S':
        lat_dd *= -1
    if lon_dir == 'W':
        lon_dd *= -1
    return (lat_dd, lon_dd);
    