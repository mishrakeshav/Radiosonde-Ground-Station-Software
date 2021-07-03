from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from src.app.components.buttons import PushButton
from src.app.utils.PreferenceSetter import PreferenceSetter
from src.app.components.logo import Logo
from src.app.components.constants import *

preference_setter = PreferenceSetter()


class ParameterInputWindow(object):
    def setupUi(self, main_window):
        self.frequency = [400, 401, 402, 403, 404, 405, 406]

        self.current_window = main_window
        self.next_window = None

        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(600, 600)
        main_window.setMinimumSize(QSize(600, 600))
        main_window.setMaximumSize(QSize(600, 600))
        self.centralwidget = QWidget(main_window)
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

        self.proceed_button = PushButton(parent=self.centralwidget, name="Proceed", position=(170, 510), size=(141, 31))

        self.back_button = PushButton(parent=self.centralwidget, name="Proceed", position=(330, 510), size=(141, 31))

        self.logo_databyte = Logo(parent=self.centralwidget, position=DATABYTE_LOGO_POSITION, size=DATABYTE_LOGO_SIZE,
                                  path=DATABYTE_LOGO_PATH)

        self.logo_somaiya = Logo(parent=self.centralwidget, position=SOMAIYA_LOGO_POSITION, size=SOMAIYA_LOGO_SIZE,
                                 path=SOMAIYA_LOGO_PATH)
        
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 20))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.main_title_label.setText(
            QCoreApplication.translate("MainWindow", u"Indravani Groundstation Software", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Start New Flight", None))
        self.subtitle_label.setText(QCoreApplication.translate("MainWindow", u"Enter Surface Parameters", None))
        self.frequency_label.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))

        preference_setter.set_frequency_options(self.frequency_input)

        self.temperature_label.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.pressure_label.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.altitude_label.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.windspeed_label.setText(QCoreApplication.translate("MainWindow", u"Windspeed", None))
        self.latitude_label.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.humidity_label.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.longitude_label.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.proceed_button.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))

