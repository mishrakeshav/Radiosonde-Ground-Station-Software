import netCDF4 as nc

PATH = '/home/phoenix/Desktop/Projects/Radiosonde-Ground-Station-Software/src/export/20210306_043308/Indravani_788_20210306_043637.nc'

if __name__ == '__main__':
    df = nc.Dataset(PATH)
    print(f"Variables: {type(df.variables)}")
    time_variable = df.variables['time']
    print(time_variable[:])
