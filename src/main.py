from app.controllers.StartMenuController import StartMenuController
from app.controllers.PreferenceSettingController import PreferenceSettingController
import sys

from PySide2.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    file = open("./qss/custom.qss")
    with file:
        qss = file.read()
        app.setStyleSheet(qss)

    MainWindow = QMainWindow()
    window = StartMenuController(MainWindow)
    MainWindow.show()

    # Preference Setting
    # MainWindow = QMainWindow()
    # ui = PreferenceSettingController(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())

    # Execute application
    sys.exit(app.exec_())
