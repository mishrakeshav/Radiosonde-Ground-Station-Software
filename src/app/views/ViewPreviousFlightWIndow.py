from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from src.app.components.buttons import PushButton
from src.app.components.logo import Logo
from src.app.components.constants import *
from src.app.utils.constants import *


class ViewPreviousFlightWindow(object):
    def setupUi(self, main_window):
        self.folder_name = None
        self.current_window = main_window
        self.next_window = None

        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(600, 600)
        main_window.setMinimumSize(QSize(600, 600))
        main_window.setMaximumSize(QSize(600, 600))

        ###### Central Widget ######
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")

        ##### Subtitle  ######
        self.subtitle_label = QLabel(self.centralwidget)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setGeometry(QRect(0, 270, 591, 41))
        font = QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.subtitle_label.setFont(font)
        self.subtitle_label.setAlignment(Qt.AlignCenter)

        ###### Title ######
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(0, 220, 591, 41))
        font1 = QFont()
        font1.setFamily(FONT_NAME)
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.title_label.setFont(font1)
        self.title_label.setAlignment(Qt.AlignCenter)

        ###### Main Title #####
        self.main_title_label = QLabel(self.centralwidget)
        self.main_title_label.setObjectName(u"main_title_label")
        self.main_title_label.setGeometry(QRect(0, 170, 591, 41))
        font2 = QFont()
        font2.setFamily(FONT_NAME)
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.main_title_label.setFont(font2)
        self.main_title_label.setAlignment(Qt.AlignCenter)

        ###### Flight Directory ######
        self.flight_directory_label = QLabel(self.centralwidget)
        self.flight_directory_label.setObjectName(u"flight_directory_label")
        self.flight_directory_label.setGeometry(QRect(40, 390, 151, 21))
        font3 = QFont()
        font3.setFamily(FONT_NAME)
        font3.setPointSize(14)
        self.flight_directory_label.setFont(font3)
        self.flight_directory_label.setAlignment(Qt.AlignCenter)
        self.flight_directory_input = QLineEdit(self.centralwidget)
        self.flight_directory_input.setObjectName(u"flight_directory_input")
        self.flight_directory_input.setGeometry(QRect(200, 390, 281, 31))

        ###### Browse Button ######
        self.browse_button = PushButton(name="Browse Flight", parent=self.centralwidget,
                                        position=(480, 390,), size=(61, 31))

        ###### Proceed Button ######
        self.proceed_button = PushButton(name="Proceed", parent=self.centralwidget,
                                         position=(160, 480), size=(151, 41))

        ###### Back Button ######
        self.back_button = PushButton(name="Proceed", parent=self.centralwidget,
                                      position=(330, 480), size=(151, 41))

        self.logo_databyte = Logo(parent=self.centralwidget, position=DATABYTE_LOGO_POSITION, size=DATABYTE_LOGO_SIZE,
                                  path=DATABYTE_LOGO_PATH)

        self.logo_somaiya = Logo(parent=self.centralwidget, position=SOMAIYA_LOGO_POSITION, size=SOMAIYA_LOGO_SIZE,
                                 path=SOMAIYA_LOGO_PATH)

        main_window.setCentralWidget(self.centralwidget)

        ###### Menubar ######
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
        self.subtitle_label.setText(QCoreApplication.translate("MainWindow", u"Select Flight Directory", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"View Previous Flights", None))
        self.main_title_label.setText(
            QCoreApplication.translate("MainWindow", u"Indravani Groundstation Software", None))
        self.flight_directory_label.setText(QCoreApplication.translate("MainWindow", u"Flight Directory", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.proceed_button.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))

