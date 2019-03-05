# Read FTP data via the web
import urllib.request
import urllib.parse
import urllib.error
server = "ftp.ngdc.noaa.gov"
dir = "hazards/DART/20070815_peru"
fileName = "21415_from_20070727_08_55_15_tides.txt"
ftpURL = "ftp://anonymous:anonymous@"
dart = urllib.request.urlopen(ftpURL + server + "/" + dir + "/" + fileName)
for line in dart:
    line = str(line, encoding="utf8")
    if "LAT, " in line:
        print(line)
        break
