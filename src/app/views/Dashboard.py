
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from app.utils.Canvas import MplCanvas
from app.utils.Gauge import gauge

class Dashboard(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 520)
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

        self.graph_altitude_nav = NavigationToolbar(self.graph_altitude, self.tab)
        self.graph_altitude_nav.setObjectName(u"graph_altitude_nav")
        self.graph_altitude_nav.setMinimumSize(QSize(0, 30))
        self.graph_altitude_nav.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_4.addWidget(self.graph_altitude_nav, 0, 1, 1, 1)


        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        # -----------  Gauges -----------------
        self.pressure_gauge = MplCanvas(self.tab)
        self.pressure_gauge.setObjectName(u"pressure_gauge")
        self.pressure_gauge.setMinimumSize(QSize(125, 125))
        self.pressure_gauge.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_3.addWidget(self.pressure_gauge)


        self.temperature_gauge = MplCanvas(self.tab)
        self.temperature_gauge.setObjectName(u"temperature_gauge")
        self.temperature_gauge.setMinimumSize(QSize(125, 125))
        self.temperature_gauge.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_3.addWidget(self.temperature_gauge)


        self.humidity_gauge = MplCanvas(self.tab)
        self.humidity_gauge.setObjectName(u"humidity_gauge")
        self.humidity_gauge.setMinimumSize(QSize(125, 125))
        self.humidity_gauge.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_3.addWidget(self.humidity_gauge)


        self.wind_speed_gauge = MplCanvas(self.tab)
        self.wind_speed_gauge.setObjectName(u"wind_speed_gauge")
        self.wind_speed_gauge.setMinimumSize(QSize(125, 125))
        self.wind_speed_gauge.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_3.addWidget(self.wind_speed_gauge)


        self.wind_direction_gauge = MplCanvas(self.tab)
        self.wind_direction_gauge.setObjectName(u"wind_direction_gauge")
        self.wind_direction_gauge.setMinimumSize(QSize(125, 125))
        self.wind_direction_gauge.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_3.addWidget(self.wind_direction_gauge)


        self.altitude_gauge = MplCanvas(self.tab)
        self.altitude_gauge.setObjectName(u"altitude_gauge")
        self.altitude_gauge.setMinimumSize(QSize(125, 125))
        self.altitude_gauge.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_3.addWidget(self.altitude_gauge)


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
        self.temperature_check = QCheckBox(self.layoutWidget_2)
        self.temperature_check.setObjectName(u"temperature_check")

        self.verticalLayout.addWidget(self.temperature_check)

        self.pressure_check = QCheckBox(self.layoutWidget_2)
        self.pressure_check.setObjectName(u"pressure_check")

        self.verticalLayout.addWidget(self.pressure_check)

        self.humidity_check = QCheckBox(self.layoutWidget_2)
        self.humidity_check.setObjectName(u"humidity_check")

        self.verticalLayout.addWidget(self.humidity_check)

        self.wind_speed_check = QCheckBox(self.layoutWidget_2)
        self.wind_speed_check.setObjectName(u"wind_speed_check")

        self.verticalLayout.addWidget(self.wind_speed_check)

        self.altitude_check = QCheckBox(self.layoutWidget_2)
        self.altitude_check.setObjectName(u"altitude_check")

        self.verticalLayout.addWidget(self.altitude_check)


        self.gridLayout_4.addWidget(self.parameter_group, 1, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.spec_graph = QLabel(self.tab_2)
        self.spec_graph.setObjectName(u"spec_graph")
        self.spec_graph.setMinimumSize(QSize(300, 200))
        self.spec_graph.setStyleSheet(u"background-color: blue;")

        self.gridLayout_5.addWidget(self.spec_graph, 0, 1, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 1, 2, 1, 1)

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

        self.hohograph_check = QRadioButton(self.layoutWidget)
        self.hohograph_check.setObjectName(u"hohograph_check")

        self.verticalLayout_3.addWidget(self.hohograph_check)

        self.track_check = QRadioButton(self.layoutWidget)
        self.track_check.setObjectName(u"track_check")

        self.verticalLayout_3.addWidget(self.track_check)


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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

        self.update_gauge()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.temperature_check.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.pressure_check.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.humidity_check.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.wind_speed_check.setText(QCoreApplication.translate("MainWindow", u"WindSpeed", None))
        self.altitude_check.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.spec_graph.setText(QCoreApplication.translate("MainWindow", u"Graphs", None))
        self.visualization_group.setTitle(QCoreApplication.translate("MainWindow", u"Visualization", None))
        self.skewt_check.setText(QCoreApplication.translate("MainWindow", u"Skew-T", None))
        self.tphi_check.setText(QCoreApplication.translate("MainWindow", u"T-Phi", None))
        self.hohograph_check.setText(QCoreApplication.translate("MainWindow", u"Hodograph", None))
        self.track_check.setText(QCoreApplication.translate("MainWindow", u"Ballon Track", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Time[s]", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"P[hPa]", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"T[C]", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Hu[%]", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ws[m/s]", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Wd[]", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

    def update_gauge(self):
        # will change this later
        gauge(self.temperature_gauge.axes, labels=['','','',''],
        colors=['#FFCC00','#FFCC00','#FFCC00','#FFCC00'], arrow=3,
        title=f'Temp {chr(176)}C')
        self.temperature_gauge.draw()
        gauge(self.humidity_gauge.axes, labels=['','','',''],
        colors=['#0063BF','#0063BF','#0063BF','#0063BF'], arrow=4,
        title=f'Temp {chr(176)}C')
        self.humidity_gauge.draw()
        gauge(self.wind_speed_gauge.axes, labels=['','','',''],
        colors=['#FFCC00','#FFCC00','#FFCC00','#FFCC00'], arrow=1,
        title=f'Temp {chr(176)}C')
        self.wind_speed_gauge.draw()
        gauge(self.wind_direction_gauge.axes, labels=['','','',''],
        colors=['#ED1C24','#ED1C24','#ED1C24','#ED1C24'], arrow=2,
        title=f'Temp {chr(176)}C')
        self.wind_direction_gauge.draw()
        gauge(self.altitude_gauge.axes, labels=['','','',''],
        colors=['#0063BF','#0063BF','#0063BF','#0063BF'], arrow=3,
        title=f'Temp {chr(176)}C')
        self.altitude_gauge.draw()
        gauge(self.pressure_gauge.axes, labels=['','','',''],
        colors=['#FFCC00','#FFCC00','#FFCC00','#FFCC00'], arrow=3,
        title=f'Temp {chr(176)}C')
        self.pressure_gauge.draw()


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    window = Dashboard()
    window.setupUi(MainWindow)
    MainWindow.show()

    # Execute application
    sys.exit(app.exec_())
