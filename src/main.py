from app.controllers.StartMenuController import StartMenuController
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

    # Execute application
    sys.exit(app.exec_())
