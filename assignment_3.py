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
plot = df_isd.plot(title="ISD data for Jeddah")
plt.show()


