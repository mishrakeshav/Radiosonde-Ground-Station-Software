import metpy.calc as mpcalc
from metpy.plots import SkewT
from metpy.units import units


def skewt(data_frame, graph):
    p = data_frame['pressure'].values * units.hPa
    T = data_frame['external_temperature'].values * units.degC
    Td = data_frame['dew_point'].values * units.degC
    wind_speed = data_frame['wind_speed'].values * units.knots
    wind_direction = data_frame['wind_direction'].astype('int')
    u, v = mpcalc.wind_components(wind_speed, wind_direction)

    figure = graph.graph.fig
    figure.clf()

    skew = SkewT(figure)
    skew.plot(p, T, 'r', linewidth=2)
    skew.plot(p, Td, 'g', linewidth=2)
    skew.plot_barbs(p, u, v)
    graph.graph.draw()
