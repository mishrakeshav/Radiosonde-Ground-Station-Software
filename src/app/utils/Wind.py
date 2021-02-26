import math

class Wind:
    # constant(static variable)
    RADIUS_OF_EARTH = 6372795
    TWO_PI = math.pi*2

    @staticmethod
    def square(a):
        return a**2

    @staticmethod
    def calculate_time_difference(previous_time, current_time):
        """
            Keyword arguments
                previous_time   -- Previous Time
                current_time    -- Current Time
            Returns :
                time difference
        """
        return current_time - previous_time

    @staticmethod
    def distance_between(previous_latitude:float, previous_longitude:float,
                                    current_latitude:float, current_longitude:float):
        """
            Keyword arguments

                previous_latitude   -- Previous Latitudes
                previous_longitude  -- Previous Longitude
                current_latitude    -- Current Latitude
                current_longitude   -- Current Longitude

            Returns :
                Distance in meters between two positions, both specified as
                signed decimal-degrees latitude and longitude. Uses great-circle
                distance computation for hypothetical sphere of radius 6372795 meters.
                Because Earth is no exact sphere, rounding errors may be up to 0.5%.
        """
        delta = math.radians(previous_longitude - current_longitude)

        # sin component of longitude
        sdlong = math.sin(delta)
        # cos component of longitude
        cdlong = math.cos(delta)
        #converting to radians
        previous_latitude = math.radians(previous_latitude)
        current_latitude = math.radians(current_latitude)
        # sin component of previous latitude
        sprevious_latitude = math.sin(previous_latitude)
        # cos compenent if previous latitude
        cprevious_latitude = math.cos(previous_latitude)
        # sin component of current latitude
        scurrent_latitude = math.sin(current_latitude)
        # cos compenent if current latitude
        ccurrent_latitude = math.cos(current_latitude)

        delta = (cprevious_latitude*scurrent_latitude) - (sprevious_latitude-ccurrent_latitude*cdlong)
        delta = delta**2
        delta += (Wind.square(ccurrent_latitude*sdlong))
        delta = math.sqrt(delta)

        denom = (sprevious_latitude*scurrent_latitude) + (cprevious_latitude*ccurrent_latitude*cdlong)
        delta = math.atan2(delta,denom)

        return delta*Wind.RADIUS_OF_EARTH



    @staticmethod
    def calculate_wind_speed(previous_latitude:float, previous_longitude:float, current_latitude:float,
                            current_longitude:float, previous_time:int, current_time:int):
        """
            Keyword arguments
                previous_latitude   -- Previous Latitudes
                previous_longitude  -- Previous Longitude
                current_latitude    -- Current Latitude
                current_longitude   -- Current Longitude
                previous_time       -- Previous Time
                current_time        -- Current Time
            Returns :
                returns the Windspeed in m/s
        """
        time = Wind.calculate_time_difference(previous_time, current_time)
        if time == 0:
            return 0
        euclidian_distance = Wind.distance_between(previous_latitude, previous_longitude,
                                                        current_latitude, current_longitude)
        return round(euclidian_distance/time, 3)

    @staticmethod
    def calculate_wind_direction(previous_latitude:float,previous_longitude:float,
                                current_latitude:float, current_longitude:float):

        """
            Keyword arguments

                    previous_latitude   -- Previous Latitudes
                    previous_longitude  -- Previous Longitude
                    current_latitude    -- Current Latitude
                    current_longitude   -- Current Longitude
            Returns:

                Course in degrees (North=0, West=270) from position 1 to position 2,
                both specified as signed decimal-degrees latitude and longitude.
                Because Earth is no exact sphere, calculated course may be off
                by a tiny fraction.
        """
        dlongitude = math.radians(current_longitude-previous_longitude)
        # converting to radians
        previous_latitude = math.radians(previous_latitude)
        current_latitude = math.radians(current_latitude)

        #calculations
        a1 = math.sin(dlongitude)*math.cos(current_latitude)
        a2 = math.sin(previous_latitude)*math.cos(current_latitude)*math.cos(dlongitude)
        a2 = math.cos(previous_latitude)*math.sin(current_latitude) - a2
        a2 = math.atan2(a1,a2)
        if (a2 < 0):
            a2 += Wind.TWO_PI

        return int(math.degrees(a2))
