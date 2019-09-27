"""Merge multiple shapefiles using dbfpy"""

# https://github.com/GeospatialPython/Learn/raw/master/footprints.zip

import glob
import shapefile
from dbfpy3 import dbf
shp_files = glob.glob("footprints_*.shp")
w = shapefile.Writer(shp="merged.shp", shx="merged.shx")
# Loop through ONLY the shp files and copy their shapes
# to a writer object. We avoid opening the dbf files
# to prevent any field-parsing errors.
for f in shp_files:
    print("Shp: {}".format(f))
    r = shapefile.Reader(f)
    r = shapefile.Reader(shp=shpf)
    for s in r.shapes():
        w.poly([s.points])
    print("Num. shapes: {}".format(len(w.shapes())))
w.close()
# Now we come back with dbfpy and merge the dbf files
dbf_files = glob.glob("*.dbf")
# Use the first dbf file as a template
template = dbf_files.pop(0)
merged_dbf_name = "merged.dbf"
# Copy the entire template dbf file to the merged file
merged_dbf = open(merged_dbf_name, "wb")
temp = open(template, "rb")
merged_dbf.write(temp.read())
merged_dbf.close()
temp.close()
# Now read each record from teh remaining dbf files
# and use the contents to create a new record in
# the merged dbf file.
db = dbf.Dbf(merged_dbf_name)
for f in dbf_files:
    print("Dbf: {}".format(f))
    dba = dbf.Dbf(f)
    for rec in dba:
        db_rec = db.newRecord()
        for k, v in list(rec.asDict().items()):
            db_rec[k] = v
        db_rec.store()
db.close()
