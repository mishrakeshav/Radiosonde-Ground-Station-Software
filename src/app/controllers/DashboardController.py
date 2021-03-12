from PySide2.QtWidgets import *
from PySide2.QtCore import *

import json
import pandas as pd
from math import ceil
from datetime import datetime, time
import serial

from src.app.utils.Wind import Wind
from src.app.utils.Worker import Worker
from src.app.utils.net_cdf import cdf
from src.app.utils.skewt import skewt
from src.app.utils.hodograph import hodograph
from src.app.utils.tephigram import tephigram
from src.app.utils.stuve import stuve
from src.app.views.DashboardWindow import DashboardWindow
from src.app.views.ViewMap import MapView
from src.app.components.constants import *


def parse_time(time_):
    hours, minutes, seconds = int(time_[:2]), int(time_[2:4]), int(time_[4:])
    return time(hours, minutes, seconds)


class DashboardController(DashboardWindow):
    def __init__(self, main_window, flight_folder_path, comport_name):
        super().__init__()

        self.main_window = main_window
        self.flight_folder_path = flight_folder_path
        self.comport_name = comport_name
        self.flight_init_time = datetime.utcnow()
        self.previous_time = 0

        path = os.path.join(flight_folder_path, 'params.json')
        with open(path) as json_file:
            flight_data = json.load(json_file)
            self.previous_latitude = flight_data["data"]["latitude"]
            self.previous_longitude = flight_data["data"]["longitude"]

        path = os.path.join(flight_folder_path, 'output.csv')
        self.data_frame = pd.read_csv(path)

        self.comport = serial.Serial(port=self.comport_name, baudrate=BAUD_RATE, timeout=TIMEOUT)
        self.setupUi(main_window=main_window)
        self.parameter_list = [
            (self.temperature_check, 'external_temperature', COLOR_TEMPERATURE),
            (self.pressure_check, 'pressure', COLOR_PRESSURE),
            (self.altitude_check, 'altitude', COLOR_ALTITUDE),
            (self.humidity_check, 'humidity', COLOR_HUMIDITY),
            (self.wind_speed_check, 'wind_speed', COLOR_WINDSPEED),
        ]

        # setting up the menu bar
        self.actionTrack_Balloon.triggered.connect(self.open_map)
        self.actionCreate_File.triggered.connect(lambda: cdf(self.data_frame, self.flight_folder_path))

        self.threadpool = QThreadPool()
        self.run_threads()

    def open_map(self):
        print('Generating Map')
        _ = MapView(self.flight_folder_path)

    def read_port(self):
        output_file = os.path.join(self.flight_folder_path, "output.csv")
        while True:
            if self.comport.in_waiting:
                data = self.comport.read_until().decode('ascii').split(",")
                data = [data[0]] + list(map(lambda x: float(x), data[1:]))
                time_str, latitude, longitude, satellite, altitude, pressure, internal_temperature, \
                    external_temperature, humidity = data
                time_parsed = parse_time(time_str)
                data[0] = time_parsed
                time_elapsed = ceil((datetime.utcnow() - self.flight_init_time).total_seconds())

                wind_direction = Wind.calculate_wind_direction(
                    self.previous_latitude,
                    self.previous_longitude,
                    latitude,
                    longitude
                )

                wind_speed = Wind.calculate_wind_speed(
                    self.previous_latitude,
                    self.previous_longitude,
                    latitude,
                    longitude,
                    self.previous_time,
                    time_elapsed
                )

                scaled_pressure = pressure / (PRESSURE_MAXIMUM - PRESSURE_MINIMUM) * 100

                scaled_external_temperature = external_temperature / (TEMPERATURE_MAXIMUM - TEMPERATURE_MINIMUM) * 100

                dew_point = external_temperature - ((100 - humidity) / 5)

                data_dict = {
                    'time': time_parsed,
                    'latitude': latitude,
                    'longitude': longitude,
                    'satellite': satellite,
                    'altitude': altitude,
                    'pressure': pressure,
                    'internal_temperature': internal_temperature,
                    'external_temperature': external_temperature,
                    'dew_point': dew_point,
                    'humidity': humidity,
                    'time_elapsed': time_elapsed,
                    'wind_direction': wind_direction,
                    'wind_speed': wind_speed,
                    'scaled_pressure': scaled_pressure,
                    'scaled_external_temperature': scaled_external_temperature
                }

                data.extend([time_elapsed, wind_direction, wind_speed,
                             scaled_pressure, scaled_external_temperature, dew_point])

                data = list(map(lambda x: str(x), data))
                with open(output_file, 'a') as file_output:
                    file_output.write(",".join(data) + "\n")

                self.data_frame = self.data_frame.append(data_dict, ignore_index=True)

                self.update_graph()
                self.update_table(data_dict)
                self.update_gauge(data_dict)
                self.update_spec_graphs()

                self.previous_longitude = longitude
                self.previous_latitude = latitude
                self.previous_time = time_elapsed

    def update_gauge(self, data):
        self.pressure_gauge.update_gauge(data['pressure'])
        self.temperature_gauge.update_gauge(data['external_temperature'])
        self.humidity_gauge.update_gauge(data['humidity'])
        self.wind_speed_gauge.update_gauge(data['wind_speed'])
        self.wind_direction_gauge.update_gauge(data['wind_direction'])
        self.altitude_gauge.update_gauge(data['altitude'])

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

    def update_table(self, data):
        cols = ['time', 'pressure', 'external_temperature', 'humidity', 'wind_speed', 'wind_direction']
        row = self.table.rowCount()
        self.table.insertRow(row)
        for index, name in enumerate(cols):
            self.table.setItem(row, index, QTableWidgetItem(str(data[name])))

    def update_spec_graphs(self):
        if self.hodograph_check.isChecked():
            hodograph(data_frame=self.data_frame, graph=self.spec_graph)
        elif self.tphi_check.isChecked():
            tephigram(data_frame=self.data_frame, graph=self.spec_graph)
        elif self.skewt_check.isChecked():
            skewt(data_frame=self.data_frame, graph=self.spec_graph)
        elif self.stuve_check.isChecked():
            stuve(data_frame=self.data_frame, graph=self.spec_graph)

    def run_threads(self):
        worker1 = Worker(self.read_port)
        self.threadpool.start(worker1)
