import sys
import os
from collections import defaultdict

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import pandas as pd
import metpy.calc as mpcalc
from metpy.plots import Hodograph, SkewT
from metpy.units import units
import numpy as np
from tephi import Tephigram
import matplotlib.pyplot as plt

from app.utils.Canvas import MplCanvas
from app.utils.ReadComPort import SerialPort
from app.utils.Worker import Worker
from app.utils.styles import *
from app.utils.Percentage import Percentage
from app.utils.MapGenerator import Map
from app.views.ViewMap import MapView

GAUGE_MINIMUM_HEIGHT = 125
GAUGE_MINIMUM_WIDTH = 125
GAUGE_MAXIMUM_HEIGHT = 250
GAUGE_MAXIMUM_WIDTH = 16777215


GAUGE_LABEL_WIDTH = 16777215
GAUGE_LABEL_HIEGHT = 30
GAUGE_PATH = os.path.join(sys.path[0], "resources", "images")


class Dashboard(object):
    def setupUi(self, MainWindow, flight_folder_path, surface_data):

        self.parameter_list = []
        self.surface_data = surface_data 
        self.flight_folder_path = flight_folder_path
        self.data_frame = pd.read_csv(
            os.path.join(self.flight_folder_path, "output.csv"))

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 520)
        self.actionTrack_Balloon = QAction(MainWindow)
        self.actionTrack_Balloon.setObjectName(u"actionTrack_Balloon")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")

        self.tab = QWidget()
        self.tab.setObjectName(u"Graph Views")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        # -----------  Graph V/s Time -----------------
        self.graph_time = MplCanvas(self.tab)
        self.graph_time.setObjectName(u"graph_time")
        self.gridLayout_4.addWidget(self.graph_time, 1, 0, 2, 1)

        self.graph_time_nav = NavigationToolbar(self.graph_time, self.tab)
        self.graph_time_nav.setObjectName(u"graph_time_nav")
        self.graph_time_nav.setMinimumSize(QSize(0, 30))
        self.graph_time_nav.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_4.addWidget(self.graph_time_nav, 0, 0, 1, 1)

        # -----------  Graph V/s Altitude -----------------
        self.graph_altitude = MplCanvas(self.tab)
        self.graph_altitude.setObjectName(u"graph_altitude")
        self.gridLayout_4.addWidget(self.graph_altitude, 1, 1, 2, 1)

        self.graph_altitude_nav = NavigationToolbar(
            self.graph_altitude, self.tab)
        self.graph_altitude_nav.setObjectName(u"graph_altitude_nav")
        self.graph_altitude_nav.setMinimumSize(QSize(0, 30))
        self.graph_altitude_nav.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_4.addWidget(self.graph_altitude_nav, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        # -----------  Gauges -----------------
        font = QFont()
        font.setFamily(u"Ubuntu Mono")
        font.setPointSize(18)
        font.setBold(True)

        self.pressure_gauge_vertical_layout = QVBoxLayout()
        self.pressure_gauge = QLabel(self.tab)
        self.pressure_gauge.setObjectName(u"pressure_gauge")
        self.pressure_gauge.setMinimumSize(
            QSize(GAUGE_MINIMUM_WIDTH, GAUGE_MINIMUM_HEIGHT))
        self.pressure_gauge.setMaximumSize(
            QSize(GAUGE_MAXIMUM_WIDTH, GAUGE_MAXIMUM_HEIGHT))
        self.pressure_gauge.setScaledContents(True)
        self.pressure_gauge_vertical_layout.addWidget(self.pressure_gauge)
        self.pressure_gauge_label = QLabel(self.tab)
        self.pressure_gauge_label.setMinimumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.pressure_gauge_label.setMaximumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.pressure_gauge_label.setFont(font)
        self.pressure_gauge_label.setAlignment(Qt.AlignCenter)
        self.pressure_gauge_vertical_layout.addWidget(
            self.pressure_gauge_label)
        self.horizontalLayout_3.addLayout(self.pressure_gauge_vertical_layout)

        self.temperature_gauge_vertical_layout = QVBoxLayout()
        self.temperature_gauge = QLabel(self.tab)
        self.temperature_gauge.setObjectName(u"temperature_gauge")
        self.temperature_gauge.setMinimumSize(
            QSize(GAUGE_MINIMUM_WIDTH, GAUGE_MINIMUM_HEIGHT))
        self.temperature_gauge.setMaximumSize(
            QSize(GAUGE_MAXIMUM_WIDTH, GAUGE_MAXIMUM_HEIGHT))
        self.temperature_gauge.setScaledContents(True)
        self.temperature_gauge_vertical_layout.addWidget(
            self.temperature_gauge)
        self.temperature_gauge_label = QLabel(self.tab)
        self.temperature_gauge_label.setMinimumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.temperature_gauge_label.setMaximumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.temperature_gauge_label.setFont(font)
        self.temperature_gauge_label.setAlignment(Qt.AlignCenter)
        self.temperature_gauge_vertical_layout.addWidget(
            self.temperature_gauge_label)
        self.horizontalLayout_3.addLayout(
            self.temperature_gauge_vertical_layout)

        self.humidity_gauge_vertical_layout = QVBoxLayout()
        self.humidity_gauge = QLabel(self.tab)
        self.humidity_gauge.setObjectName(u"humidity_gauge")
        self.humidity_gauge.setMinimumSize(
            QSize(GAUGE_MINIMUM_WIDTH, GAUGE_MINIMUM_HEIGHT))
        self.humidity_gauge.setMaximumSize(
            QSize(GAUGE_MAXIMUM_WIDTH, GAUGE_MAXIMUM_HEIGHT))
        self.humidity_gauge.setScaledContents(True)
        self.humidity_gauge_vertical_layout.addWidget(self.humidity_gauge)
        self.humidity_gauge_label = QLabel(self.tab)
        self.humidity_gauge_label.setMinimumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.humidity_gauge_label.setMaximumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.humidity_gauge_label.setFont(font)
        self.humidity_gauge_label.setAlignment(Qt.AlignCenter)
        self.humidity_gauge_vertical_layout.addWidget(
            self.humidity_gauge_label)
        self.horizontalLayout_3.addLayout(self.humidity_gauge_vertical_layout)

        self.wind_speed_gauge_vertical_layout = QVBoxLayout()
        self.wind_speed_gauge = QLabel(self.tab)
        self.wind_speed_gauge.setObjectName(u"wind_speed_gauge")
        self.wind_speed_gauge.setMinimumSize(
            QSize(GAUGE_MINIMUM_WIDTH, GAUGE_MINIMUM_HEIGHT))
        self.wind_speed_gauge.setMaximumSize(
            QSize(GAUGE_MAXIMUM_WIDTH, GAUGE_MAXIMUM_HEIGHT))
        self.wind_speed_gauge.setScaledContents(True)
        self.wind_speed_gauge_vertical_layout.addWidget(self.wind_speed_gauge)
        self.wind_speed_gauge_label = QLabel(self.tab)
        self.wind_speed_gauge_label.setMinimumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.wind_speed_gauge_label.setMaximumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.wind_speed_gauge_label.setFont(font)
        self.wind_speed_gauge_label.setAlignment(Qt.AlignCenter)
        self.wind_speed_gauge_vertical_layout.addWidget(
            self.wind_speed_gauge_label)
        self.horizontalLayout_3.addLayout(
            self.wind_speed_gauge_vertical_layout)

        self.wind_direction_gauge_vertical_layout = QVBoxLayout()
        self.wind_direction_gauge = QLabel(self.tab)
        self.wind_direction_gauge.setObjectName(u"wind_direction_gauge")
        self.wind_direction_gauge.setMinimumSize(
            QSize(GAUGE_MINIMUM_WIDTH, GAUGE_MINIMUM_HEIGHT))
        self.wind_direction_gauge.setMaximumSize(
            QSize(GAUGE_MAXIMUM_WIDTH, GAUGE_MAXIMUM_HEIGHT))
        self.wind_direction_gauge.setScaledContents(True)
        self.wind_direction_gauge_vertical_layout.addWidget(
            self.wind_direction_gauge)
        self.wind_direction_gauge_label = QLabel(self.tab)
        self.wind_direction_gauge_label.setMinimumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.wind_direction_gauge_label.setMaximumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.wind_direction_gauge_label.setFont(font)
        self.wind_direction_gauge_label.setAlignment(Qt.AlignCenter)
        self.wind_direction_gauge_vertical_layout.addWidget(
            self.wind_direction_gauge_label)
        self.horizontalLayout_3.addLayout(
            self.wind_direction_gauge_vertical_layout)

        self.altitude_gauge_vertical_layout = QVBoxLayout()
        self.altitude_gauge = QLabel(self.tab)
        self.altitude_gauge.setObjectName(u"altitude_gauge")
        self.altitude_gauge.setMinimumSize(
            QSize(GAUGE_MINIMUM_WIDTH, GAUGE_MINIMUM_HEIGHT))
        self.altitude_gauge.setMaximumSize(
            QSize(GAUGE_MAXIMUM_WIDTH, GAUGE_MAXIMUM_HEIGHT))
        self.altitude_gauge.setScaledContents(True)
        self.altitude_gauge_vertical_layout.addWidget(self.altitude_gauge)
        self.altitude_gauge_label = QLabel(self.tab)
        self.altitude_gauge_label.setMinimumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.altitude_gauge_label.setMaximumSize(
            QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HIEGHT))
        self.altitude_gauge_label.setFont(font)
        self.altitude_gauge_label.setAlignment(Qt.AlignCenter)
        self.altitude_gauge_vertical_layout.addWidget(
            self.altitude_gauge_label)
        self.horizontalLayout_3.addLayout(self.altitude_gauge_vertical_layout)

        self.gridLayout_4.addLayout(self.horizontalLayout_3, 3, 0, 1, 3)

        self.parameter_group = QGroupBox(self.tab)
        self.parameter_group.setObjectName(u"parameter_group")
        self.parameter_group.setMinimumSize(QSize(150, 230))
        self.parameter_group.setMaximumSize(QSize(150, 230))
        self.layoutWidget_2 = QWidget(self.parameter_group)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 30, 116, 176))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.temperature_color = "red"
        self.temperature_check = QCheckBox(self.layoutWidget_2)
        self.temperature_check.setObjectName(u"temperature_check")
        self.temperature_check.setChecked(True)
        self.temperature_check.setStyleSheet(temperature_checkbox_indicator)
        self.parameter_list.append(
            (self.temperature_check, "Scaled Temperature", self.temperature_color))
        self.verticalLayout.addWidget(self.temperature_check)

        self.pressure_color = "magenta"
        self.pressure_check = QCheckBox(self.layoutWidget_2)
        self.pressure_check.setObjectName(u"pressure_check")
        self.pressure_check.setStyleSheet(pressure_checkbox_indicator)
        self.parameter_list.append(
            (self.pressure_check, "Scaled Pressure", self.pressure_color))
        self.verticalLayout.addWidget(self.pressure_check)

        self.humidity_color = "blue"
        self.humidity_check = QCheckBox(self.layoutWidget_2)
        self.humidity_check.setObjectName(u"humidity_check")
        self.humidity_check.setChecked(True)
        self.humidity_check.setStyleSheet(humidity_checkbox_indicator)
        self.parameter_list.append(
            (self.humidity_check, "Humidity", self.humidity_color))
        self.verticalLayout.addWidget(self.humidity_check)

        self.wind_speed_color = "green"
        self.wind_speed_check = QCheckBox(self.layoutWidget_2)
        self.wind_speed_check.setObjectName(u"wind_speed_check")
        self.wind_speed_check.setStyleSheet(wind_speed_checkbox_indicator)
        self.parameter_list.append(
            (self.wind_speed_check, "Wind Speed", self.wind_speed_color))
        self.verticalLayout.addWidget(self.wind_speed_check)

        self.altitude_color = "yellow"
        self.altitude_check = QCheckBox(self.layoutWidget_2)
        self.altitude_check.setObjectName(u"altitude_check")
        self.altitude_check.setStyleSheet(altitude_checkbox_indicator)
        self.parameter_list.append(
            (self.altitude_check, "Altitude", self.altitude_color))
        self.verticalLayout.addWidget(self.altitude_check)

        self.gridLayout_4.addWidget(self.parameter_group, 1, 2, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.spec_graph = MplCanvas(self.tab_2)
        self.spec_graph.setObjectName(u"spec_graph")
        self.spec_graph.setMinimumSize(QSize(300, 200))

        self.gridLayout_5.addWidget(self.spec_graph, 0, 1, 2, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.spec_graph_list = {}
        self.visualization_group = QGroupBox(self.tab_2)
        self.visualization_group.setObjectName(u"visualization_group")
        self.visualization_group.setMinimumSize(QSize(100, 150))
        self.visualization_group.setMaximumSize(QSize(200, 150))
        self.layoutWidget = QWidget(self.visualization_group)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 114, 112))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.skewt_check = QRadioButton(self.layoutWidget)
        self.skewt_check.setObjectName(u"skewt_check")
        # self.skewt_check.setChecked(True)
        self.skewt_check.toggled.connect(self.onClicked)
        self.spec_graph_list["skewt"] = {
            "check": self.skewt_check, "function": self.update_skewt}
        self.verticalLayout_3.addWidget(self.skewt_check)

        self.tphi_check = QRadioButton(self.layoutWidget)
        self.tphi_check.setObjectName(u"tphi_check")
        self.tphi_check.setChecked(True)
        self.spec_graph_list["tphi"] = {
            "check": self.tphi_check, "function": self.update_tphi}
        self.verticalLayout_3.addWidget(self.tphi_check)

        self.stuve_check = QRadioButton(self.layoutWidget)
        self.stuve_check.setObjectName(u"stuve_check")
        self.spec_graph_list["stuve"] = {
            "check": self.stuve_check, "function": self.update_stuve}
        self.verticalLayout_3.addWidget(self.stuve_check)

        self.hodograph_check = QRadioButton(self.layoutWidget)
        self.hodograph_check.setObjectName(u"hodograph_check")
        self.hodograph_check.setChecked(True)
        self.spec_graph_list["hodograph"] = {
            "check": self.hodograph_check, "function": self.update_hodograph}
        self.verticalLayout_3.addWidget(self.hodograph_check)

        self.gridLayout_5.addWidget(self.visualization_group, 0, 2, 1, 1)

        self.table = QTableWidget(self.tab_2)
        if (self.table.columnCount() < 6):
            self.table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table.setObjectName(u"table")
        self.table.setMaximumSize(QSize(600, 16777215))

        self.gridLayout_5.addWidget(self.table, 0, 0, 2, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 2, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 830, 22))
        self.menuVisualization = QMenu(self.menubar)
        self.menuVisualization.setObjectName(u"menuVisualization")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuVisualization.menuAction())
        self.menuVisualization.addAction(self.actionTrack_Balloon)
        self.actionTrack_Balloon.triggered.connect(self.open_map)
        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

        self.display_graphs()
        







        
    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            
        
       






    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.actionTrack_Balloon.setText(
            QCoreApplication.translate("MainWindow", u"Track Balloon", None))
        self.temperature_check.setText(
            QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.pressure_check.setText(
            QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.humidity_check.setText(
            QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.wind_speed_check.setText(
            QCoreApplication.translate("MainWindow", u"WindSpeed", None))
        self.altitude_check.setText(
            QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.visualization_group.setTitle(
            QCoreApplication.translate("MainWindow", u"Visualization", None))
        self.skewt_check.setText(
            QCoreApplication.translate("MainWindow", u"Skew-T", None))
        self.tphi_check.setText(
            QCoreApplication.translate("MainWindow", u"T-Phi", None))
        self.hodograph_check.setText(
            QCoreApplication.translate("MainWindow", u"Hodograph", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"Time[s]", None))
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"P[hPa]", None))
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"T[C]", None))
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"Hu[%]", None))
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"Ws[m/s]", None))
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"Wd[]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuVisualization.setTitle(
            QCoreApplication.translate("MainWindow", u"Visualization", None))

    def open_map(self):
        self.map = MapView()

    def display_graphs(self):
        output_file = os.path.join(self.flight_folder_path, "output.csv")
        self.update_graph()
        self.update_spec_graphs()
        # self.update_hodograph()

        

    def update_gauge(self, pressure, temperature, humidity, wind_speed, wind_direction, altitude):
        self.pressure_gauge_label.setText(str(pressure))
        self.temperature_gauge_label.setText(str(temperature))
        self.humidity_gauge_label.setText(str(humidity))
        self.wind_speed_gauge_label.setText(str(wind_speed))
        self.wind_direction_gauge_label.setText(str(wind_direction))
        self.altitude_gauge_label.setText(str(altitude))

        pressure = Percentage.get_pressure(pressure)
        temperature = Percentage.get_temperature(temperature)
        humidity = int(humidity)
        wind_speed = Percentage.get_wind_speed(wind_speed)
        wind_direction = Percentage.get_wind_direction(wind_direction)
        altitude = Percentage.get_altitude(altitude)

        self.pressure_gauge.setPixmap(
            QPixmap(os.path.join(GAUGE_PATH, "pressure", f"{pressure}.png")))
        self.temperature_gauge.setPixmap(QPixmap(os.path.join(
            GAUGE_PATH, "temperature", f"{temperature}.png")))
        self.humidity_gauge.setPixmap(
            QPixmap(os.path.join(GAUGE_PATH, "humidity", f"{humidity}.png")))
        self.wind_speed_gauge.setPixmap(
            QPixmap(os.path.join(GAUGE_PATH, "wind_speed", f"{wind_speed}.png")))
        self.wind_direction_gauge.setPixmap(QPixmap(os.path.join(
            GAUGE_PATH, "wind_direction", f"{wind_direction}.png")))
        self.altitude_gauge.setPixmap(
            QPixmap(os.path.join(GAUGE_PATH, "altitude", f"{altitude}.png")))

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
        print(wind_speed[:5])
        u, v = mpcalc.wind_components(wind_speed, wind_dir)

        self.spec_graph.axes.cla()
        h = Hodograph(self.spec_graph.axes, component_range=.5)
        h.add_grid(increment=0.1)
        h.plot_colormapped(u, v, wind_speed)
        self.spec_graph.draw()

    def update_skewt(self):
        print("updating skewt")
        self.data_frame['Td'] = self.data_frame['External Temperature'].values - \
            ((100 - self.data_frame.Humidity)/5)
        p = self.data_frame['Pressure'].values * units.hPa
        T = self.data_frame['External Temperature'].values * units.degC
        Td = self.data_frame['Td'].values * units.degC
        wind_speed = self.data_frame['Wind Speed'].values * units.knots
        wind_dir = self.data_frame['Wind Direction'].values * units.degrees
        u, v = mpcalc.wind_components(wind_speed, wind_dir)
        skew = SkewT(self.spec_graph.fig)
        skew.plot(p, T, 'r', linewidth=2)
        skew.plot(p, Td, 'g', linewidth=2)
        skew.plot_barbs(p, u, v)
        self.spec_graph.draw()
        

    def update_tphi(self):
        print("updating tphi")
        self.data_frame['Td'] = self.data_frame['External Temperature'].values - \
            ((100 - self.data_frame.Humidity)/5)
        dewpoint = list(
            zip(self.data_frame['Pressure'], self.data_frame['Td']))
        drybulb = list(
            zip(self.data_frame['Pressure'], self.data_frame['External Temperature']))
        tephigram = Tephigram(figure=self.spec_graph.fig)
        tephigram.plot(dewpoint, label="Dew Point Temperature", color="blue")
        tephigram.plot(drybulb, label="Dry Bulb Temperature", color="red")
        self.spec_graph.draw()

    def update_stuve(self):
        print("updating stuve")
        self.data_frame['Td'] = self.data_frame['External Temperature'].values - \
            ((100 - self.data_frame.Humidity)/5)
        height_MSL_m = self.data_frame['Altitude'].tolist()
        press_mb = self.data_frame['Pressure'].tolist()
        temp_C = self.data_frame['External Temperature'].tolist()
        td_C = self.data_frame['Td'].tolist()
        wind_spd_kt = self.data_frame['Wind Speed'].tolist()
        wind_dir_deg = self.data_frame['Wind Direction'].tolist()
        x = np.arange(220, 460, 10)
        y = np.arange(100, 1026, 25)
        temp_C = [i+273.15 for i in temp_C]
        td_C = [i+273.15 for i in td_C]
        theta_2D, P_2D = np.meshgrid(x, y)
        T_2D = theta_2D*(P_2D/1000.)**0.286
        y = np.arange(40000, 102600, 2500)
        x = np.array([0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.,
                      3., 4., 6., 8., 10., 12., 16., 20.])
        labels = ['0.1', '0.2', '0.4', '0.6', '0.8', '1', '1.5',
                  '2', '3', '4', '6', '8', '10', '12', '16', '20']
        x = x/1000.
        ws_2D, Pws_2D = np.meshgrid(x, y)
        ws_T_2D = 1./(1./273.15-1.844e-4 *
                      np.log(ws_2D*Pws_2D/611.3/(ws_2D+0.622)))
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
            ws_T_2D, Pws_2D*0.01, color='#a4c2f4', linestyle='dashed')
        self.spec_graph.axes.plot(T_2D, P_2D, color='#f6b26b')
        self.spec_graph.axes.plot(temp_C, press_mb, 'r', lw=2)
        self.spec_graph.axes.plot(td_C, press_mb, 'g', lw=2)

        for i in np.arange(16):
            self.spec_graph.axes.text(
                ws_T_2D[3, i], Pws_2D[3, i]*0.01, labels[i], color='#0000f4', ha='center', weight='bold')
            self.spec_graph.axes.text(
                ws_T_2D[22, i], Pws_2D[22, i]*0.01, labels[i], color='#0000f4', ha='center', weight='bold')

        self.spec_graph.draw()
        

    def update_spec_graphs(self):
        for graph in self.spec_graph_list:
            # if graph['check'].isChecked():
                # graph["function"]()
            # if self.spec_graph_list[graph]["check"].isChecked():
            #     self.spec_graph_list[graph]["function"]()
            print(self.spec_graph_list[graph]["check"].isChecked())

    # def run_threads(self):
    #     worker1 = Worker(self.read_port)
    #     self.threadpool.start(worker1)
    
    def run_threads(self):
        worker1 = Worker(self.update_graph)
        self.threadpool.start(worker1)


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    window = Dashboard()
    window.setupUi(MainWindow)
    MainWindow.show()

    # Execute application
    sys.exit(app.exec_())
