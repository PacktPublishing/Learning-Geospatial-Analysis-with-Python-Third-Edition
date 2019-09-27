"""
Classify an NDVI tiff using 7 classes
by "pushing" the NDVI through
masks defined by the desired
range of values for each class.
"""
import gdal_array as gd
import operator
from functools import reduce


def histogram(a, bins=list(range(256))):
    """
    Histogram function for multi-dimensional array.
    a = array
    bins = range of numbers to match
    """
    fa = a.flat
    n = gd.numpy.searchsorted(gd.numpy.sort(fa), bins)
    n = gd.numpy.concatenate([n, [len(fa)]])
    hist = n[1:]-n[:-1]
    return hist


def stretch(a):
    """
    Performs a histogram stretch on a gdal_array array image.
    """
    hist = histogram(a)
    lut = []
    for b in range(0, len(hist), 256):
        # step size
        step = reduce(operator.add, hist[b:b+256]) / 255
        # create equalization lookup table
        n = 0
        for i in range(256):
            lut.append(n / step)
            n = n + hist[i+b]
    gd.numpy.take(lut, a, out=a)
    return a

# NDVI output from ndvi script
source = "ndvi.tif"
# Target file name for classified
# image image
target = "ndvi_color.tif"

# Load the image into an array
ndvi = gd.LoadFile(source).astype(gd.numpy.uint8)
# Peform a histogram stretch so we are able to
# use all of the classes
ndvi = stretch(ndvi)

# Create a blank 3-band image the same size as the ndvi
rgb = gd.numpy.zeros((3, len(ndvi), len(ndvi[0])), gd.numpy.uint8)

# Class list with ndvi upper range values.
# Note the lower and upper values are listed on the ends
classes = [58, 73, 110, 147, 184, 220, 255]

# Color look-up table (lut)
# The lut must match the number of classes
# Specified as R, G, B tuples from dark brown to dark green
lut = [[120, 69, 25], [255, 178, 74], [255, 237, 166], [173, 232, 94],
       [135, 181, 64], [3, 156, 0], [1, 100, 0]]

# Starting value of the first class
start = 1

# Process all classes.
for i in range(len(classes)):
    mask = gd.numpy.logical_and(start <= ndvi,
                                ndvi <= classes[i])
    for j in range(len(lut[i])):
        rgb[j] = gd.numpy.choose(mask, (rgb[j], lut[i][j]))
    start = classes[i]+1

# Save a geotiff image of the colorized ndvi.
gd.SaveArray(rgb, target, format="GTiff", prototype=source)
