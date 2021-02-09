import os
import sys
import json

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from pyside_material import apply_stylesheet
from serial.tools.list_ports import comports
from app.utils.PreferenceSetter import PreferenceSetter

from app.views.ParameterInputWindow import ParameterInputWindow
from app.utils.Alerts import Alert
from app.utils.constants import * 


preference_setter = PreferenceSetter()


class PortSelectionWindow(object):
    def setupUi(self, MainWindow,PreviousWindow):
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
        self.radiosonde_port_input = QComboBox(self.centralwidget)

        self.radiosonde_port_input.setObjectName(u"radiosonde_port_input")
        self.radiosonde_port_input.setGeometry(QRect(340, 400, 141, 25))
        self.receiver_port_input = QComboBox(self.centralwidget)

        self.receiver_port_input.setObjectName(u"receiver_port_input")
        self.receiver_port_input.setGeometry(QRect(340, 350, 141, 25))
        self.receiver_port_label = QLabel(self.centralwidget)
        self.receiver_port_label.setObjectName(u"receiver_port_label")
        self.receiver_port_label.setGeometry(QRect(120, 350, 211, 21))
        font = QFont()
        font.setFamily(u"Ubuntu Mono")
        font.setPointSize(15)
        self.receiver_port_label.setFont(font)
        self.receiver_port_label.setAlignment(Qt.AlignCenter)
        self.radiosonde_port_label = QLabel(self.centralwidget)
        self.radiosonde_port_label.setObjectName(u"radiosonde_port_label")
        self.radiosonde_port_label.setGeometry(QRect(110, 400, 211, 21))
        self.radiosonde_port_label.setFont(font)
        self.radiosonde_port_label.setAlignment(Qt.AlignCenter)
        self.subtitle_label = QLabel(self.centralwidget)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setGeometry(QRect(0, 270, 591, 41))
        font1 = QFont()
        font1.setFamily(u"Ubuntu Mono")
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setWeight(50)
        self.subtitle_label.setFont(font1)
        self.subtitle_label.setAlignment(Qt.AlignCenter)
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(0, 220, 591, 41))
        font2 = QFont()
        font2.setFamily(u"Ubuntu Mono")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.title_label.setFont(font2)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_title_label = QLabel(self.centralwidget)
        self.main_title_label.setObjectName(u"main_title_label")
        self.main_title_label.setGeometry(QRect(0, 170, 591, 41))
        font3 = QFont()
        font3.setFamily(u"Ubuntu Mono")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.main_title_label.setFont(font3)
        self.main_title_label.setAlignment(Qt.AlignCenter)
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(320, 470, 141, 31))
        self.proceed_button = QPushButton(self.centralwidget)
        self.proceed_button.setObjectName(u"proceed_button")
        self.proceed_button.setGeometry(QRect(160, 470, 141, 31))
        self.logo_databyte = QLabel(self.centralwidget)
        self.logo_databyte.setObjectName(u"logo_databyte")
        self.logo_databyte.setGeometry(QRect(150, 10, 161, 141))
        self.logo_databyte.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "logo.jpeg")))
        self.logo_databyte.setScaledContents(True)
        self.logo_somaiya = QLabel(self.centralwidget)
        self.logo_somaiya.setObjectName(u"logo_somaiya")
        self.logo_somaiya.setGeometry(QRect(320, 20, 121, 111))
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


        preference_setter.set_receiver_port(self.get_comport_list(), self.receiver_port_input)
        preference_setter.set_radiosonde_port(self.get_comport_list(), self.radiosonde_port_input)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # custom setups
        self.connect_buttons()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.receiver_port_label.setText(QCoreApplication.translate("MainWindow", u"Receiver com port :", None))
        self.radiosonde_port_label.setText(QCoreApplication.translate("MainWindow", u"Radiosonde com port :", None))
        self.subtitle_label.setText(QCoreApplication.translate("MainWindow", u"Receiver com port and Radiosonde com port", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Start New Flight", None))
        self.main_title_label.setText(QCoreApplication.translate("MainWindow", u"Indravani Groundstation Software", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.proceed_button.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.logo_databyte.setText("")
        self.logo_somaiya.setText("")


    # connects buttons to methods that gets triggered on click
    def connect_buttons(self):
        self.proceed_button.clicked.connect(self.open_next_window)
        self.back_button.clicked.connect(self.open_previous_window)

    def open_previous_window(self):
        self.current_window.close()
        self.previous_window.show()

    def open_next_window(self):

        receiver_port = self.receiver_port_input.currentText()
        radiosonde_port = self.radiosonde_port_input.currentText()

        if False:
            Alert(
                main_text = "Port Selection Error",
                info_text = "The radiosonde and receiver port cannot be same",
                alert_type = Alert.WARNING,
            )
        else:
            if self.next_window:
                self.current_window.close()
                self.next_window.show()
            else:
                self.next_window = QMainWindow()
                self.next_window_ui = ParameterInputWindow()
                self.next_window_ui.setupUi(receiver_port, radiosonde_port, self.next_window,self.current_window)
                self.next_window.show()
                self.current_window.close()

    def get_comport_list(self):
        comport_list = comports()
        comport_list = list(map(lambda x: str(x).split()[0], comport_list))
        return comport_list
