import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from app.views.PreviousParameterInputWindow import ParameterInputWindow
from app.utils.Alerts import Alert


ASSETS_DIR = os.path.join("resources", "images", "assets")

class ViewPreviousFlightWindow(object):
    def setupUi(self, MainWindow, PreviousWindow):

        self.folder_name = None
        # to navigate between windows 
        self.current_window = MainWindow
        self.previous_window = PreviousWindow
        self.next_window = None 

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QSize(600, 600))
        MainWindow.setMaximumSize(QSize(600, 600))
        MainWindow.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.subtitle_label = QLabel(self.centralwidget)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setGeometry(QRect(0, 270, 591, 41))
        font = QFont()
        font.setFamily(u"Ubuntu Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.subtitle_label.setFont(font)
        self.subtitle_label.setAlignment(Qt.AlignCenter)
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
        self.main_title_label = QLabel(self.centralwidget)
        self.main_title_label.setObjectName(u"main_title_label")
        self.main_title_label.setGeometry(QRect(0, 170, 591, 41))
        font2 = QFont()
        font2.setFamily(u"Ubuntu Mono")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.main_title_label.setFont(font2)
        self.main_title_label.setAlignment(Qt.AlignCenter)
        self.flight_directory_label = QLabel(self.centralwidget)
        self.flight_directory_label.setObjectName(u"flight_directory_label")
        self.flight_directory_label.setGeometry(QRect(40, 390, 151, 21))
        font3 = QFont()
        font3.setFamily(u"Ubuntu Mono")
        font3.setPointSize(14)
        self.flight_directory_label.setFont(font3)
        self.flight_directory_label.setAlignment(Qt.AlignCenter)
        self.flight_directory_input = QLineEdit(self.centralwidget)
        self.flight_directory_input.setObjectName(u"flight_directory_input")
        self.flight_directory_input.setGeometry(QRect(200, 390, 281, 31))
        self.browse_button = QPushButton(self.centralwidget)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setGeometry(QRect(480, 390, 61, 31))
        self.proceed_button = QPushButton(self.centralwidget)
        self.proceed_button.setObjectName(u"proceed_button")
        self.proceed_button.setGeometry(QRect(160, 480, 151, 41))
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(330, 480, 151, 41))
        self.logo_databyte = QLabel(self.centralwidget)
        self.logo_databyte.setObjectName(u"logo_databyte")
        self.logo_databyte.setGeometry(QRect(150, 20, 161, 141))
        self.logo_databyte.setPixmap(os.path.join(ASSETS_DIR, "logo.jpeg"))
        self.logo_databyte.setScaledContents(True)
        self.logo_somaiya = QLabel(self.centralwidget)
        self.logo_somaiya.setObjectName(u"logo_somaiya")
        self.logo_somaiya.setGeometry(QRect(320, 30, 121, 111))
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
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.subtitle_label.setText(QCoreApplication.translate("MainWindow", u"Select Flight Directory", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"View Previous Flights", None))
        self.main_title_label.setText(QCoreApplication.translate("MainWindow", u"Indravani Groundstation Software", None))
        self.flight_directory_label.setText(QCoreApplication.translate("MainWindow", u"Flight Directory", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.proceed_button.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.logo_databyte.setText("")
        self.logo_somaiya.setText("")

    def get_folder(self):
        self.folder_name = QFileDialog.getExistingDirectory()
        self.flight_directory_input.setText(str(self.folder_name))
        print(self.folder_name)
        

    def connect_buttons(self):
        self.proceed_button.clicked.connect(self.open_next_window)
        self.back_button.clicked.connect(self.open_previous_window)
        self.browse_button.clicked.connect(self.get_folder)
    
    def open_next_window(self):
        if not self.folder_name:
            Alert(main_text = "PLS BROWSER WINDOW",  info_text= "Pls choose folder first lol")
            return 
        # validation 
        if self.next_window:
            self.current_window.close()
            self.next_window.show()
        else:
            self.next_window = QMainWindow()
            self.next_window_ui = ParameterInputWindow()
            self.next_window_ui.setupUi(self.folder_name,self.next_window,self.current_window)
            self.next_window.show()
            self.current_window.close()
    
    def open_previous_window(self):
        self.current_window.close()
        self.previous_window.show()

