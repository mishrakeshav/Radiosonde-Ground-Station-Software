import numpy as np


def stuve(data_frame, graph):
    press_mb = data_frame['pressure']
    temp_C = data_frame['external_temperature']
    td_C = data_frame['dew_point']
    x = np.arange(220, 460, 10)
    y = np.arange(100, 1026, 25)
    temp_C = [i + 273.15 for i in temp_C]
    td_C = [i + 273.15 for i in td_C]

    theta_2D, P_2D = np.meshgrid(x, y)
    T_2D = theta_2D * (P_2D / 1000.) ** 0.286

    y = np.arange(40000, 102600, 2500)

    x = np.array([0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.,
                  3., 4., 6., 8., 10., 12., 16., 20.])

    x = x / 1000.

    labels = ['0.1', '0.2', '0.4', '0.6', '0.8', '1', '1.5',
              '2', '3', '4', '6', '8', '10', '12', '16', '20']

    ws_2D, Pws_2D = np.meshgrid(x, y)
    ws_T_2D = 1. / (1. / 273.15 - 1.844e-4 *
                    np.log(ws_2D * Pws_2D / 611.3 / (ws_2D + 0.622)))

    graph.graph.fig.clf()
    graph.graph.axes.set_yscale('log')
    graph.graph.axes.set_xlabel('temp K')
    graph.graph.axes.set_ylabel('pressure mb')
    graph.graph.axes.set_title('Stuve chart')
    graph.graph.axes.set_xlim(200, 300)
    graph.graph.axes.set_ylim(1025, 400)
    graph.graph.axes.minorticks_off()
    graph.graph.axes.set_xticks(np.arange(200, 301, 10))
    graph.graph.axes.set_yticks([1000, 850, 700, 600, 500, 400])
    graph.graph.axes.set_yticklabels(
        ['1000', '850', '700', '600', '500', '400'])
    graph.graph.axes.grid(True)
    graph.graph.axes.plot(
        ws_T_2D, Pws_2D * 0.01, color='#a4c2f4', linestyle='dashed')
    graph.graph.axes.plot(T_2D, P_2D, color='#f6b26b')
    graph.graph.axes.plot(temp_C, press_mb, 'r', lw=2)
    graph.graph.axes.plot(td_C, press_mb, 'g', lw=2)

    for i in np.arange(16):
        graph.graph.axes.text(
            ws_T_2D[3, i], Pws_2D[3, i] * 0.01,
            labels[i],
            color='#0000f4',
            ha='center',
            weight='bold'
        )
        graph.graph.axes.text(
            ws_T_2D[22, i], Pws_2D[22, i] * 0.01,
            labels[i],
            color='#0000f4',
            ha='center',
            weight='bold'
        )

    graph.graph.draw()
