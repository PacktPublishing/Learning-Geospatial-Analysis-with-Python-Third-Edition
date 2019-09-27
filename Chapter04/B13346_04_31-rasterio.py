import rasterio
ds = rasterio.open("SatImage.tif")
print(ds.name)
print(ds.count)
print(ds.width)
print(ds.height)