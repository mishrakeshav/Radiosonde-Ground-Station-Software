import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import pandas as pd

from src.app.utils.Canvas import MplCanvas
from src.app.utils.ReadComPort import SerialPort
from src.app.utils.styles import *
from src.app.utils.constants import *



class DashboardWindow(object):
    def setupUi(self, main_window, flight_folder_path, comport_name):

        self.parameter_list = []

        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(830, 520)
        self.actionTrack_Balloon = QAction(main_window)
        self.actionTrack_Balloon.setObjectName(u"actionTrack_Balloon")

        self.actionCreate_File = QAction(main_window)
        self.actionCreate_File.setObjectName(u"actionCreate_File")

        self.centralwidget = QWidget(main_window)
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

        self.spec_graph_nav = NavigationToolbar(self.spec_graph, self.tab_2)
        self.spec_graph_nav.setObjectName(u"spec_graph_nav")
        self.spec_graph_nav.setMinimumSize(QSize(0, 200))
        self.gridLayout_5.addWidget(self.spec_graph_nav, 0, 0, 1, 1)

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
        self.skewt_check.toggled.connect(self.onClicked)
        self.skewt_check.setObjectName(u"skewt_check")
        self.skewt_check.toggled.connect(self.onClicked)
        self.spec_graph_list["skewt"] = {
            "check": self.skewt_check, "function": self.update_skewt}
        self.verticalLayout_3.addWidget(self.skewt_check)

        self.tphi_check = QRadioButton(self.layoutWidget)
        self.tphi_check.toggled.connect(self.onClicked)
        self.tphi_check.setObjectName(u"tphi_check")
        # self.tphi_check.setChecked(True)
        self.tphi_check.toggled.connect(self.onClicked)
        self.spec_graph_list["tphi"] = {
            "check": self.tphi_check, "function": self.update_tphi}
        self.verticalLayout_3.addWidget(self.tphi_check)

        self.stuve_check = QRadioButton(self.layoutWidget)
        self.stuve_check.toggled.connect(self.onClicked)
        self.stuve_check.setObjectName(u"stuve_check")
        self.stuve_check.toggled.connect(self.onClicked)
        self.spec_graph_list["stuve"] = {
            "check": self.stuve_check, "function": self.update_stuve}
        self.verticalLayout_3.addWidget(self.stuve_check)

        self.hodograph_check = QRadioButton(self.layoutWidget)
        self.hodograph_check.toggled.connect(self.onClicked)
        self.hodograph_check.setObjectName(u"hodograph_check")
        self.hodograph_check.toggled.connect(self.onClicked)
        # self.hodograph_check.setChecked(True)
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

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 830, 22))
        self.menuVisualization = QMenu(self.menubar)
        self.menuVisualization.setObjectName(u"menuVisualization")

        self.menuFiles = QMenu(self.menubar)
        self.menuFiles.setObjectName(u"menuFiles")

        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuVisualization.menuAction())
        self.menuVisualization.addAction(self.actionTrack_Balloon)
        self.actionTrack_Balloon.triggered.connect(self.open_map)

        self.menubar.addAction(self.menuFiles.menuAction())
        self.menuFiles.addAction(self.actionCreate_File)
        self.actionCreate_File.triggered.connect(self.cdf)

        self.retranslateUi(main_window)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(main_window)

        self.graph_time.show()

        self.threadpool = QThreadPool()

        self.plot_ref_time = None
        self.comport = SerialPort(comport_name)
        self.comport.initialize_port(flight_folder_path)
        self.flight_folder_path = flight_folder_path
        self.data_frame = pd.read_csv(
            os.path.join(flight_folder_path, "output.csv"))
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.table.scrollToBottom)
        self.timer.start()
        self.run_threads()

        def onClicked(self):
            radioButton = self.sender()
            # self.cdf()
            if radioButton.isChecked():
                self.update_spec_graphs()

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.update_spec_graphs()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.actionTrack_Balloon.setText(
            QCoreApplication.translate("MainWindow", u"Track Balloon", None))

        self.actionCreate_File.setText(
            QCoreApplication.translate("MainWindow", u"NetCDF", None))

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
        self.stuve_check.setText(
            QCoreApplication.translate("MainWindow", u"Stuve", None))
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
        self.menuFiles.setTitle(
            QCoreApplication.translate("MainWindow", u"Files", None))
