from src.app.components.buttons import PushButton

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from src.app.utils.constants import *


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

        self.previous_flights_button = PushButton(name="Previous Flight", parent=self.centralwidget,
                                                  position=(170, 480))
        self.new_flight_button = PushButton(name="New Flight", parent=self.centralwidget, position=(170, 340))
        self.continue_flight_button = PushButton(name="Continue Flight", parent=self.centralwidget,
                                                 position=(170, 410))

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
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.main_title_label.setText(
            QCoreApplication.translate("MainWindow", u"Indravani Radiostation Software", None))
        self.logo_databyte.setText("")
        self.logo_somaiya.setText("")
