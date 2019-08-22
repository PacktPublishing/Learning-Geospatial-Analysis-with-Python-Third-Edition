# View data in geopandas

import geopandas
import matplotlib.pyplot as plt

gdf = geopandas.GeoDataFrame

census = gdf.from_file("GIS_CensusTract_poly.shp")

print(census.to_json())

census.plot()

plt.show()