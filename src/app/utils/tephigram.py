from tephi import Tephigram


def tephigram(data_frame, graph):
    dew_point = list(zip(data_frame['pressure'], data_frame['dew_point']))
    dry_bulb = list(zip(data_frame['pressure'], data_frame['external_temperature']))

    figure = graph.graph.fig
    figure.clf()

    tephigram = Tephigram(figure=figure)
    tephigram.plot(dew_point, label="Dew Point Temperature", color="blue")
    tephigram.plot(dry_bulb, label="Dry Bulb Temperature", color="red")
    graph.graph.draw()
