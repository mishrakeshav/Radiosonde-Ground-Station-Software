import os
import sys
import io
import pandas as pd

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtWebEngineWidgets import *
from PySide2.QtPrintSupport import *

from app.utils.MapGenerator import Map


class MapView(QMainWindow):
    def __init__(self, export_path, *args, **kwargs):
        super(MapView, self).__init__(*args, **kwargs)
        self.export_path = os.path.join(export_path, 'output.csv')
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        
        df = pd.read_csv(self.export_path)
        lats = list(df['Latitude'])
        lons = list(df['Longitude'])
        self.map_generator = Map()
        self.map_generator.generate_map(lats, lons)
        self.browser.setHtml(self.map_generator.data.getvalue().decode())

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.show()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapView()
    app.exec_()
