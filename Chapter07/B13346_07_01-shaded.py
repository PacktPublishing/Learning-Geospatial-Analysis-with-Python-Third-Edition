"""
Creates a shaded relief ASCII grid
from an ASCII DEM.  Also outputs
intermediate grids for slope and
aspect.
"""

# http://git.io/vYwUX

from linecache import getline
import numpy as np

# File name of ASCII digital elevation model
source = "dem.asc"
# File name of the slope grid
slopegrid = "slope.asc"
# File name of the aspect grid
aspectgrid = "aspect.asc"
# Output file name for shaded relief
shadegrid = "relief.asc"

# Shaded elevation parameters
# Sun direction
azimuth = 315.0
# Sun angle
altitude = 45.0
# Elevation exageration
z = 1.0
# Resolution
scale = 1.0
# No data value for output
NODATA = -9999

# Needed for numpy conversions
deg2rad = 3.141592653589793 / 180.0
rad2deg = 180.0 / 3.141592653589793

# Parse the header using a loop and
# the built-in linecache module
hdr = [getline(source, i) for i in range(1, 7)]
values = [float(h.split(" ")[-1].strip()) for h in hdr]
cols, rows, lx, ly, cell, nd = values
xres = cell
yres = cell * -1

# Load the dem into a numpy array
arr = np.loadtxt(source, skiprows=6)

# Exclude 2 pixels around the edges which are usually NODATA.
# Also set up structure for a 3x3 windows to process the slope
# throughout the grid
window = []
for row in range(3):
    for col in range(3):
        window.append(arr[row:(row + arr.shape[0] - 2),
                      col:(col + arr.shape[1] - 2)])

# Process each cell
x = ((z * window[0] + z * window[3] + z * window[3] + z * window[6]) -
     (z * window[2] + z * window[5] + z * window[5] + z * window[8])) / \
    (8.0 * xres * scale)

y = ((z * window[6] + z * window[7] + z * window[7] + z * window[8]) -
     (z * window[0] + z * window[1] + z * window[1] + z * window[2])) / \
     (8.0 * yres * scale)

# Calculate slope
slope = 90.0 - np.arctan(np.sqrt(x * x + y * y)) * rad2deg

# Calculate aspect
aspect = np.arctan2(x, y)

# Calculate the shaded relief
shaded = np.sin(altitude * deg2rad) * np.sin(slope * deg2rad) + \
     np.cos(altitude * deg2rad) * np.cos(slope * deg2rad) * \
     np.cos((azimuth - 90.0) * deg2rad - aspect)
shaded = shaded * 255

# Rebuild the new header
header = "ncols        {}\n".format(shaded.shape[1])
header += "nrows        {}\n".format(shaded.shape[0])
header += "xllcorner    {}\n".format(lx + (cell * (cols - shaded.shape[1])))
header += "yllcorner    {}\n".format(ly + (cell * (rows - shaded.shape[0])))
header += "cellsize     {}\n".format(cell)
header += "NODATA_value      {}\n".format(NODATA)

# Set no-data values
for pane in window:
    slope[pane == nd] = NODATA
    aspect[pane == nd] = NODATA
    shaded[pane == nd] = NODATA

# Open the output file, add the header, save the slope grid
with open(slopegrid, "wb") as f:
    f.write(bytes(header, 'UTF-8'))
    np.savetxt(f, slope, fmt="%4i")

# Open the output file, add the header, save the slope grid
with open(aspectgrid, "wb") as f:
    f.write(bytes(header, 'UTF-8'))
    np.savetxt(f, aspect, fmt="%4i")

# Open the output file, add the header, save the array
with open(shadegrid, "wb") as f:
    f.write(bytes(header, 'UTF-8'))
    np.savetxt(f, shaded, fmt="%4i")
