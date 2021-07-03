from PySide2.QtWidgets import *

import pandas as pd

from src.app.utils.hodograph import hodograph
from src.app.utils.skewt import skewt
from src.app.utils.tephigram import tephigram
from src.app.utils.stuve import stuve
from src.app.utils.net_cdf import cdf
from src.app.components.constants import *
from src.app.views.FlightDashboardWindow import FlightDashboardWindow
from src.app.views.ViewMap import MapView


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

        self.hodograph_check.toggled.connect(self.update_spec_graphs)
        self.skewt_check.toggled.connect(self.update_spec_graphs)
        self.tphi_check.toggled.connect(self.update_spec_graphs)
        self.stuve_check.toggled.connect(self.update_spec_graphs)

        # Update the graphs when the checkboxes change their state
        for checkbox, _, _ in self.parameter_list:
            checkbox.stateChanged.connect(self.update_graph)

        # setting up the menu bar
        self.actionTrack_Balloon.triggered.connect(self.open_map)
        self.actionCreate_File.triggered.connect(lambda: cdf(self.data_frame, self.flight_folder_path))

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

                if parameter_name == "altitude":
                    continue

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

    def update_spec_graphs(self):
        if self.hodograph_check.isChecked():
            hodograph(data_frame=self.data_frame, graph=self.spec_graph)
        elif self.tphi_check.isChecked():
            tephigram(data_frame=self.data_frame, graph=self.spec_graph)
        elif self.skewt_check.isChecked():
            skewt(data_frame=self.data_frame, graph=self.spec_graph)
        elif self.stuve_check.isChecked():
            stuve(data_frame=self.data_frame, graph=self.spec_graph)
