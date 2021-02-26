from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from math import ceil
from src.app.components.constants import *
from src.app.components.fonts import GaugeLabelFont


class Gauge(QtWidgets.QVBoxLayout):
    def __init__(self, parent, assets_path, minimum=0, maximum=100):
        super().__init__()

        self.assets_path = assets_path
        self.minimum = minimum
        self.maximum = maximum

        self.gauge = QtWidgets.QLabel(parent)
        self.gauge.setObjectName(u"pressure_gauge")
        self.gauge.setMinimumSize(GAUGE_MINIMUM_SIZE)
        self.gauge.setMaximumSize(GAUGE_MAXIMUM_SIZE)
        self.gauge.setScaledContents(True)
        self.addWidget(self.gauge)

        self.label = QtWidgets.QLabel(parent)
        self.label.setMinimumSize(GAUGE_LABEL_SIZE)
        self.label.setMaximumSize(GAUGE_LABEL_SIZE)
        self.label.setFont(GaugeLabelFont())
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Value")
        self.addWidget(self.label)

    def update_gauge(self, value):
        image_number = ceil(value/(self.maximum - self.minimum) * 100)
        image_number = min(max(image_number, 1), 100)
        path = os.path.join(self.assets_path, str(image_number) + ".png")
        self.gauge.setPixmap(QPixmap(path))
        self.label.setText(str(value))

