import datetime as dt
import xarray as xr
date = dt.datetime.now()
year = '{:04d}'.format(date.year)
month='{:02d}'.format(date.month)
day='{:02d}'.format(date.day)
horizon_start = 0;
horizon = 26;
hours = ['00', '06', '12', '18']
for j in hours:
    jstr = str(j);
    for k in range(horizon_start,horizon):
        kstr = "{0:0=3d}".format(3 * k)
        url = 'http://www.ncei.noaa.gov/thredds/dodsC/gfs-003-files/'+year+month+'/'+year+month+day+'/gfs_3_'+year+month+day+'_'+jstr+'00_'+kstr+'.grb2'
        print(url)
		nc = xr.open_dataset(url, engine='netcdf4')
		#v-component_of_wind_height_above_ground
		wvh=nc.variables['v-component_of_wind_height_above_ground']
		wvh_value=wvh.values
		v_component_of_wind_height_above_ground_80m = wvh_value[0,1,25,68]
		print(v_component_of_wind_height_above_ground_80m)
		wuh=nc.variables['u-component_of_wind_height_above_ground']
		wuh_value=wuh.values
		u_component_of_wind_height_above_ground_80m = wuh_value[0,1,25,68]
		print(u_component_of_wind_height_above_ground_80m)
		
		

