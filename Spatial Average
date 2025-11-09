import numpy as np
from netCDF4 import Dataset

def average_velocity_field(input_file):
    nc_in = Dataset(input_file, 'r')
       velocity_field = nc_in.variables['velocity_magnitude'][:, :]
   
    average_velocity = np.mean(velocity_field)
    print (average_velocity)

    nc_in.close()


# example:
input_file = 'total_ashegh.nc'
average_velocity_field(input_file)
