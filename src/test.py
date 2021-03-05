import math

R = 6371e3

lat1_rad = math.radians(lat1_deg)
lat2_rad = math.radians(lat2_deg)

lat_diff_rad = math.radians(lat2_deg-lat1_deg)
lon_diff_rad = math.radians(lon2_deg-lon1_deg)

a = math.pow(math.sin(lat_diff_rad/2), 2) + \
    math.cos(lat1_rad) * math.cos(lat2_rad) * \
    math.pow(math.sin(lon_diff_rad/2), 2)

c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

d = R * c