# Geolocating Photos on the Map

# http://git.io/vczR0

import glob
import os
try:
    import Image
    import ImageDraw
except:
    from PIL import Image
    from PIL.ExifTags import TAGS
import shapefile


def exif(img):
    """Return EXIF metatdata from image"""
    exif_data = {}
    try:    
        i = Image.open(img)
        tags = i._getexif()
        for tag, value in tags.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value
    except:
        pass
    return exif_data


def dms2dd(d, m, s, i):
    """Convert degrees/minutes/seconds to
    decimal degrees"""
    sec = float((m * 60) + s)
    dec = float(sec / 3600)
    deg = float(d + dec)
    if i.upper() == 'W':
        deg = deg * -1
    elif i.upper() == 'S':
        deg = deg * -1
    return float(deg)


def gps(exif):
    """Extract GPS info from EXIF metadat"""
    lat = None
    lon = None
    if exif['GPSInfo']:        
        # Lat
        coords = exif['GPSInfo']
        i = coords[1]
        d = coords[2][0][0]
        m = coords[2][1][0]
        s = coords[2][2][0]
        lat = dms2dd(d, m ,s, i)
        # Lon
        i = coords[3]
        d = coords[4][0][0]
        m = coords[4][1][0]
        s = coords[4][2][0]
        lon = dms2dd(d, m ,s, i)
    return lat, lon

# Hold photo file name and GPS coordinates
photos = {}
photo_dir = "./photos"

# Locate all of the JPG photos
files = glob.glob(os.path.join(photo_dir, "*.jpg"))

# Extract GPS metatdata from files
for f in files:
    e = exif(f)
    lat, lon = gps(e)
    photos[f] = [lon, lat]

# Build a point shapefile with photo
# filename as an attribute
with shapefile.Writer("photos", shapefile.POINT) as w:
    w.field("NAME", "C", 80)
    for f, coords in photos.items():
        w.point(*coords)
        w.record(f)
