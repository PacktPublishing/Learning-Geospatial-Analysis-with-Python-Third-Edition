# Read tsunami monitoring data via ftp
import ftplib
server = "ftp.ngdc.noaa.gov"
dir = "hazards/DART/20070815_peru"
fileName = "21415_from_20070727_08_55_15_tides.txt"
ftp = ftplib.FTP(server)
ftp.login()
ftp.cwd(dir)
out = open(fileName, "wb")
ftp.retrbinary("RETR " + fileName, out.write)
out.close()
dart = open(fileName)
for line in dart:
    if "LAT, " in line:
        print(line)
        break
