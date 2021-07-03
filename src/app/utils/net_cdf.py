import os
import pandas as pd
import numpy as np
from datetime import datetime
import netCDF4 as nc

CALENDAR = 'standard'
UNITS = 'seconds since 1970-01-01 00:00:00'


def cdf(data_frame, flight_folder_path):
    print("Compiling the NETCDF Document...")
    n_rows, n_cols = data_frame.shape

    # TODO: This check is naive. There can be pressure values below 800hPa ...
    if data_frame['pressure'][n_rows - 1] > 800:
        # TODO: NETCDF cannot be compiled as the pressure conditions are not met
        #  Inform this to the user as an alert
        return

    # File Creation
    now = datetime.utcnow()
    now = now.strftime("%Y%m%d_%H%M%S")
    file_name = 'Indravani' + '_' + now + '.nc'
    path = os.path.join(flight_folder_path, file_name)

    # Create Dimension
    ncout = nc.Dataset(path, 'w', format='NETCDF4')
    ncout.createDimension('base_time', 1)
    ncout.createDimension('time_elapsed', n_rows)
    ncout.createDimension('time', n_rows)
    ncout.createDimension('latitude', n_rows)
    ncout.createDimension('longitude', n_rows)
    ncout.createDimension('altitude', n_rows)
    ncout.createDimension('pressure', n_rows)
    ncout.createDimension('humidity', n_rows)
    ncout.createDimension('wind_direction', n_rows)
    ncout.createDimension('wind_speed', n_rows)
    ncout.createDimension('temperature', n_rows)
    ncout.createDimension('dew_point', n_rows)

    base_time = ncout.createVariable('base_time', 'i8', ('base_time',))
    base_time.standard_name = 'Launch Time'
    base_time.long_name = 'Radiosonde Launch Time'
    base_time.units = 'UNIX time'

    time_elapsed = ncout.createVariable('time_elapsed', "i8", ('time_elapsed',))
    time_elapsed.long_name = 'Time Elapsed'
    time_elapsed.units = 'seconds'
    time_elapsed.calendar = 'standard'
    time_elapsed.axis = 'T'

    time = ncout.createVariable('time', "i8", ('time',))
    time.long_name = 'time'
    time.units = 'seconds since 1990-01-01 00:00:00'
    time.calendar = 'standard'
    time.axis = 'T'

    longitude = ncout.createVariable('longitude', np.dtype('double').char, ('longitude',))
    longitude.standard_name = 'longitude'
    longitude.long_name = 'longitude'
    longitude.units = 'degrees_east'
    longitude.axis = 'X'

    latitude = ncout.createVariable('latitude', np.dtype('double').char, ('latitude',))
    latitude.standard_name = 'latitude'
    latitude.long_name = 'latitude'
    latitude.units = 'degrees_north'
    latitude.axis = 'Y'

    altitude = ncout.createVariable('altitude', np.dtype('double').char, ('altitude',))
    altitude.standard_name = 'altitude'
    altitude.long_name = 'altitude'
    altitude.units = 'meters (m)'

    pressure = ncout.createVariable('pressure', np.dtype('double').char, ('pressure',))
    pressure.standard_name = 'pressure'
    pressure.long_name = 'pressure'
    pressure.units = 'hectopascal (hPa)'

    humidity = ncout.createVariable('humidity', np.dtype('double').char, ('humidity',))
    humidity.standard_name = 'Humidity'
    humidity.long_name = 'Humidity'
    humidity.units = 'percent (%)'

    wind_direction = ncout.createVariable('wind_direction', np.dtype('double').char, ('wind_direction',))
    wind_direction.standard_name = 'Wind Direction'
    wind_direction.long_name = 'Wind Direction'
    wind_direction.units = 'degrees'

    wind_speed = ncout.createVariable('wind_speed', np.dtype('double').char, ('wind_speed',))
    wind_speed.standard_name = 'Wind Speed'
    wind_speed.long_name = 'Wind Speed'
    wind_speed.units = 'm/s'

    temperature = ncout.createVariable('temperature', np.dtype('double').char, ('temperature',))
    temperature.standard_name = 'Temperature'
    temperature.long_name = 'Dry Temperature'
    temperature.units = 'degree Celsius'

    dew_point = ncout.createVariable('dew_point', np.dtype('double').char, ('dew_point',))
    dew_point.standard_name = 'Dew Point'
    dew_point.long_name = 'Dew Point'
    dew_point.units = 'degree Celsius'

    # Process datetime
    data_frame["time"] = pd.to_datetime(data_frame['time'])
    time_seconds = data_frame['time'].apply(lambda x: nc.date2num(x, units=UNITS, calendar=CALENDAR))

    base_time[:] = nc.date2num(data_frame['time'][0], units=UNITS, calendar=CALENDAR)
    time_elapsed[:] = data_frame['time_elapsed']
    time[:] = time_seconds
    longitude[:] = data_frame['longitude']
    latitude[:] = data_frame['latitude']
    altitude[:] = data_frame['altitude']
    pressure[:] = data_frame['pressure']
    humidity[:] = data_frame['humidity']
    wind_direction[:] = data_frame['wind_direction']
    wind_speed[:] = data_frame['wind_speed']
    temperature[:] = data_frame['external_temperature']
    dew_point[:] = data_frame['external_temperature'].values - ((100 - data_frame['humidity']) / 5)
    ncout.close()

    print("NETCDF Document compiled Successfully...")
