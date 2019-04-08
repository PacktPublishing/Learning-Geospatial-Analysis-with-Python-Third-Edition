"""Parse NMEA GPS strings"""

# https://github.com/GeospatialPython/Learn/raw/master/nmea.txt

from pynmea.streamer import NMEAStream
nmeaFile = open("nmea.txt")
nmea_stream = NMEAStream(stream_obj=nmeaFile)
next_data = nmea_stream.get_objects()
nmea_objects = []
while next_data:
    nmea_objects += next_data
    next_data = nmea_stream.get_objects()
# The NMEA stream is parsed!
# Let's loop through the
# Python object types:
for nmea_ob in nmea_objects:
    if hasattr(nmea_ob, "lat"):
        print("Lat/Lon: ({}, {})".format(nmea_ob.lat, nmea_ob.lon))
