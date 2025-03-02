# Assignment 5: Analysis of the 2009 Jeddah Rainfall Event Using Geostationary Satellite Data
# Data Visualization and Inspection

# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr

# Open one of the netCDF file:
dset_1 = xr.open_dataset(r'C:\Users\eliaslm\geo_env\data\GridSat_Data\GRIDSAT-B1.2009.11.25.00.v02r01.nc')
dset_3 = xr.open_dataset(r'C:\Users\eliaslm\geo_env\data\GridSat_Data\GRIDSAT-B1.2009.11.25.03.v02r01.nc')
dset_6 = xr.open_dataset(r'C:\Users\eliaslm\geo_env\data\GridSat_Data\GRIDSAT-B1.2009.11.25.06.v02r01.nc')
dset_9 = xr.open_dataset(r'C:\Users\eliaslm\geo_env\data\GridSat_Data\GRIDSAT-B1.2009.11.25.09.v02r01.nc')
dset_12 = xr.open_dataset(r'C:\Users\eliaslm\geo_env\data\GridSat_Data\GRIDSAT-B1.2009.11.25.12.v02r01.nc')

# Load irwin_cdr from the netCDF files with:
IR = np.array(dset_6.variables['irwin_cdr']).squeeze()

# Check the dimensions of the resulting array:
IR.shape

# The geospatial raster data for this dataset is ordered from south to north. To correct the orientation, flip the data vertically using:
IR = np.flipud(IR)

# Apply a scale of 0.01 and an offset of 200 to the raw satellite data to obtain brightness temperatures in kelvin:
IR = IR*0.01+200

# Convert the temperatures from kelvin (K) to degrees Celsius (◦C) for easier interpretation:
IR = IR-273.15

# Plot the data with a colorbar:
plt.figure(figsize=(15,10))
#plt.figure(1)
plt.imshow(IR, extent=[-180.035, 180.035, -70.035, 70.035], aspect='auto')
jeddah_lat = 21.5
jeddah_lon = 39.2
plt.scatter(jeddah_lon, jeddah_lat, color='red', marker='o', label='Jeddah')
cbar = plt.colorbar()
cbar.set_label('Brightness temperature (degrees Celsius)')
