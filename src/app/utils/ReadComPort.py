
import re
import csv
import time
from datetime import time as time_convert
from Wind import Wind
import time
import traceback, sys


class ReadComPort():
    def __init__(self):
        self.MAXIMUM_TEMPERATURE = 60
        self.MINIMUM_TEMPERATURE = -90
        self.MAXIMUM_PRESSURE = 1100
        self.MINIMUM_PRESSURE = 3
        
        self.init_time = None
        self.previous_latitude = 0
        self.previous_longitude = 0
        self.previous_time = 0
        self.wind_speed = 0
        self.path = 'raw/18Oct2019_16_36.raw'
        self.file_input = open(
            self.path,
            encoding='utf8',
            errors='ignore'
        )
        self.field_names = ['Sr.No.', 'Time', 'Latitude', 'Longitude', 'Satelites', 'Altitude',
             'Pressure', 'Internal Temperature', 'External Temperature', 'Humidity',
             'TimeElapsed', 'Wind Direction', 'Wind Speed', 'Scaled Pressure', 'Scaled Temperature']
        self.counter = 1
        self.write_index()
    
    def write_index(self):
        with open('output.csv', 'w') as file_output:
            wr = csv.writer(file_output)
            wr.writerow(self.field_names)

    def get_time_elapsed(self,time_):
        hour = int(time_[:2])
        mins = int(time_[2:4])
        secs = int(time_[4:6])
        current_time = time_convert(hour, mins, secs)
        current_time_second = current_time.hour * 60*60 + current_time.minute*60  + current_time.second

        if self.init_time is None:
            self.init_time = current_time_second
        return current_time_second - self.init_time, current_time
    
    def write_values(self,filename, *args):
        with open(filename, 'a') as file_output:
            wr = csv.writer(file_output)
            wr.writerow(args[0])
    
    def read_com_port(self):
        data = self.file_input.readline()
        if data[0] == '$':
            try:
                val = re.split('gpggat|l|xno|yeq1s|h|P|I|E|U|X|1234567890', data)
                latitude = float(val[2])/100
                longitude = float(val[3])/100
                time_elapsed, time_ = self.get_time_elapsed(val[1])
                satellite = int(val[4])
                altitude = float(val[5])
                pressure = int(val[6])/10
                internal_temperature = int(val[7])/100
                external_temperature = int(val[8])/100
                humidity = int(val[9])/100

                wind_direction = Wind.calculate_wind_direction( self.previous_latitude, self.previous_longitude,latitude,longitude)
                if time_elapsed != self.previous_time:
                    self.wind_speed = Wind.calculate_wind_speed(
                        self.previous_latitude, self.previous_longitude,latitude ,
                        longitude, self.previous_time, time_elapsed
                    )
                self.previous_latitude = latitude
                self.previous_longitude = longitude
                self.previous_time = time_elapsed
                scaled_pressure = (pressure/(self.MAXIMUM_PRESSURE - self.MINIMUM_PRESSURE))*100
                sacled_external_temperature = (external_temperature/(self.MAXIMUM_TEMPERATURE - self.MINIMUM_TEMPERATURE))*100

                values = [self.counter, time_, latitude, longitude, satellite, altitude, \
                    pressure, internal_temperature, external_temperature, humidity, time_elapsed, \
                    wind_direction, self.wind_speed, scaled_pressure, sacled_external_temperature]
                
                self.write_values('output.csv',values)
                self.counter += 1 
            except Exception as e:
                print(e)

if __name__ == '__main__':
    read_com_port = ReadComPort()
    for i in range(3000):
        read_com_port.read_com_port()

