# Assignment 2: Global Climate Change Assessment

# Part 1: Importing Climate Model Output

# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr

# Open netCDF files:
dset = xr.open_dataset(r'c:\Users\eliaslm\geo_env\data\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc')
#dset = xr.open_dataset('C:\data\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc')

# pdb.set_trace()


# Part 2: Exploring the Data

# Explore netCDF variables
dset.keys()

# Access the air temperature variables using dset ['tas']. What are the dimensions of the air temperature variable?
# Near-Surface Air Temperature

#['tas'].dtype # Obtaining an error for this line
dset['tas']


# 6. Is this the optimal data type for air temperature data?
# This is a raster type of data. Multiple dimensions. Gridded. 


# 7. What is the temporal span of each netCDF file?
dset['time']
# print(dset.time)

start_date = dset.time[0].values
end_date   = dset.time[-1].values
print(start_date, end_date)

# Span: from 1950 to 2014
# Time resolution is monthly.
# The temporal span of each netCDF file is monthly

# 8. What are the units of the air temperature data?
# The units of the air temperature data is Kelvin (K).

# 9. What is the spatial and temporal resolution of the air temperature data?

# For spatial resolution:
print(dset.lat)
print(dset.lon)

dlat = float(dset.lat[1] - dset.lat[0])
dlon = float(dset.lon[1] - dset.lon[0])
print('Spatial resolution: ', dlat, 'degrees latitude by', dlon, 'degrees longitude')

# Spatial resolution:  1.0 degrees latitude by 1.2499999999999998 degrees longitude
# It is not projected.

print('Spatial resolution: ', dlat, 'degrees latitude by', dlon, 'degrees longitude')


# For temporal resolution:
print(dset.time)
#time_values = pd.to_datetime(dset.time.values)
#dt = time_values[1] - time_values[0]
#print("Temporal resolution:", dt)

time_values = dset.time.values  
dt = time_values[1] - time_values[0]
print('Temporal resolution:', dt)

# 10. What is the spatial projection of the air temperature:
# It is not projected.

# 11. What is the meaning of ssp in the file names?
# Shared Socio-economic Pathways- SSP's

# 12. What type of model does the data originate from: data-driven ??


# Part 3: Creation of Climate Change Maps

# Open netCDF files:
dset_1 = xr.open_dataset(r'c:\Users\eliaslm\geo_env\data\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_185001-194912.nc')
dset_2 = xr.open_dataset(r'c:\Users\eliaslm\geo_env\data\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc')
dset_3 = xr.open_dataset(r'c:\Users\eliaslm\geo_env\data\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501-210012.nc')
dset_4 = xr.open_dataset(r'c:\Users\eliaslm\geo_env\data\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501-210012.nc')
dset_5 = xr.open_dataset(r'c:\Users\eliaslm\geo_env\data\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp585_r1i1p1f1_gr1_201501-210012.nc')


# 1. Calculate the mean air temperature map for 1850-1900 (also known as the pre-industrial period) using the command:
mean_1850_1900 = np.mean(dset_1['tas'].sel(time=slice('18500101','19001231')), axis=0)

# Convert the variable to a Numpy array using:
mean_1850_1900 = np.array(mean_1850_1900)

# Explore the properties of the variable you just created by using:
mean_1850_1900.dtype
mean_1850_1900.shape

# print("The properties of the variables are type:", mean_1850_1900.dtype)
# print("The shape of the variables is:", mean_1850_1900.shape)


# 2. Calculate mean air temperature maps for 2071-2100 for each climate scenario

# dset_3 = ssp119
mean_2071_2100_ssp119 = np.mean(dset_3['tas'].sel(time=slice('20710101','21001231')), axis=0)

# Convert the variable to a Numpy array using:
mean_2071_2100_ssp119 = np.array(mean_2071_2100_ssp119)

# dset_4 = ssp245
mean_2071_2100_ssp245 = np.mean(dset_4['tas'].sel(time=slice('20710101','21001231')), axis=0)

# Convert the variable to a Numpy array using:
mean_2071_2100_ssp245 = np.array(mean_2071_2100_ssp245)

# dset_5 = ssp585
mean_2071_2100_ssp585 = np.mean(dset_5['tas'].sel(time=slice('20710101','21001231')), axis=0)

# Convert the variable to a Numpy array using:
mean_2071_2100_ssp585 = np.array(mean_2071_2100_ssp585)

# print("The mean air temperature for ssp119 is:", mean_2071_2100_ssp119)


# 3. Compute and visualize the temperature diferences between 2071-2100 and 1850-1900 for each scenario.

# dset_1 = hist_1850_1949
mean_hist_1850_1949 = np.mean(dset_1['tas'].sel(time=slice('18500101','19001231')), axis=0)

# Convert the variable to a Numpy array using:
mean_hist_1850_1949 = np.array(mean_hist_1850_1949)

# dset_2 = hist_1950_2014
mean_hist_1950_2014 = np.mean(dset_2['tas'].sel(time=slice('19500101','20141231')), axis=0)

# Convert the variable to a Numpy array using:
mean_hist_1950_2014 = np.array(mean_hist_1950_2014)

# mean_1850_1900 = np.mean(dset_1['tas'].sel(time=slice('18500101','19001231')), axis=0)

# Convert the variable to a Numpy array using:
# mean_1850_1900 = np.array(mean_1850_1900)


# Create a figure for visualizing the temperature differences between 1850-1900 (dset_1) with the different scenarios of 2021- 2100 (dset_3, dset_4, dset_5)

# Compute temperature differences for each scenario:
temp_diff_ssp119 = mean_2071_2100_ssp119 - mean_1850_1900 
temp_diff_ssp245 = mean_2071_2100_ssp245 - mean_1850_1900 
temp_diff_ssp585 = mean_2071_2100_ssp585 - mean_1850_1900 


# Scenario SSP119 Temperature Difference
plt.figure(figsize=(8,5))
plt.imshow(temp_diff_ssp119, cmap='coolwarm', origin='lower')
plt.colorbar(label='Temperature Difference (K)')
plt.title('SSP1-1.9: 2071-2100 vs. 1850-1900')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('temp_diff_ssp119.png', dpi=600, bbox_inches='tight')
plt.show()


# Scenario SSP2-4.5 Temperature Difference
plt.figure(figsize=(8,5))
plt.imshow(temp_diff_ssp245, cmap='coolwarm', origin='lower')
plt.colorbar(label='Temperature Difference (K)')
plt.title('SSP2-4.5: 2071-2100 vs. 1850-1900')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('temp_diff_ssp245.png', dpi=600, bbox_inches='tight')
plt.show()


# Scenario SSP5-8.5 Temperature Difference
plt.figure(figsize=(8,5))
plt.imshow(temp_diff_ssp585, cmap='coolwarm', origin='lower')
plt.colorbar(label='Temperature Difference (K)')
plt.title('SSP5-8.5: 2071-2100 vs. 1850-1900')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('temp_diff_ssp585.png', dpi=600, bbox_inches='tight')
plt.show()
