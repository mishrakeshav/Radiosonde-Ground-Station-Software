import os
import sys
import folium

PATH = sys.path[0]

class Map:
    def generate_map(self, lats, long):
        loc = list(zip(lats, long))
        m = folium.Map(location=[lats[-1], long[-1]],
                      zoom_start=15, tiles="Stamen Toner")
        folium.PolyLine(loc, color='red', weight=5).add_to(m)
        m.save(os.path.join(PATH, "index.html"))
