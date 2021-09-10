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


# Run this in the ananconda prompt
## Create a new environment
- for pdal 
``` 
$ conda create -n pdalenv
$ activate pdalenv
conda install -c conda-forge pdal
```
- create another also for geopandas 
``` 
$ conda create -n geoenv
$ activate geoenv
$ conda install -c conda-forge geopandas

```

- Cloning the reposity  and install all the requirement
``` 
$ pip install -r requirements.txt 
```


## Scripts and the nootebook
The scripts and the notebook  provided a tools which can help to eaisly handle task such as get the data,data prepocessing, georefence and data visualisation   



# Package_Scripts
The package interacts with USGS 3DEP data. 
- ``Boundaries``: using that, to gollect a boundaries of the data
- ``get_data`` : this one is used plus the hson file to collect the data from the url, paste the script and the jso file on the same folder
- ``reprojection`` : used to rejected the reproject the data on `WGS84`
- ``visualisation`` :  create a great data visualisation
- ``frame_region`` : get the geometry of the farm region  


## Data
The data is read from the USGS 3DEP AWS Public Dataset using the PDAL package.
The data collected will be  with the pipeline will be  a laz file and a tiff fill ,  another way to collect  directly the  data is to use this  url  "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/IA_FullState/ept.json" on the jupyter notebook or whatever the eiteor for python.

## Raster plot 

The image below show the raster of the  data downloard with te pipeline


![](image/pet/Figure_3.png)











