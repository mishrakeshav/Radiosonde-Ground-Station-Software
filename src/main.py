# standard library imports
import sys 

# third party library imports 
from PySide2.QtWidgets import *

# local imports 
from app.views.StartMenuWindow import StartMenuWindow
from app.utils.PreferenceSetter import PreferenceSetter
if __name__ == "__main__":
    # Qt Application
    prefernce_setter = PreferenceSetter()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    file = open("./qss/custom.qss")
    with file:
        qss = file.read()
        app.setStyleSheet(qss)
    # QMainWindow using QWidget as central widget
    window = StartMenuWindow()
    window.setupUi(MainWindow)
    MainWindow.show()

    # Execute application
    sys.exit(app.exec_())
