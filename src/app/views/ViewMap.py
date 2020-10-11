import os
import sys

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtWebEngineWidgets import *
from PySide2.QtPrintSupport import *

from app.utils.MapGenerator import Map

PATH = sys.path[0]


class MapView(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MapView, self).__init__(*args, **kwargs)
        
        map_generator = Map()
        map_generator.generate_map([19.1014], [72.8581])

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl.fromLocalFile(os.path.join(PATH, "index.html")))
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapView()
    app.exec_()
