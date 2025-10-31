
# Let's call numpy: a python library for numerical computing:
import numpy as np


# If you are dealing with netCDF, bring Dataset class for working with NetCDF files: (reading, writing array datasets ...)
from netCDF4 import Dataset


# Function to perform averaging and save to netCDF:

def average_and_save_netcdf(file1, file2, output_file):

    # Open the netCDF files for reading:
    
    # file1 is Info from location A
    nc1 = Dataset(file1, 'r')
    # file 2 is Info from location B
    nc2 = Dataset(file2, 'r')
    
    # What do we want? : A simple calc: A + B / 2

    # Now, we know that for example: 'analysis_C_planeXY' is an array in the netCDF file we have'
    # using "variables" we can extract rows and columns and points from the this array. 
    # ncview is a very functional tool to check.    
    
    DataGivenFromLocation_Time_1_nt = nc1.variables['analysis_C_planeXY'][1, 2, :, :]
    DataGivenFromLocation_Time_2_nt = nc2.variables['analysis_C_planeXY'][2, 2, :, :]
    
    DataGivenFromLocation_Time_1_Info = nc1.variables['analysis_Info_planeXY'][1, 2, :, :]
    DataGivenFromLocation_Time_2_Info = nc2.variables['analysis_Info_planeXY'][2, 2, :, :]
    
    DataGivenFromLocation_Time_1_pm = nc1.variables['analysis_AQ_planeXY'][1, 2, :, :]
    DataGivenFromLocation_Time_2_pm = nc2.variables['analysis_AQ_planeXY'][2, 2, :, :]
    
    DataGivenFromLocation_Time_1_ufp = nc1.variables['analysis_AQ2_planeXY'][1, 2, :, :]
    DataGivenFromLocation_Time_2_ufp = nc2.variables['analysis_AQ2_planeXY'][2, 2, :, :]
   
    DataGivenFromLocation_Time_1_u = nc1.variables['u_planeXY'][1, 2, :, :]
    DataGivenFromLocation_Time_2_u = nc2.variables['u_planeXY'][2, 2, :, :]
    
    DataGivenFromLocation_Time_1_v = nc1.variables['v_planeXY'][1, 2, :, :]
    DataGivenFromLocation_Time_2_v = nc2.variables['v_planeXY'][2, 2, :, :]
    
    DataGivenFromLocation_Time_1_w = nc1.variables['w_planeXY'][1, 2, :, :]
    DataGivenFromLocation_Time_2_w = nc2.variables['w_planeXY'][2, 2, :, :] 
    
    
    # Calculate element-wise average:
    
    Full_OUTPUT_C = (DataGivenFromLocation_Time_1_nt + DataGivenFromLocation_Time_2_nt) / 2.0
    Full_OUTPUT_Info = (DataGivenFromLocation_Time_1_Info + DataGivenFromLocation_Time_2_Info) / 2.0
    Full_OUTPUT_pm = (DataGivenFromLocation_Time_1_pm + DataGivenFromLocation_Time_2_pm) / 2.0
    Full_OUTPUT_ufp = (DataGivenFromLocation_Time_1_ufp + DataGivenFromLocation_Time_2_ufp) / 2.0
    Full_OUTPUT_u = (DataGivenFromLocation_Time_1_u + DataGivenFromLocation_Time_2_u) / 2.0
    Full_OUTPUT_v = (DataGivenFromLocation_Time_1_v + DataGivenFromLocation_Time_2_v) / 2.0
    Full_OUTPUT_w = (DataGivenFromLocation_Time_1_w + DataGivenFromLocation_Time_2_w) / 2.0
        
        
    # Now, what should we do?
   
    # Step by Step:
   
    # 1. create dimension:
         # 1.1. we can use the dimension of target array in calculation
         # 1.2. createDimension
         
    # 2. create variable using the createdDimension:
    # 2.2. Now you can equate the output array here.    
        
        
    # Let's go:        
       
    # Get dimensions from DataGivenFromLocation_Time_1:
    
    # dim1 is the size of the rows:
    dim1 = DataGivenFromLocation_Time_1_nt.shape[0]
    
    # dim2 is the size of the columns:
    dim2 = DataGivenFromLocation_Time_1_nt.shape[1]

    # Create a new netCDF file for writing:
    nc_out = Dataset(output_file, 'w', format='NETCDF4')
    
        
    # Define dimensions
    nc_out.createDimension('dim1', dim1)
    nc_out.createDimension('dim2', dim2)

    # Create the variable for average_
    var_out1 = nc_out.createVariable('Full_OUTPUT_C', 'f4', ('dim1', 'dim2'))
    var_out2 = nc_out.createVariable('Full_OUTPUT_Info', 'f4', ('dim1', 'dim2'))
    var_out3 = nc_out.createVariable('Full_OUTPUT_pm', 'f4', ('dim1', 'dim2'))
    var_out4 = nc_out.createVariable('Full_OUTPUT_ufp', 'f4', ('dim1', 'dim2'))
    var_out5 = nc_out.createVariable('Full_OUTPUT_u', 'f4', ('dim1', 'dim2'))
    var_out6 = nc_out.createVariable('Full_OUTPUT_v', 'f4', ('dim1', 'dim2'))
    var_out7 = nc_out.createVariable('Full_OUTPUT_w', 'f4', ('dim1', 'dim2'))

        
    # Write data to the variable
    var_out1[:] = Full_OUTPUT_C
    var_out2[:] = Full_OUTPUT_Info
    var_out3[:] = Full_OUTPUT_pm
    var_out4[:] = Full_OUTPUT_ufp
    var_out5[:] = Full_OUTPUT_u
    var_out6[:] = Full_OUTPUT_v
    var_out7[:] = Full_OUTPUT_w
    
  
    velocity_magnitude_1 = (Full_OUTPUT_u**2+Full_OUTPUT_v**2+Full_OUTPUT_w**2)
    velocity_magnitude = (velocity_magnitude_1)**(0.5)

    var_out8 = nc_out.createVariable('velocity_magnitude', 'f4', ('dim1', 'dim2'))    
    var_out8[:] = velocity_magnitude
    
    # Close the output netCDF file
    nc_out.close()
    
    
    
    
    Sample_1 = nc1.variables['analysis_C_planeXY'][1, 2, 110, 120]
    Sample_2 = nc2.variables['analysis_C_planeXY'][2, 2, 110, 120]
    averageC = (Sample_1 + Sample_2) / 2.0
    My_resultn = Full_OUTPUT_C[110, 120]
    print("averageC = Result of Averaging", averageC)
    print("my_resultC = Output of Result array",My_resultn)
  
    Sample_1 = nc1.variables['analysis_Info_planeXY'][1, 2, 110, 120]
    Sample_2 = nc2.variables['analysis_Info_planeXY'][2, 2, 110, 120]
    averageInfo = (Sample_1 + Sample_2) / 2.0
    My_resultl = Full_OUTPUT_Info[110, 120]
    print("averageInfo = Result of Averaging", averageInfo)
    print("my_resultInfo = Output of Result array",My_resultl)  
  
    Sample_1 = nc1.variables['analysis_AQ_planeXY'][1, 2, 110, 120]
    Sample_2 = nc2.variables['analysis_AQ_planeXY'][2, 2, 110, 120]
    averagepm = (Sample_1 + Sample_2) / 2.0
    My_resultp = Full_OUTPUT_pm[110, 120]
    print("averagepm = Result of Averaging", averagepm)
    print("my_resultpm = Result of Averaging",My_resultp)   
    
    
    
    # Close the input netCDF files
    nc1.close()
    nc2.close()
    
    
# You could run it in the location where file1 and file2 is present:

file1 = 'Input1.nc'
file2 = 'Input2.nc'
output_file = 'Full_OUTPUT.nc'

average_and_save_netcdf(file1, file2, output_file)
