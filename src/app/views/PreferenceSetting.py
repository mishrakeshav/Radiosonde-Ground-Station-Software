from typing import Container
from PySide2 import QtCore, QtGui, QtWidgets
from app.utils.PreferenceSetter import PreferenceSetter

class PreferenceSetting(object):
    def __init__(self):
        self.preference_setter = PreferenceSetter()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(500, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 778, 540))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.make_preferences_ui()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setObjectName("back_button")
        self.horizontalLayout.addWidget(self.back_button)
        
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(self.save_preferences)
        self.horizontalLayout.addWidget(self.save_button)
        
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setObjectName("reset_button")
        self.reset_button.clicked.connect(self.reset_to_defaults)
        self.horizontalLayout.addWidget(self.reset_button)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.reset_button.setText(_translate("MainWindow", "Reset to defaults"))
    

    def make_preferences_ui(self):
        self.preference_input = {}
        for pref in self.preference_setter.preferences.values():

            container = QtWidgets.QWidget()
            container.setStyleSheet("background-color:lightgrey;")

            verticalLayout = QtWidgets.QVBoxLayout(container)
            horizontalLayout = QtWidgets.QHBoxLayout()

            preference_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            preference_label.setMinimumSize(QtCore.QSize(200, 25))
            preference_label.setMaximumSize(QtCore.QSize(200, 25))
            horizontalLayout.addWidget(preference_label)

            preference_value = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            preference_value.setMinimumSize(QtCore.QSize(200, 25))
            preference_value.setMaximumSize(QtCore.QSize(200, 25))
            horizontalLayout.addWidget(preference_value)

            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            horizontalLayout.addItem(spacerItem)

            verticalLayout.addLayout(horizontalLayout)

            preference_description = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            
            preference_label.setText(f"{pref.name }")
            preference_value.setText(f"{ pref.value }")
            preference_description.setText(f"{ pref.description }")

            verticalLayout.addWidget(preference_description)

            self.preference_input[pref.name] = preference_value
            self.verticalLayout.addWidget(container)

        spacerItem1 = QtWidgets.QSpacerItem(20, 139, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
    
    def update_preference_inputs(self):
        for pref_name, pref_input in self.preference_input.items():
            pref_input.setText(self.preference_setter.preferences[pref_name].value)

    def update_preference_values(self):
        for pref_name, pref_input in self.preference_input.items():
            self.preference_setter.preferences[pref_name].value = pref_input.text()

    def reset_to_defaults(self):
        self.preference_setter.set_defaults()
        self.update_preference_inputs()

    def save_preferences(self):
        self.update_preference_values()
        self.preference_setter.save_perferences()

    def back(self):
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PreferenceSetting()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
