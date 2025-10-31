import numpy as np
from netCDF4 import Dataset

# Function to perform averaging and save to netCDF:

def average_and_save_netcdf(file1, file2, output_file):
    # Open the netCDF files for reading
    
    nc1 = Dataset(file1, 'r')
    nc2 = Dataset(file2, 'r')

#####################################################################

    # To know the shape:
    CALC_nt = nc1.variables['Information_AQ1_yz'][:, :, :, :]
    dim3 = CALC_nt.shape
    print('dimension', dim3)
    #So: [frame, Z, y, x] in yz section
    
#####################################################################
    
    CALC_time1_nt = nc1.variables['Information_AQ1_yz'][1, :, :, 2]
    CALC_time2_nt = nc2.variables['Information_AQ1_yz'][2, :, :, 2]
 
    CALC_time1_w = nc1.variables['w_yz'][1, :, :, 2]
    CALC_time2_w = nc2.variables['w_yz'][2, :, :, 2] 
    
    CALC_time1_v = nc1.variables['v_yz'][1, :, :, 2]
    CALC_time2_v = nc2.variables['v_yz'][2, :, :, 2] 
    
    CALC_time1_u = nc1.variables['u_yz'][1, :, :, 2]
    CALC_time2_u = nc2.variables['u_yz'][2, :, :, 2] 
    
    CALC_time1_AQ2 = nc1.variables['Information_AQ2_yz'][1, :, :, 2]
    CALC_time2_AQ2 = nc2.variables['Information_AQ2_yz'][2, :, :, 2] 
    
    CALC_time1_AQ3 = nc1.variables['AQ3_yz'][1, :, :, 2]
    CALC_time2_AQ3 = nc2.variables['AQ3_yz'][2, :, :, 2] 
    
    CALC_time1_AQ4 = nc1.variables['Information_AQ42.5_yz'][1, :, :, 2]
    CALC_time2_AQ4 = nc2.variables['Information_AQ42.5_yz'][2, :, :, 2] 
    
    CALC_time1_AQ5 = nc1.variables['Information_N_AQ5_yz'][1, :, :, 2]
    CALC_time2_AQ5 = nc2.variables['Information_N_AQ5_yz'][2, :, :, 2]
    
    
    # Calculate element-wise average
    total_Alanysis_AQ1 = (CALC_time1_nt + CALC_time2_nt) / 2.0
    total_Alanysis_w = (CALC_time1_w + CALC_time2_w) / 2.0
    total_Alanysis_v = (CALC_time1_v + CALC_time2_v) / 2.0
    total_Alanysis_u = (CALC_time1_u + CALC_time2_u) / 2.0
    total_Alanysis_AQ2 = (CALC_time1_AQ2 + CALC_time2_AQ2) / 2.0
    total_Alanysis_AQ3 = (CALC_time1_AQ3 + CALC_time2_AQ3)/2.0
    total_Alanysis_AQ4 = (CALC_time1_AQ4 + CALC_time2_AQ4) / 2.0
    total_Alanysis_AQ5 = (CALC_time1_AQ5 + CALC_time2_AQ5) / 2.0
 
    # Get dimensions from CALC_time1 (assuming they are the same for both arrays)
    dim1 = CALC_time1_nt.shape[0]
    dim2 = CALC_time1_nt.shape[1]

    # Create a new netCDF file for writing
    nc_out = Dataset(output_file, 'w', format='NETCDF4')
    
      
    # Define dimensions
    nc_out.createDimension('dim1', dim1)
    nc_out.createDimension('dim2', dim2)

    # Create the variable for average_ASMAR
    var_out1 = nc_out.createVariable('total_Alanysis_AQ1', 'f4', ('dim1', 'dim2'))
    var_out2 = nc_out.createVariable('total_Alanysis_w', 'f4', ('dim1', 'dim2'))

    var_out3 = nc_out.createVariable('total_Alanysis_v', 'f4', ('dim1', 'dim2'))
    var_out4 = nc_out.createVariable('total_Alanysis_u', 'f4', ('dim1', 'dim2'))

    var_out5 = nc_out.createVariable('total_Alanysis_AQ2', 'f4', ('dim1', 'dim2'))
    var_out6 = nc_out.createVariable('total_Alanysis_AQ3', 'f4', ('dim1', 'dim2'))

    var_out7 = nc_out.createVariable('total_Alanysis_AQ4', 'f4', ('dim1', 'dim2'))
    var_out8 = nc_out.createVariable('total_Alanysis_AQ5', 'f4', ('dim1', 'dim2'))



    # Write data to the variable
    var_out1[:] = total_Alanysis_AQ1
    var_out2[:] = total_Alanysis_w
    var_out3[:] = total_Alanysis_v
    var_out4[:] = total_Alanysis_u
    var_out5[:] = total_Alanysis_AQ2
    var_out6[:] = total_Alanysis_AQ3
    var_out7[:] = total_Alanysis_AQ4
    var_out8[:] = total_Alanysis_AQ5



    # Close the output netCDF file
    
    nc_out.close()
    
    Sample_1 = nc1.variables['Information_AQ1_yz'][1, 7, 103, 2]
    Sample_2 = nc2.variables['Information_AQ1_yz'][2, 7, 103, 2]
    averageAQ1 = (Sample_1 + Sample_2) / 2.0
    My_resultn = total_Alanysis_AQ1[7, 103]
    print("averageAQ1", averageAQ1)
    print("my_resultAQ1",My_resultn)
  
    Sample_1 = nc1.variables['w_yz'][1, 7, 103, 2]
    Sample_2 = nc2.variables['w_yz'][2, 7, 103, 2]
    averageAQ2 = (Sample_1 + Sample_2) / 2.0
    My_resultl = total_Alanysis_w[7, 103]
    print("averageAQ2", averageAQ2)
    print("my_resultAQ2",My_resultl)  
  

    
    # Close the input netCDF files
    nc1.close()
    nc2.close()
# Example usage:
file1 = 'Input1.003.nc'
file2 = 'Input1.004.nc'
output_file = 'total_OUT4b.nc'

average_and_save_netcdf(file1, file2, output_file)
