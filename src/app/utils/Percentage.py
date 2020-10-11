TEMPERATURE_MAXIMUM = 60
TEMPERATURE_MINIMUM = -90
PRESSURE_MAXIMUM = 1060
PRESSURE_MINIMUM = 3
HUMIDITY_MAXIMUM = 100
HUMIDITY_MINIMUM = 0
WIND_SPEED_MAXIMUM = 180
WIND_SPEED_MINIMUM = 0
WIND_DIRECTION_MAXIMUM = 360
WIND_DIRECTION_MINIMUM = 0
ALTITUDE_MAXIMUM = 40000
ALTITUDE_MINIMUM = 0

def min_max(value):
    return max(1, min(value, 100))


class Percentage:

    @staticmethod
    def get_pressure(value):
        return min_max(int(value//(PRESSURE_MAXIMUM-PRESSURE_MINIMUM))*100)
    
    @staticmethod
    def get_temperature(value):
        return min_max(int(value//(TEMPERATURE_MAXIMUM-TEMPERATURE_MINIMUM))*100)
    
    @staticmethod
    def get_wind_speed(value):
        return min_max(int(value//(WIND_SPEED_MAXIMUM-WIND_SPEED_MINIMUM))*100)
    
    @staticmethod
    def get_wind_direction(value):
        return min_max(int(value//(WIND_DIRECTION_MAXIMUM-WIND_DIRECTION_MINIMUM))*100)
    
    @staticmethod
    def get_altitude(value):
        return min_max(int(value//(ALTITUDE_MAXIMUM-ALTITUDE_MINIMUM))*100)


