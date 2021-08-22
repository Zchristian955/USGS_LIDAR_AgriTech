import py3dep
from pynhd import NLDI
import matplotlib.pyplot as plt




geom = NLDI().get_basins("01031500").geometry[0]
dem = py3dep.get_map("DEM", geom, resolution=30, geo_crs="epsg:4326", crs="epsg:3857")
slope = py3dep.get_map("Slope Degrees", geom, resolution=30)
slope = py3dep.deg2mpm(slope)



fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
dem.plot(ax=ax1)
slope.plot(ax=ax2)
fig.savefig("dem_slope.png", bbox_inches="tight", facecolor="w")

##################################################################################################
