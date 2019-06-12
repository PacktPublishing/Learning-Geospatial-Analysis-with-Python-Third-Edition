import glob
import os
import rasterio
from l8qa.qa import write_cloud_mask

# Directory where our data is
landsat_dir = "l8"

# Get a list of landsat images
images = glob.glob(os.path.join(landsat_dir, 'L*/'))

# Find the quality insurance metadata 
src_qa = glob.glob(os.path.join(landsat_dir, '*QA*'))[0]

# Here we will create the cloudmask
# Read the source QA into an rasterio object.
with rasterio.open(src_qa) as qa_raster:
    profile = qa_raster.profile
    profile.update(nodata=0)

    # Write the cloud mask tif out
    write_cloud_mask(qa_raster.read(1), profile, 'cloudmask.tif')
