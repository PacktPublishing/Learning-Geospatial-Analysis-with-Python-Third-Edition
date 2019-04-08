"""Merge multiple shapefiles using dbfpy"""

# https://github.com/GeospatialPython/Learn/raw/master/footprints.zip

import glob
import shapefile
from dbfpy import dbf
shp_files = glob.glob("footprints_*.shp")
w = shapefile.Writer()
# Loop through ONLY the shp files and copy their shapes
# to a writer object. We avoid opening the dbf files
# to prevent any field-parsing errors.
for f in shp_files:
    print "Shp: %s" % f
    shpf = open(f, "rb")
    r = shapefile.Reader(shp=shpf)
    w._shapes.extend(r.shapes())
    print "Num. shapes: %s" % len(w._shapes)
    shpf.close()
# Save only the shp and shx index file to the new
# merged shapefile.
w.saveShp("merged.shp")
w.saveShx("merged.shx")
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
    print "Dbf: %s" % f
    dba = dbf.Dbf(f)
    for rec in dba:
        db_rec = db.newRecord()
        for k, v in rec.asDict().items():
            db_rec[k] = v
        db_rec.store()
db.close()
