# Assignment 3: Analysis of Hot Spells in Jeddah Using In Situ Weather Data

# Part 1: Downloading and Importing Jeddah Weather Data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
import tools


# Loading the Jeddah weather data into a Pandas dataframe using the read isd csv function from tools.py with the command:
df_isd = tools.read_isd_csv(r'C:\Users\eliaslm\geo_env\data\ISD_Data\41024099999.csv')

# Visualize and get an overview of the ISD data for Jeddah:
plt.figure(figsize=(8,5))
plot = df_isd.plot(title="ISD data for Jeddah")
plt.savefig('ISD_Data_Jeddah.png', dpi=600, bbox_inches='tight')
plt.show()

# Part 2: Heat Index (HI) Calculation

# 1. The Heat Index (HI; ◦C), often referred to as the apparent temperature, is a useful measure
# that combines air temperature and relative humidity to determine how hot it feels to the
# human body. To calculate the HI from our Jeddah data, we need relative humidity (%) data.
# However, the station only provides dewpoint temperature (◦C) data. Dewpoint temperature
# is the temperature to which the air needs to be cooled to, at constant pressure, to
# achieve a relative humidity of 100 %. It is essentialy a different way to express the humidity
# of air. To convert dewpoint temperature (◦C) to relative humidity (%), we can use the
# dewpoint to rh function from tools.py, which requires dewpoint temperature and air
# temperature as input. Add a new column named ‘RH’ to the df isd dataframe as follows:

df_isd['RH'] = tools.dewpoint_to_rh(df_isd['DEW'].values, df_isd['TMP'].values)


# Calculate the HI from air temperature and relative humidity data using the gen heat -
# index function from tools.py. Add a new column named ’HI’ as follows:
df_isd['HI'] = tools.gen_heat_index(df_isd['TMP'].values, df_isd['RH'].values)

# What is the highest HI observed in the year? Execute df isd.max() to obtain the maximum values for all columns, including the HI.
df_isd.max()

# What is the day and time when the highest HI was observed? Use the command df -isd.idxmax() to pinpoint the exact moment of the highest HI.
df_isd.idxmax()


# 5. The ISD is a global dataset and time is expressed in Universal Coordinated Time (UTC).   
# What is the local time of the highest HI?

highest_hi_utc_str = "2024-08-10 11:00:00"
timestamp_utc = pd.Timestamp(highest_hi_utc_str, tz="UTC")
timestamp_local = timestamp_utc.tz_convert("Asia/Riyadh")
print("Highest HI in local time:", timestamp_local)

### Checar ### Should we modify the columns?


# 6. What air temperature and relative humidity were observed at this moment? Use the command
# df isd.loc[["yyyy-mm-dd HH:MM:SS"]]. Replace yyyy-mm-dd HH:MM:SS
# with the highest HI date and time. The loc method is used to select specific rows or
# columns from a dataframe using the names of columns or indices.
df_isd.loc[["2024-08-10 11:00:00"]]

# 7. Based on the National Weather Service’s HI categories (https://www.weather.gov/ama/heatindex), what physical effects on the body might be expected at this HI level?

# 8. Can this event of high temperature and humidity be called a heatwave?

# 9. Is it possible to calculate the HI using daily weather data instead of hourly data? The pandas dataframe method resample could be used for this purpose.
resampled_df = df_isd.resample('D').mean()

# 10. Produce a figure of the HI time series for the year using the plt.savefig function.
plt.figure(figsize=(8,5))
df_isd['HI'].plot()
plt.xlabel('Time (Hourly Data)')
plt.ylabel('Heat Index (HI)')
plt.title('Heat Index (HI) Time series for the Year')  
plt.savefig('HI_time_series.png', dpi=300, bbox_inches='tight')  
plt.show()   

# Part 3: Potential Impact of Climate Change

# 1. What is the projected increase in air temperature for Jeddah, under ‘middle-of-the-road’scenario SSP2-4.5, according to the simulation you have analyzed in assignment 2?
# Load the data from the netcdf file using the xarray open dataset function.

dset_4 = xr.open_dataset(r'c:\Users\eliaslm\geo_env\data\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501-210012.nc')
tas_4 = dset_4.sel(lat=21.5, lon=39.2, method='nearest')
tas_4 = tas_4['tas'] -273.15
tas_4 = tas_4.sel(time=slice('2071-01-01', '2100-12-31'))
tas_4 = tas_4.to_dataframe()
tas_4

df_isd['TMP'].mean()
temp = df_isd['TMP'].mean()
print(temp)

delta = temp - tas_4['tas'].mean()
print(delta)

df_isd['newtemp'] = df_isd['TMP'] + delta  
df_isd

df_isd['newdewp'] = df_isd['DEW'] + delta  
df_isd


# 2. To assess the potential impact of climate change on hot spells in Jeddah, apply this projected warming to the air temperature data and recalculate the HI. What is the increase in the highest HI value when this additional warming is considered?
df_isd['RH'] = tools.dewpoint_to_rh(df_isd['newdewp'].values, df_isd['newtemp'].values)
df_isd['HI'] = tools.gen_heat_index(df_isd['newtemp'].values, df_isd['RH'].values)
df_isd.max()

# HI 2024 = 50.86
# HI 2071 - 2100 mean = 54.885729