# USGS_LIDAR-_AgriTech_

At AgriTech, we are very interested in how water flows through a maize farm field. This knowledge will help us improve our research 
on new agricultural products being tested on farms.How much maize a field produces is very spatially variable?

One important ingredient to understanding water flow in a field is by measuring the elevation of the field at many points. The 
[USGS 3DEP](https://www.usgs.gov/core-science-systems/ngp/3dep) recently released high resolution elevation data as a lidar point cloud called USGS
3DEP in a public dataset on Amazon. This dataset is essential to build models of water flow and predict plant health and maize harvest. 

As part of the data engineering team, you are tasked to produce an easy to use, reliable and well designed python module that domain experts and data scientists 
can use to fetch, visualise, and transform publicly available satellite and LIDAR data. In particular, your code should interface[ with USGS 3DEP](https://www.usgs.gov/core-science-systems/ngp/3dep) and fetch data using their API. 


So then, the first step is to make: 
- Library with can directly interact with the api 
- Data Fetching and Loading 
- Terrain Visualization 
- Data transformation 




### Instalation
- **Install Required Python Modules**
- The pipeline is call iowa.json
``` 
pip install requirements packages
```


## Create a new environment
- for pdal 
``` 
conda install -c conda-forge pdal
```
-create another also for geopandas 
``` 
conda install -c conda-forge geopandas
```

The image below show the raster of the  data downloard with te pipeline

[image](https://github.com/Zchristian955/USGS_LIDAR_AgriTech/blob/20d006a6c6d6b88e38bc5e1d3111cfb932bdf889/image/pet/Figure_3.png)










