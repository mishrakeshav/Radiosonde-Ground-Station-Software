from PySide2.QtWidgets import *

import numpy as np
import pandas as pd
import metpy.calc as mpcalc
from metpy.plots import Hodograph, SkewT
from metpy.units import units
from tephi import Tephigram

from src.app.components.constants import *
from src.app.views.FlightDashboardWindow import FlightDashboardWindow
from src.app.views.ViewMap import MapView
from src.app.utils.net_cdf import cdf


class FlightDashboardController(FlightDashboardWindow):
    def __init__(self, main_window, flight_folder_path):
        self.main_window = main_window
        self.flight_folder_path = flight_folder_path
        self.setupUi(main_window=main_window)

        path = os.path.join(flight_folder_path, 'output.csv')
        self.data_frame = pd.read_csv(path)

        self.parameter_list = [
            (self.temperature_check, 'external_temperature', COLOR_TEMPERATURE),
            (self.pressure_check, 'pressure', COLOR_PRESSURE),
            (self.altitude_check, 'altitude', COLOR_ALTITUDE),
            (self.humidity_check, 'humidity', COLOR_HUMIDITY),
            (self.wind_speed_check, 'wind_speed', COLOR_WINDSPEED),
        ]

        self.hodograph_check.toggled.connect(lambda flag: self.update_spec_graphs(flag, self.update_hodograph))
        self.skewt_check.toggled.connect(lambda flag: self.update_spec_graphs(flag, self.update_skewt))
        self.tphi_check.toggled.connect(lambda flag: self.update_spec_graphs(flag, self.update_tphi))
        self.stuve_check.toggled.connect(lambda flag: self.update_spec_graphs(flag, self.update_stuve))

        # Update the graphs when the checkboxes change their state
        for checkbox, _, _ in self.parameter_list:
            checkbox.stateChanged.connect(self.update_graph)

        # setting up the menu bar
        self.actionTrack_Balloon.triggered.connect(self.open_map)
        self.actionCreate_File.triggered.connect(lambda: cdf(self.data_frame))

        self.update_table()
        self.update_graph()

    def open_map(self):
        _ = MapView(self.flight_folder_path)

    def update_table(self):
        cols = ['time', 'pressure', 'external_temperature', 'humidity', 'wind_speed', 'wind_direction']

        for row_number in range(len(self.data_frame)):
            self.table.insertRow(row_number)
            for col_number, col in enumerate(cols):
                self.table.setItem(row_number, col_number, QTableWidgetItem(str(self.data_frame.iloc[row_number][col])))

    def update_graph(self):
        self.graph_time.clear_canvas()
        self.graph_altitude.clear_canvas()

        for parameter_check, parameter_name, color in self.parameter_list:
            if parameter_check.isChecked():
                self.graph_time.plot(
                    x=self.data_frame["time_elapsed"],
                    y=self.data_frame[parameter_name],
                    c=color)

                if parameter_name == "altitude": continue

                self.graph_altitude.plot(
                    x=self.data_frame[parameter_name],
                    y=self.data_frame["altitude"],
                    c=color)

        self.graph_time.set_xlabel('Time Elapsed (s)')
        self.graph_time.set_ylabel('Parameters (units)')

        self.graph_altitude.set_xlabel('Parameters (units)')
        self.graph_altitude.set_ylabel('Altitude (m)')

        self.graph_altitude.graph.axes.grid()
        self.graph_time.graph.axes.grid()

        self.graph_altitude.graph.draw()
        self.graph_time.graph.draw()

    def update_hodograph(self):
        wind_speed = self.data_frame['wind_speed'].values * units.knots
        wind_direction = self.data_frame['wind_direction'].values * units.degrees
        u, v = mpcalc.wind_components(wind_speed, wind_direction)

        self.spec_graph.clear_canvas()
        h = Hodograph(self.spec_graph.graph.axes, component_range=.5)
        h.add_grid(increment=0.1)
        h.plot_colormapped(u, v, wind_speed)
        self.spec_graph.graph.draw()

    def update_skewt(self):
        self.data_frame['Td'] = self.data_frame['external_temperature'].values - (
                (100 - self.data_frame['humidity']) / 5)
        p = self.data_frame['pressure'].values * units.hPa
        T = self.data_frame['external_temperature'].values * units.degC
        Td = self.data_frame['Td'].values * units.degC
        wind_speed = self.data_frame['wind_speed'].values * units.knots
        wind_direction = self.data_frame['wind_direction'].values * units.degrees
        u, v = mpcalc.wind_components(wind_speed, wind_direction)

        figure = self.spec_graph.graph.fig
        figure.clf()

        skew = SkewT(figure)
        skew.plot(p, T, 'r', linewidth=2)
        skew.plot(p, Td, 'g', linewidth=2)
        skew.plot_barbs(p, u, v)
        self.spec_graph.graph.draw()

    def update_tphi(self):
        self.data_frame['Td'] = self.data_frame['external_temperature'].values - (
                (100 - self.data_frame['humidity'].values) / 5)
        dewpoint = list(zip(self.data_frame['pressure'], self.data_frame['Td']))
        drybulb = list(zip(self.data_frame['pressure'], self.data_frame['external_temperature']))

        figure = self.spec_graph.graph.fig
        figure.clf()

        tephigram = Tephigram(figure=figure)
        tephigram.plot(dewpoint, label="Dew Point Temperature", color="blue")
        tephigram.plot(drybulb, label="Dry Bulb Temperature", color="red")
        self.spec_graph.graph.draw()

    def update_stuve(self):
        self.data_frame['Td'] = self.data_frame['external_temperature'].values - (
                (100 - self.data_frame['humidity'].values) / 5)

        press_mb = self.data_frame['pressure'].tolist()
        temp_C = self.data_frame['external_temperature'].tolist()
        td_C = self.data_frame['Td'].tolist()
        x = np.arange(220, 460, 10)
        y = np.arange(100, 1026, 25)
        temp_C = [i + 273.15 for i in temp_C]
        td_C = [i + 273.15 for i in td_C]
        theta_2D, P_2D = np.meshgrid(x, y)
        T_2D = theta_2D * (P_2D / 1000.) ** 0.286
        y = np.arange(40000, 102600, 2500)
        x = np.array([0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.,
                      3., 4., 6., 8., 10., 12., 16., 20.])
        labels = ['0.1', '0.2', '0.4', '0.6', '0.8', '1', '1.5',
                  '2', '3', '4', '6', '8', '10', '12', '16', '20']
        x = x / 1000.
        ws_2D, Pws_2D = np.meshgrid(x, y)
        ws_T_2D = 1. / (1. / 273.15 - 1.844e-4 *
                        np.log(ws_2D * Pws_2D / 611.3 / (ws_2D + 0.622)))

        self.spec_graph.graph.fig.clf()

        self.spec_graph.graph.axes.set_yscale('log')
        self.spec_graph.graph.axes.set_xlabel('temp K')
        self.spec_graph.graph.axes.set_ylabel('pressure mb')
        self.spec_graph.graph.axes.set_title('Stuve chart')
        self.spec_graph.graph.axes.set_xlim(200, 300)
        self.spec_graph.graph.axes.set_ylim(1025, 400)
        self.spec_graph.graph.axes.minorticks_off()
        self.spec_graph.graph.axes.set_xticks(np.arange(200, 301, 10))
        self.spec_graph.graph.axes.set_yticks([1000, 850, 700, 600, 500, 400])
        self.spec_graph.graph.axes.set_yticklabels(
            ['1000', '850', '700', '600', '500', '400'])
        self.spec_graph.graph.axes.grid(True)
        self.spec_graph.graph.axes.plot(
            ws_T_2D, Pws_2D * 0.01, color='#a4c2f4', linestyle='dashed')
        self.spec_graph.graph.axes.plot(T_2D, P_2D, color='#f6b26b')
        self.spec_graph.graph.axes.plot(temp_C, press_mb, 'r', lw=2)
        self.spec_graph.graph.axes.plot(td_C, press_mb, 'g', lw=2)

        for i in np.arange(16):
            self.spec_graph.graph.axes.text(
                ws_T_2D[3, i], Pws_2D[3, i] * 0.01, labels[i], color='#0000f4', ha='center', weight='bold')
            self.spec_graph.graph.axes.text(
                ws_T_2D[22, i], Pws_2D[22, i] * 0.01, labels[i], color='#0000f4', ha='center', weight='bold')

        self.spec_graph.graph.draw()

    def update_spec_graphs(self, flag, function):
        if flag: function()
