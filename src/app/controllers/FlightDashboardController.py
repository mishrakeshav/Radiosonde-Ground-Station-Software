from PySide2.QtWidgets import *

from datetime import datetime
import numpy as np
import pandas as pd
import metpy.calc as mpcalc
from metpy.plots import Hodograph, SkewT
from metpy.units import units
from tephi import Tephigram
import netCDF4 as nc

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

        self.spec_graph_list = [
            (self.hodograph_check, self.update_hodograph),
            (self.skewt_check, self.update_skewt),
            (self.tphi_check, self.update_tphi),
            (self.stuve_check, self.update_stuve),
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
        self.actionCreate_File.triggered.connect(self.cdf)

        self.update_table()
        self.update_graph()

    def open_map(self):
        _ = MapView(self.flight_folder_path)

    def update_table(self):
        cols = ['time', 'pressure', 'external_temperature', 'humidity', 'wind_speed', 'wind_direction']

        for row_number in range(len(self.data_frame)):
            for col_number, col in enumerate(cols):
                self.table.setItem(row_number + 1, col_number, QTableWidgetItem(self.data_frame.iloc[row_number][col]))

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

    def cdf(self):
        x = len(self.data_frame['Pressure'])
        if (self.data_frame['Pressure'][x - 1] <= 800):
            self.data_frame["Time"] = pd.to_datetime(self.data_frame['Time'])
            timed = self.data_frame['Time'][0]
            format = '%Y-%m-%d %H:%M:%S'  # The format
            timed = str(timed)
            timed = datetime.strptime(timed, format)
            calendar = 'standard'
            units = 'seconds since 1970-01-01 00:00:00'
            timed = nc.date2num(timed, units=units, calendar=calendar)
            size = len(self.data_frame['Time'])
            times = [timed + self.data_frame['TimeElapsed'][i] for i in range(size)]

            now = datetime.utcnow()
            now = now.strftime("%Y%m%d_%H%M%S")
            netfile = 'Indravani' + '_' + str(int(self.data_frame['Pressure'][x - 1])) + '_' + now + '.nc'

            ncout = nc.Dataset(netfile, 'w', format='NETCDF4')
            base = 1
            ncout.createDimension('base_time', base)
            ncout.createDimension('time_offset', size)
            ncout.createDimension('time', size)
            ncout.createDimension('lat', size)
            ncout.createDimension('lon', size)
            ncout.createDimension('alt', size)
            ncout.createDimension('pres', size)
            ncout.createDimension('rh', size)
            ncout.createDimension('wdir', size)
            ncout.createDimension('wspd', size)
            ncout.createDimension('tdry', size)
            ncout.createDimension('dp', size)

            base_time = ncout.createVariable('base_time', 'i8', ('base_time'))
            base_time.standard_name = 'Launch Time'
            base_time.long_name = 'Radiosonde Launch Time'
            base_time.units = 'seconds since 1990-01-01 00:00:00'
            time_offset = ncout.createVariable('time_offset', "i8", ('time_offset',))
            time_offset.long_name = 'Time Elapsed'
            time_offset.units = 'seconds'
            time_offset.calendar = 'standard'
            time_offset.axis = 'T'
            time = ncout.createVariable('time', "i8", ('time',))
            time.long_name = 'time'
            time.units = 'seconds since 1990-01-01 00:00:00'
            time.calendar = 'standard'
            time.axis = 'T'
            lon = ncout.createVariable('lon', np.dtype('double').char, ('lon'))
            lon.standard_name = 'longitude'
            lon.long_name = 'longitude'
            lon.units = 'degrees_east'
            lon.axis = 'X'
            lat = ncout.createVariable('lat', np.dtype('double').char, ('lat'))
            lat.standard_name = 'latitude'
            lat.long_name = 'latitude'
            lat.units = 'degrees_north'
            lat.axis = 'Y'
            alt = ncout.createVariable('alt', np.dtype('double').char, ('alt'))
            alt.standard_name = 'altitude'
            alt.long_name = 'altitude'
            alt.units = 'meters'
            pres = ncout.createVariable('pres', np.dtype('double').char, ('pres'))
            pres.standard_name = 'pressure'
            pres.long_name = 'pressure'
            pres.units = 'hPa'
            rh = ncout.createVariable('rh', np.dtype('double').char, ('rh'))
            rh.standard_name = 'Humidity'
            rh.long_name = 'Relative Humidity'
            rh.units = '%'
            wdir = ncout.createVariable('wdir', np.dtype('double').char, ('wdir'))
            wdir.standard_name = 'Wind Direction'
            wdir.long_name = 'Wind Direction'
            wdir.units = 'degrees'
            wspd = ncout.createVariable('wspd', np.dtype('double').char, ('wspd'))
            wspd.standard_name = 'Wind Speed'
            wspd.long_name = 'Wind Speed'
            wspd.units = 'm/s'
            tdry = ncout.createVariable('tdry', np.dtype('double').char, ('tdry'))
            tdry.standard_name = 'Temperature'
            tdry.long_name = 'Dry Temperature'
            tdry.units = 'degree Celsius'
            dp = ncout.createVariable('dp', np.dtype('double').char, ('dp'))
            dp.standard_name = 'Dew Point'
            dp.long_name = 'Dew Point'
            dp.units = 'degree Celsius'
            base_time[:] = timed
            time_offset[:] = self.data_frame['TimeElapsed'].tolist()[:]
            time[:] = times[:]
            lon[:] = self.data_frame['Longitude'].tolist()[:]
            lat[:] = self.data_frame['Latitude'].tolist()[:]
            alt[:] = self.data_frame['Altitude'].tolist()[:]
            pres[:] = self.data_frame['Pressure'].tolist()[:]
            rh[:] = self.data_frame['Humidity'].tolist()[:]
            wdir[:] = self.data_frame['Wind Direction'].tolist()[:]
            wspd[:] = self.data_frame['Wind Speed'].tolist()[:]
            tdry[:] = self.data_frame['External Temperature'].tolist()[:]
            dp[:] = (self.data_frame['External Temperature'].values - (
                    (100 - self.data_frame['Humidity']) / 5)).tolist()[:]
            ncout.close()
