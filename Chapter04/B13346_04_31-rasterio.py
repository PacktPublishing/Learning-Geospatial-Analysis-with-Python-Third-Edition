import rasterio
ds = rasterio.open("SatImage.tif")
ds.name
ds.count
ds.width
ds.height