import math


class Wind:
    # constant(static variable)
    RADIUS_OF_EARTH = 6372795
    TWO_PI = math.pi * 2

    @staticmethod
    def distance_between(lat1_deg: float, lon1_deg: float,
                         lat2_deg: float, lon2_deg: float):
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

        lat1_rad = math.radians(lat1_deg)
        lat2_rad = math.radians(lat2_deg)

        lat_diff_rad = math.radians(lat2_deg - lat1_deg)
        lon_diff_rad = math.radians(lon2_deg - lon1_deg)

        a = math.pow(math.sin(lat_diff_rad / 2), 2) + \
            math.cos(lat1_rad) * math.cos(lat2_rad) * \
            math.pow(math.sin(lon_diff_rad / 2), 2)

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = Wind.RADIUS_OF_EARTH * c
        return distance

    @staticmethod
    def calculate_wind_speed(previous_latitude: float, previous_longitude: float, current_latitude: float,
                             current_longitude: float, previous_time: int, current_time: int):
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

        time = current_time - previous_time
        if time == 0:
            return 0
        euclidean_distance = Wind.distance_between(previous_latitude, previous_longitude,
                                                   current_latitude, current_longitude)
        return round(euclidean_distance / time, 3)

    @staticmethod
    def calculate_wind_direction(previous_latitude: float, previous_longitude: float,
                                 current_latitude: float, current_longitude: float):
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

        dlongitude = math.radians(current_longitude - previous_longitude)
        # converting to radians
        previous_latitude = math.radians(previous_latitude)
        current_latitude = math.radians(current_latitude)

        # calculations
        a1 = math.sin(dlongitude) * math.cos(current_latitude)
        a2 = math.sin(previous_latitude) * math.cos(current_latitude) * math.cos(dlongitude)
        a2 = math.cos(previous_latitude) * math.sin(current_latitude) - a2
        a2 = math.atan2(a1, a2)
        if a2 < 0:
            a2 += Wind.TWO_PI

        return int(math.degrees(a2))
