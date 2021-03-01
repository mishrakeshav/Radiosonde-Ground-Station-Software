import io
import folium


class Map:
    def generate_map(self, lats, long):
        loc = list(zip(lats, long))
        m = folium.Map(location=[lats[-1], long[-1]],
                       zoom_start=15)
        folium.PolyLine(loc, color='red', weight=10).add_to(m)
        self.data = io.BytesIO()
        m.save(self.data, close_file=False)
