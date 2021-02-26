from PySide2.QtWidgets import *

from src.app.views.FlightDashboardWindow import FlightDashboardWindow
from src.app.views.ViewMap import MapView
import metpy.calc as mpcalc
from metpy.plots import Hodograph, SkewT
from metpy.units import units
import numpy as np
import pandas as pd
from tephi import Tephigram
import netCDF4 as nc
from datetime import datetime


class FlightDashboardController(FlightDashboardWindow):
    def __init__(self, main_window, flight_folder_path):
        self.main_window = main_window
        self.flight_folder_path = flight_folder_path
        self.setupUi(main_window=main_window)

    def open_map(self):
        self.map = MapView(self.flight_folder_path)

    def update_table(self, data):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for i in range(len(data)):
            self.table.setItem(row, i, QTableWidgetItem(str(data[i])))
        self.table.scrollToBottom()

    def update_graph(self):
        self.graph_time.axes.cla()
        for parameter_check, parameter_name, color in self.parameter_list:
            if parameter_check.isChecked():
                self.graph_time.axes.plot(
                    self.data_frame[parameter_name], self.data_frame["TimeElapsed"], color=color)
        self.graph_time.axes.grid()
        self.graph_time.axes.set_xlabel('Time Elapsed (s)')
        self.graph_time.draw()

        self.graph_altitude.axes.cla()
        for parameter_check, parameter_name, color in self.parameter_list:
            if parameter_name == "Altitude":
                continue
            if parameter_check.isChecked():
                self.graph_altitude.axes.plot(
                    self.data_frame[parameter_name], self.data_frame["Altitude"], color=color)
        self.graph_altitude.axes.grid()
        self.graph_altitude.axes.set_xlabel('Time Elapsed (s)')
        self.graph_altitude.draw()

    def update_hodograph(self):
        print("updating hodograph")
        wind_speed = np.array(
            list(map(float, self.data_frame['Wind Speed'].values))) * units.knots
        wind_dir = np.array(
            list(map(float, self.data_frame['Wind Direction'].values))) * units.degrees
        u, v = mpcalc.wind_components(wind_speed, wind_dir)

        # self.spec_graph.axes.cla()
        self.spec_graph.fig.clf()
        h = Hodograph(self.spec_graph.axes, component_range=.5)
        h.add_grid(increment=0.1)
        h.plot_colormapped(u, v, wind_speed)
        self.spec_graph.draw()

    def update_skewt(self):
        print("updating skewt")
        self.data_frame['Td'] = self.data_frame['External Temperature'].values - \
                                ((100 - self.data_frame.Humidity) / 5)
        p = self.data_frame['Pressure'].values * units.hPa
        T = self.data_frame['External Temperature'].values * units.degC
        Td = self.data_frame['Td'].values * units.degC
        wind_speed = self.data_frame['Wind Speed'].values * units.knots
        wind_dir = self.data_frame['Wind Direction'].values * units.degrees
        u, v = mpcalc.wind_components(wind_speed, wind_dir)

        self.spec_graph.fig.clf()

        skew = SkewT(self.spec_graph.fig)
        skew.plot(p, T, 'r', linewidth=2)
        skew.plot(p, Td, 'g', linewidth=2)
        skew.plot_barbs(p, u, v)
        self.spec_graph.draw()

    def update_tphi(self):
        print("updating tphi")
        self.data_frame['Td'] = self.data_frame['External Temperature'].values - \
                                ((100 - self.data_frame.Humidity) / 5)
        dewpoint = list(
            zip(self.data_frame['Pressure'], self.data_frame['Td']))
        drybulb = list(
            zip(self.data_frame['Pressure'], self.data_frame['External Temperature']))

        self.spec_graph.fig.clf()

        tephigram = Tephigram(figure=self.spec_graph.fig)
        tephigram.plot(dewpoint, label="Dew Point Temperature", color="blue")
        tephigram.plot(drybulb, label="Dry Bulb Temperature", color="red")
        self.spec_graph.draw()

    def update_stuve(self):
        print("updating stuve")
        self.data_frame['Td'] = self.data_frame['External Temperature'].values - \
                                ((100 - self.data_frame.Humidity) / 5)
        height_MSL_m = self.data_frame['Altitude'].tolist()
        press_mb = self.data_frame['Pressure'].tolist()
        temp_C = self.data_frame['External Temperature'].tolist()
        td_C = self.data_frame['Td'].tolist()
        wind_spd_kt = self.data_frame['Wind Speed'].tolist()
        wind_dir_deg = self.data_frame['Wind Direction'].tolist()
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

        self.spec_graph.fig.clf()

        self.spec_graph.axes.set_yscale('log')
        self.spec_graph.axes.set_xlabel('temp K')
        self.spec_graph.axes.set_ylabel('pressure mb')
        self.spec_graph.axes.set_title('Stuve chart')
        self.spec_graph.axes.set_xlim(200, 300)
        self.spec_graph.axes.set_ylim(1025, 400)
        self.spec_graph.axes.minorticks_off()
        self.spec_graph.axes.set_xticks(np.arange(200, 301, 10))
        self.spec_graph.axes.set_yticks([1000, 850, 700, 600, 500, 400])
        self.spec_graph.axes.set_yticklabels(
            ['1000', '850', '700', '600', '500', '400'])
        self.spec_graph.axes.grid(True)
        self.spec_graph.axes.plot(
            ws_T_2D, Pws_2D * 0.01, color='#a4c2f4', linestyle='dashed')
        self.spec_graph.axes.plot(T_2D, P_2D, color='#f6b26b')
        self.spec_graph.axes.plot(temp_C, press_mb, 'r', lw=2)
        self.spec_graph.axes.plot(td_C, press_mb, 'g', lw=2)

        for i in np.arange(16):
            self.spec_graph.axes.text(
                ws_T_2D[3, i], Pws_2D[3, i] * 0.01, labels[i], color='#0000f4', ha='center', weight='bold')
            self.spec_graph.axes.text(
                ws_T_2D[22, i], Pws_2D[22, i] * 0.01, labels[i], color='#0000f4', ha='center', weight='bold')

        self.spec_graph.draw()

    def update_spec_graphs(self):
        # self.spec_graph.axes.cla()
        for graph in self.spec_graph_list:
            if self.spec_graph_list[graph]["check"].isChecked():
                self.spec_graph_list[graph]["function"]()

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
