from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from src.app.components.buttons import PushButton
from src.app.utils.PreferenceSetter import PreferenceSetter
from src.app.components.constants import *
from src.app.components.logo import Logo

preference_setter = PreferenceSetter()


class PortSelectionWindow(object):
    def setupUi(self, MainWindow):
        self.current_window = MainWindow
        self.next_window = None

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QSize(600, 600))
        MainWindow.setMaximumSize(QSize(600, 600))
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
        self.back_button = PushButton(self.centralwidget, position=(160, 480), size=(151, 41), name="Back")
        self.proceed_button = PushButton(self.centralwidget, position=(330, 480), size=(151, 41), name="Proceed")

        self.logo_databyte = Logo(parent=self.centralwidget, position=DATABYTE_LOGO_POSITION, size=DATABYTE_LOGO_SIZE,
                                  path=DATABYTE_LOGO_PATH)

        self.logo_somaiya = Logo(parent=self.centralwidget, position=SOMAIYA_LOGO_POSITION, size=SOMAIYA_LOGO_SIZE,
                                 path=SOMAIYA_LOGO_PATH)

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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.receiver_port_label.setText(QCoreApplication.translate("MainWindow", u"Receiver com port :", None))
        self.radiosonde_port_label.setText(QCoreApplication.translate("MainWindow", u"Radiosonde com port :", None))
        self.subtitle_label.setText(
            QCoreApplication.translate("MainWindow", u"Receiver com port and Radiosonde com port", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Start New Flight", None))
        self.main_title_label.setText(
            QCoreApplication.translate("MainWindow", u"Indravani Groundstation Software", None))
