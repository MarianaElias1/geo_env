# Assignment 6: Estimation of Open Water Evaporation in Wadi Murwani Reservoir Using ECMWF ERA5

#Part 2: Data Pre-Processing

# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray
import tools

# Open dataset
dset = xarray.open_dataset(r'C:\Users\eliaslm\Desktop\new\geo_env\ERA5_Data\download.nc')

# Extract the relevant variables from the dataset, including air temperature (t2m), precipitation (tp), latitude, longitude, and time. 
#Then, convert these variables into numpy arrays for further processing:

t2m = np.array(dset.variables['t2m'])
tp = np.array(dset.variables['tp'])
latitude = np.array(dset.variables['latitude'])
longitude = np.array(dset.variables['longitude'])
time_dt = np.array(dset.variables['time'])

# Convert the air temperature from K to ◦C and precipitation from m h−1 to mm h−1 for more intuitive interpretation:
t2m = t2m - 273.15
tp = tp * 1000

# If the ERA5 dataset has four dimensions, indicating the presence of both final and preliminary data, compute the mean across the second dimension to simplify the dataset:
if t2m.ndim == 4:
    t2m = np.nanmean(t2m, axis=1)
    tp = np.nanmean(tp, axis=1)

# Create a Pandas dataframe containing time series data for both air temperature and precipitation.
# Focus on the grid cell closest to the reservoir (row 3, column 2):
df_era5 = pd.DataFrame(index=time_dt)
df_era5['t2m'] = t2m[:,3,2]
df_era5['tp'] = tp[:,3,2]

# Finally, plot the time series:
df_era5.plot()
plt.xlabel('Time')
plt.ylabel('Air Temperature (°C) / Precipitation (mm h−1)')
plt.title('ERA5 Time Series Data')
plt.grid()
plt.legend(['Air Temperature (t2m)', 'Precipitation (tp)'], loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()

# What is the average annual precipitation in mm y−1? 
# Resample the data to annual time step and calculate the mean precipitation as follows:
annual_precip = df_era5['tp'].resample('YE').mean()*24*365.25
mean_annual_precip = np.nanmean(annual_precip)
print('Average annual precipitation: {:.2f} mm y-1'.format(mean_annual_precip))


# Part 3: Calculation of Potential Evaporation (PE)

# Derive all inputs for the function from the hourly ERA5 data:
tmin = df_era5['t2m'].resample('D').min().values
tmax = df_era5['t2m'].resample('D').max().values
tmean = df_era5['t2m'].resample('D').mean().values
lat = 21.25
doy = df_era5['t2m'].resample('D').mean().index.dayofyear

# Compute the PE using:
pe = tools.hargreaves_samani_1982(tmin, tmax, tmean, lat, doy)

# Plot the PE time series:
ts_index = df_era5['t2m'].resample('D').mean().index
plt.figure()
plt.plot(ts_index, pe, label='Potential Evaporation')
plt.title('Potential Evaporation Time Series')
plt.grid()
plt.legend()
plt.xlabel('Time')
plt.ylabel('Potential evaporation (mm d−1)')
plt.show()

# What is the mean annual PE in mm y−1?
annual_pe = np.nanmean(pe)*365.25
print('Average annual potential evaporation: {:.2f} mm y-1'.format(annual_pe))


# Based on the mean annual PE, what is the volume of water potentially lost from the reservoir through evaporation annually? 
 
# Assume the reservoir covers an area of 1.6 km2, as determined from satellite imagery from December 12, 2023
# Note that the PE calculated using the Hargreaves and Samani (1985) method is representative of a grass reference surface. 
# To adjust this PE for open water surfaces like reservoirs, a surface coefficient, often called a crop coefficient in agricultural contexts, should be applied. 
# However, for the purposes of this assignment, we will ignore this to keep things relatively simple.

# Calculate the volume of water lost through evaporation annually:
area = 1.6e6 # m2
volume = annual_pe * area   # m3
print('Volume of water lost through evaporation annually: {:.2f} m3'.format(volume))
