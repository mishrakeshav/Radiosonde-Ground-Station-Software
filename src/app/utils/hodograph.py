import metpy.calc as mpcalc
from metpy.plots import Hodograph
from metpy.units import units


def hodograph(data_frame, graph):
    wind_speed = data_frame['wind_speed'].values * units.knots
    wind_direction = data_frame['wind_direction'].astype('int')
    u, v = mpcalc.wind_components(wind_speed, wind_direction)

    graph.clear_canvas()
    h = Hodograph(graph.graph.axes, component_range=.5)
    h.add_grid(increment=0.1)
    h.plot_colormapped(u, v, wind_speed)
    graph.graph.draw()
