from app.views.PreferenceSetting import PreferenceSetting
import sys
import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from pyside_material import apply_stylesheet

from app.views.PortSelectionWindow import PortSelectionWindow
from app.views.ViewPreviousFlightWIndow import ViewPreviousFlightWindow
from app.views.PreferenceSetting import PreferenceSetting



ASSETS_DIR = os.path.join("resources", "images", "assets")
FONT_NAME = u"MS Shell Dlg 2"

class StartMenuWindow(object):
    def setupUi(self, MainWindow):
        # to navigate between windows
        self.current_window = MainWindow
        self.new_flight_window = None 
        self.previous_flight_window = None 

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QSize(600, 600))
        MainWindow.setMaximumSize(QSize(600, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_title_label = QLabel(self.centralwidget)
        self.main_title_label.setObjectName(u"main_title_label")
        self.main_title_label.setGeometry(QRect(40, 180, 551, 81))
        font = QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.main_title_label.setFont(font)
        self.main_title_label.setAlignment(Qt.AlignCenter)
        self.previous_flights_button = QPushButton(self.centralwidget)
        self.previous_flights_button.setObjectName(u"previous_flights_button")
        self.previous_flights_button.setGeometry(QRect(170, 480, 271, 51))
        font1 = QFont()
        font1.setFamily(FONT_NAME)
        font1.setPointSize(17)
        font1.setBold(False)
        font1.setWeight(50)
        self.previous_flights_button.setFont(font1)
        self.new_flight_button = QPushButton(self.centralwidget)
        self.new_flight_button.setObjectName(u"new_flight_button")
        self.new_flight_button.setGeometry(QRect(170, 340, 271, 51))
        self.new_flight_button.setFont(font1)
        self.continue_flight_button = QPushButton(self.centralwidget)
        self.continue_flight_button.setObjectName(u"continue_flight_button")
        self.continue_flight_button.setGeometry(QRect(170, 410, 271, 51))
        self.continue_flight_button.setFont(font1)
        self.logo_databyte = QLabel(self.centralwidget)
        self.logo_databyte.setObjectName(u"logo_databyte")
        self.logo_databyte.setGeometry(QRect(160, 30, 161, 141))
        self.logo_databyte.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "logo.jpeg")))
        self.logo_databyte.setScaledContents(True)
        self.logo_somaiya = QLabel(self.centralwidget)
        self.logo_somaiya.setObjectName(u"logo_somaiya")
        self.logo_somaiya.setGeometry(QRect(330, 40, 121, 111))
        self.logo_somaiya.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "svv.png")))
        self.logo_somaiya.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.set_accesible_name()
        QMetaObject.connectSlotsByName(MainWindow)

        # custom setups 
        self.connect_buttons()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.main_title_label.setText(QCoreApplication.translate("MainWindow", u"Indravani Radiostation Software", None))
        self.previous_flights_button.setText(QCoreApplication.translate("MainWindow", u"View Previous Flight", None))
        self.new_flight_button.setText(QCoreApplication.translate("MainWindow", u"Start New Flight", None))
        self.continue_flight_button.setText(QCoreApplication.translate("MainWindow", u"Continue Flight", None))
        self.logo_databyte.setText("")
        self.logo_somaiya.setText("")

    def set_accesible_name(self):
        self.new_flight_button.setAccessibleName(QCoreApplication.translate("MainWindow", u"btn_outline_secondary", None))
        self.continue_flight_button.setAccessibleName(QCoreApplication.translate("MainWindow", u"btn_outline_danger", None))
        self.previous_flights_button.setAccessibleName(QCoreApplication.translate("MainWindow", u"btn_secondary",None))

    def connect_buttons(self):
        self.new_flight_button.clicked.connect(self.start_new_flight)
        self.previous_flights_button.clicked.connect(self.view_previous_flight)

    def start_new_flight(self):
        # if next window object is already created
        if self.new_flight_window:
            self.current_window.close()
            self.new_flight_window.show()
        else:
            self.new_flight_window = QMainWindow()
            self.new_flight_window_ui = PortSelectionWindow()
            self.new_flight_window_ui.setupUi(self.new_flight_window,self.current_window)
            self.new_flight_window.show()
            self.current_window.close()
    
    def view_previous_flight(self):
        if self.previous_flight_window:
            self.current_window.close()
            self.previous_flight_window.show()
        else:
            # self.previous_flight_window = QMainWindow()
            # self.previous_flight_window_ui = ViewPreviousFlightWindow()
            # self.previous_flight_window_ui.setupUi(self.previous_flight_window,self.current_window)
            # self.previous_flight_window.show()
            # self.current_window.close()

            self.previous_flight_window = QMainWindow()
            self.previous_flight_window_ui = PreferenceSetting()
            self.previous_flight_window_ui.setupUi(self.previous_flight_window)
            self.previous_flight_window.show()
            self.current_window.close()
