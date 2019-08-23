"""Threshold an image to black and white"""

# http://git.io/vqarj

from gdal import gdal_array

# Input file name (thermal image)
src = "islands.tif"

# Output file name
tgt = "islands_classified.tiff"

# Load the image into numpy using gdal
srcArr = gdal_array.LoadFile(src)

# Split the histogram into 20 bins as our classes
classes = gdal_array.numpy.histogram(srcArr, bins=2)[1]

lut = [[255, 0, 0], [0, 0, 0], [255, 255, 255]]

# Starting value for classification
start = 1

# Set up the output image
rgb = gdal_array.numpy.zeros((3, srcArr.shape[0], srcArr.shape[1], ),
                              gdal_array.numpy.float32)

# Process all classes and assign colors
for i in range(len(classes)):
    mask = gdal_array.numpy.logical_and(start <= srcArr, srcArr <= classes[i])
    for j in range(len(lut[i])):
        rgb[j] = gdal_array.numpy.choose(mask, (rgb[j], lut[i][j]))
    start = classes[i]+1

# Save the image
gdal_array.SaveArray(rgb.astype(gdal_array.numpy.uint8),
                      tgt, format="GTIFF", prototype=src)
