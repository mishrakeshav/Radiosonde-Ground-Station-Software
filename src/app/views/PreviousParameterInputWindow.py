import sys
import os
import datetime
import json

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from pyside_material import apply_stylesheet

from app.views.FlightDashboard import Dashboard
from app.utils.Alerts import Alert

try:
    PATH = sys._MEIPASS
except:
    PATH = sys.path[0]
ASSETS_DIR = os.path.join(PATH, "resources", "images", "assets")

class ParameterInputWindow(object):
    def setupUi(self,folder_path ,MainWindow, PreviousWindow):
        # Date from the port selection page
        self.folder_path = folder_path

        # to navigate between windows
        self.current_window = MainWindow
        self.previous_window = PreviousWindow
        self.next_window = None

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QSize(600, 600))
        MainWindow.setMaximumSize(QSize(600, 600))
        MainWindow.setStyleSheet(u"background-color:white;\n""")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_title_label = QLabel(self.centralwidget)
        self.main_title_label.setObjectName(u"main_title_label")
        self.main_title_label.setGeometry(QRect(0, 170, 591, 41))
        font = QFont()
        font.setFamily(u"Ubuntu Mono")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.main_title_label.setFont(font)
        self.main_title_label.setAlignment(Qt.AlignCenter)
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(0, 220, 591, 41))
        font1 = QFont()
        font1.setFamily(u"Ubuntu Mono")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.title_label.setFont(font1)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.subtitle_label = QLabel(self.centralwidget)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setGeometry(QRect(0, 270, 591, 41))
        font2 = QFont()
        font2.setFamily(u"Ubuntu Mono")
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setWeight(50)
        self.subtitle_label.setFont(font2)
        self.subtitle_label.setAlignment(Qt.AlignCenter)
        self.frequency_label = QLabel(self.centralwidget)
        self.frequency_label.setObjectName(u"frequency_label")
        self.frequency_label.setGeometry(QRect(20, 340, 151, 21))
        font3 = QFont()
        font3.setFamily(u"Ubuntu Mono")
        font3.setPointSize(14)
        self.frequency_label.setFont(font3)
        self.frequency_label.setAlignment(Qt.AlignCenter)
        self.frequency_input = QComboBox(self.centralwidget)
        self.frequency_input.addItem("")
        self.frequency_input.addItem("")
        self.frequency_input.addItem("")
        self.frequency_input.addItem("")
        self.frequency_input.addItem("")
        self.frequency_input.setObjectName(u"frequency_input")
        self.frequency_input.setGeometry(QRect(160, 340, 101, 21))
        self.temperature_label = QLabel(self.centralwidget)
        self.temperature_label.setObjectName(u"temperature_label")
        self.temperature_label.setGeometry(QRect(20, 380, 151, 21))
        self.temperature_label.setFont(font3)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.pressure_label = QLabel(self.centralwidget)
        self.pressure_label.setObjectName(u"pressure_label")
        self.pressure_label.setGeometry(QRect(20, 420, 151, 21))
        self.pressure_label.setFont(font3)
        self.pressure_label.setAlignment(Qt.AlignCenter)
        self.altitude_label = QLabel(self.centralwidget)
        self.altitude_label.setObjectName(u"altitude_label")
        self.altitude_label.setGeometry(QRect(20, 460, 151, 21))
        self.altitude_label.setFont(font3)
        self.altitude_label.setAlignment(Qt.AlignCenter)
        self.windspeed_label = QLabel(self.centralwidget)
        self.windspeed_label.setObjectName(u"windspeed_label")
        self.windspeed_label.setGeometry(QRect(300, 420, 151, 21))
        self.windspeed_label.setFont(font3)
        self.windspeed_label.setAlignment(Qt.AlignCenter)
        self.latitude_label = QLabel(self.centralwidget)
        self.latitude_label.setObjectName(u"latitude_label")
        self.latitude_label.setGeometry(QRect(300, 340, 151, 21))
        self.latitude_label.setFont(font3)
        self.latitude_label.setAlignment(Qt.AlignCenter)
        self.humidity_label = QLabel(self.centralwidget)
        self.humidity_label.setObjectName(u"humidity_label")
        self.humidity_label.setGeometry(QRect(300, 460, 151, 21))
        self.humidity_label.setFont(font3)
        self.humidity_label.setAlignment(Qt.AlignCenter)
        self.longitude_label = QLabel(self.centralwidget)
        self.longitude_label.setObjectName(u"longitude_label")
        self.longitude_label.setGeometry(QRect(300, 380, 151, 21))
        self.longitude_label.setFont(font3)
        self.longitude_label.setAlignment(Qt.AlignCenter)
        self.temperature_input = QLineEdit(self.centralwidget)
        self.temperature_input.setObjectName(u"temperature_input")
        self.temperature_input.setGeometry(QRect(160, 380, 113, 25))
        self.longitude_input = QLineEdit(self.centralwidget)
        self.longitude_input.setObjectName(u"longitude_input")
        self.longitude_input.setGeometry(QRect(430, 380, 113, 25))
        self.pressure_input = QLineEdit(self.centralwidget)
        self.pressure_input.setObjectName(u"pressure_input")
        self.pressure_input.setGeometry(QRect(160, 420, 113, 25))
        self.windspeed_input = QLineEdit(self.centralwidget)
        self.windspeed_input.setObjectName(u"windspeed_input")
        self.windspeed_input.setGeometry(QRect(430, 420, 113, 25))
        self.altitude_input = QLineEdit(self.centralwidget)
        self.altitude_input.setObjectName(u"altitude_input")
        self.altitude_input.setGeometry(QRect(160, 460, 113, 25))
        self.humidity_input = QLineEdit(self.centralwidget)
        self.humidity_input.setObjectName(u"humidity_input")
        self.humidity_input.setGeometry(QRect(430, 460, 113, 25))
        self.latitude_input = QLineEdit(self.centralwidget)
        self.latitude_input.setObjectName(u"latitude_input")
        self.latitude_input.setGeometry(QRect(430, 340, 113, 25))
        self.proceed_button = QPushButton(self.centralwidget)
        self.proceed_button.setObjectName(u"proceed_button")
        self.proceed_button.setGeometry(QRect(170, 510, 141, 31))
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(330, 510, 141, 31))
        self.logo_databyte = QLabel(self.centralwidget)
        self.logo_databyte.setObjectName(u"logo_databyte")
        self.logo_databyte.setGeometry(QRect(160, 20, 161, 141))
        self.logo_databyte.setPixmap(os.path.join(ASSETS_DIR, "logo.jpeg"))
        self.logo_databyte.setScaledContents(True)
        self.logo_somaiya = QLabel(self.centralwidget)
        self.logo_somaiya.setObjectName(u"logo_somaiya")
        self.logo_somaiya.setGeometry(QRect(330, 30, 121, 111))
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

        QMetaObject.connectSlotsByName(MainWindow)

        # custom setups
        self.connect_buttons()
        self.fill_parameters()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.main_title_label.setText(QCoreApplication.translate("MainWindow", u"Indravani Groundstation Software", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Start New Flight", None))
        self.subtitle_label.setText(QCoreApplication.translate("MainWindow", u"Enter Surface Parameters", None))
        self.frequency_label.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.frequency_input.setItemText(0, QCoreApplication.translate("MainWindow", u"600", None))
        self.frequency_input.setItemText(1, QCoreApplication.translate("MainWindow", u"601", None))
        self.frequency_input.setItemText(2, QCoreApplication.translate("MainWindow", u"602", None))
        self.frequency_input.setItemText(3, QCoreApplication.translate("MainWindow", u"603", None))
        self.frequency_input.setItemText(4, QCoreApplication.translate("MainWindow", u"604", None))

        self.temperature_label.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.pressure_label.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.altitude_label.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.windspeed_label.setText(QCoreApplication.translate("MainWindow", u"Windspeed", None))
        self.latitude_label.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.humidity_label.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.longitude_label.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.proceed_button.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.logo_databyte.setText("")
        self.logo_somaiya.setText("")

    # connects buttons to the methods that gets triggered on click
    def connect_buttons(self):
        self.proceed_button.clicked.connect(self.open_next_window)
        self.back_button.clicked.connect(self.open_previous_window)

    # fills all the QlineEdits  
    def fill_parameters(self):
        with open(os.path.join(self.folder_path , 'params.json')) as fileinput:
            self.data = json.load(fileinput) 

        # assert(type(self.data['data']['']) 
        print(self.data)
        self.set_label_text()
    
    def set_label_text(self):
        self.temperature_input.setText(str(self.data['data']['temperature']))
        self.pressure_input.setText(str(self.data['data']['pressure']))
        self.altitude_input.setText(str(self.data['data']['altitude']))
        self.windspeed_input.setText(str(self.data['data']['windspeed']))
        self.latitude_input.setText(str(self.data['data']['latitude']))
        self.humidity_input.setText(str(self.data['data']['humidity']))
        self.longitude_input.setText(str(self.data['data']['longitude']))
        self.frequency_input.setCurrentText(str(self.data['data']['frequency']))


    
    def open_next_window(self):
        if self.next_window:
            self.current_window.close()
            self.next_window.show()
        else:
            self.next_window = QMainWindow()
            self.next_window_ui = Dashboard()
            self.next_window_ui.setupUi(self.next_window, self.folder_path, self.data)
            self.next_window.show()
            self.current_window.close()

    def open_previous_window(self):
        self.current_window.close()
        self.previous_window.show()

