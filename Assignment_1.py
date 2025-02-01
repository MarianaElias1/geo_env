# 1. Assignment 1

# 2. Import necessary Python packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr


# 3. Open the netCDF file and 4. insert a breakpoint
dset = xr.open_dataset(r'C:\Users\eliaslm\geo_env\data\N21E039.SRTMGL1_NC.nc')
#pdb.set_trace()

# 6. Explore the variables in the file
dset
# dset.variables

# 7. Load the variable containing elevation data, named SRTMGL1_DEM
DEM = np.array(dset.variables['SRTMGL1_DEM'])

# 8. Close the netCDF file with:
dset.close()

# 9. Add another breakpoint, then determine the data dimensions
DEM.shape

# 10. Visualize the data
plt.imshow(DEM)
cbar = plt.colorbar()
cbar.set_label('Elevation (m asl)')
plt.show()

# 11. Save the figure in PNG format by replacing plt.show(), with:
plt.savefig('Assignment_1.png', dpi=300)