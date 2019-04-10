"""Graph a histogram of a remotely sensed image"""

# http://git.io/vqs41
# uses output from swap-bands.py script

from osgeo import gdal_array
import turtle as t


def histogram(a, bins=list(range(0, 256))):
    """
    Histogram function for multi-dimensional array.
    a = array
    bins = range of numbers to match
    """
    fa = a.flat
    n = gdal_array.numpy.searchsorted(gdal_array.numpy.sort(fa), bins)
    n = gdal_array.numpy.concatenate([n, [len(fa)]])
    hist = n[1:]-n[:-1]
    return hist


def draw_histogram(hist, scale=True):
    t.color("black")
    # Draw the axes
    axes = ((-355, -200), (355, -200), (-355, -200), (-355, 250))
    t.up()
    for p in axes:
        t.goto(p)
        t.down()
    # Labels
    t.up()
    t.goto(0, -250)
    t.write("VALUE", font=("Arial, ", 12, "bold"))
    t.up()
    t.goto(-400, 280)
    t.write("FREQUENCY", font=("Arial, ", 12, "bold"))
    # Tick marks
    # x axis
    x = -355
    y = -200
    t.up()
    for i in range(1, 11):
        x = x+65
        t.goto(x, y)
        t.down()
        t.goto(x, y-10)
        t.up()
        t.goto(x, y-25)
        t.write("{}".format((i*25)), align="center")
    # y axis
    x = -355
    y = -200
    t.up()
    pixels = sum(hist[0])
    if scale:
        max = 0
        for h in hist:
            hmax = h.max()
            if hmax > max:
                max = hmax
        pixels = max
    label = int(pixels/10)
    for i in range(1, 11):
        y = y+45
        t.goto(x, y)
        t.down()
        t.goto(x-10, y)
        t.up()
        t.goto(x-15, y-6)
        t.write("{}" .format((i*label)), align="right")
    # Plot each histogram as a colored line
    x_ratio = 709.0 / 256
    y_ratio = 450.0 / pixels
    # Add more colors to this list if comparing
    # more than 3 bands or 1 image
    colors = ["red", "green", "blue"]
    for j in range(len(hist)):
        h = hist[j]
        x = -354
        y = -199
        t.up()
        t.goto(x, y)
        t.down()
        t.color(colors[j])
        for i in range(256):
            x = i * x_ratio
            y = h[i] * y_ratio
            x = x - (709/2)
            y = y + -199
            t.goto((x, y))
im = "swap.tif"
histograms = []
arr = gdal_array.LoadFile(im)
for b in arr:
    histograms.append(histogram(b))
draw_histogram(histograms)
# Hide our pen
t.pen(shown=False)
t.done()
