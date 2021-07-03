import os
import sys
import pandas as pd

from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import *

from src.app.utils.MapGenerator import Map


class MapView(QMainWindow):
    def __init__(self, export_path, *args, **kwargs):
        super(MapView, self).__init__(*args, **kwargs)
        self.export_path = os.path.join(export_path, 'output.csv')
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        df = pd.read_csv(self.export_path)
        latitude = list(df['latitude'])
        longitude = list(df['longitude'])
        self.map_generator = Map()
        self.map_generator.generate_map(latitude, longitude)
        self.browser.setHtml(self.map_generator.data.getvalue().decode())

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    path = "/home/phoenix/Desktop/Projects/Radiosonde-Ground-Station-Software/src/export/20210227_094749"
    window = MapView(export_path=path)
    app.exec_()
