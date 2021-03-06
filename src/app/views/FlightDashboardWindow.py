from PySide2.QtCore import *
from PySide2.QtWidgets import *

from src.app.components.canvas import Canvas
from src.app.utils.styles import *
from src.app.components.constants import *


class FlightDashboardWindow(object):
    def setupUi(self, main_window):

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

        # --------------------------- TAB 1 Contents ---------------------------
        self.tab = QWidget()
        self.tab.setObjectName(u"Graph Views")

        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        # -----------  Graph V/s Time -----------------
        self.graph_time = Canvas(parent=self.tab)
        self.graph_time.set_xlabel("Time Elapsed(s)")
        self.graph_time.set_ylabel("Atmospheric Parameters")
        self.graph_time.set_title("Parameters V/S Time Elapsed")
        self.gridLayout_4.addLayout(self.graph_time, 0, 0, 1, 1)

        # -----------  Graph V/s Altitude -----------------
        self.graph_altitude = Canvas(parent=self.tab)
        self.graph_time.set_xlabel("Atmospheric Parameters")
        self.graph_time.set_ylabel("Altitude")
        self.graph_time.set_title("Parameters V/S Altitude")
        self.gridLayout_4.addLayout(self.graph_altitude, 0, 1, 1, 1)

        # Graph Index
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

        self.temperature_check = QCheckBox(self.layoutWidget_2)
        self.temperature_check.setChecked(True)
        self.temperature_check.setStyleSheet(temperature_checkbox_indicator)
        self.verticalLayout.addWidget(self.temperature_check)

        self.pressure_check = QCheckBox(self.layoutWidget_2)
        self.pressure_check.setStyleSheet(pressure_checkbox_indicator)
        self.verticalLayout.addWidget(self.pressure_check)

        self.humidity_check = QCheckBox(self.layoutWidget_2)
        self.humidity_check.setChecked(True)
        self.humidity_check.setStyleSheet(humidity_checkbox_indicator)
        self.verticalLayout.addWidget(self.humidity_check)

        self.wind_speed_check = QCheckBox(self.layoutWidget_2)
        self.wind_speed_check.setStyleSheet(wind_speed_checkbox_indicator)
        self.verticalLayout.addWidget(self.wind_speed_check)

        self.altitude_check = QCheckBox(self.layoutWidget_2)
        self.altitude_check.setStyleSheet(altitude_checkbox_indicator)
        self.verticalLayout.addWidget(self.altitude_check)

        self.gridLayout_4.addWidget(self.parameter_group, 0, 2, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        # ----------------------- END TAB 1 Contents ---------------------------

        self.tabWidget.addTab(self.tab, "")

        # --------------------------- TAB 2 Contents ---------------------------
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

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
        self.gridLayout_5.addWidget(self.table, 0, 0, 1, 1)

        self.spec_graph = Canvas(parent=self.tab_2)
        self.gridLayout_5.addLayout(self.spec_graph, 0, 1, 1, 1)

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
        self.verticalLayout_3.addWidget(self.skewt_check)

        self.tphi_check = QRadioButton(self.layoutWidget)
        self.tphi_check.setObjectName(u"tphi_check")
        self.verticalLayout_3.addWidget(self.tphi_check)

        self.stuve_check = QRadioButton(self.layoutWidget)
        self.stuve_check.setObjectName(u"stuve_check")
        self.verticalLayout_3.addWidget(self.stuve_check)

        self.hodograph_check = QRadioButton(self.layoutWidget)
        self.hodograph_check.setObjectName(u"hodograph_check")
        self.verticalLayout_3.addWidget(self.hodograph_check)

        self.gridLayout_5.addWidget(self.visualization_group, 0, 2, 1, 1)
        # ----------------------- END TAB 2 Contents ---------------------------

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

        self.menubar.addAction(self.menuFiles.menuAction())
        self.menuFiles.addAction(self.actionCreate_File)

        self.retranslateUi(main_window)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(main_window)
        main_window.show()

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
        self.parameter_group.setTitle(
            QCoreApplication.translate("MainWindow", u"Parameters", None))
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
