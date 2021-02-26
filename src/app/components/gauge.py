from PySide2 import QtWidgets
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QPixmap
from src.app.components.constants import *
from src.app.components.fonts import GaugeLabelFont


class Gauge(QtWidgets.QVBoxLayout):
    def __init__(self, parent):
        super().__init__()
        path = os.path.join(GAUGE_PATH, "pressure", f"1.png")
        self.gauge = QtWidgets.QLabel(parent)
        self.gauge.setObjectName(u"pressure_gauge")
        self.gauge.setMinimumSize(GAUGE_MINIMUM_SIZE)
        self.gauge.setMaximumSize(GAUGE_MAXIMUM_SIZE)
        self.gauge.setScaledContents(True)
        self.gauge.setPixmap(QPixmap(fileName=path))
        self.addWidget(self.gauge)

        self.label = QtWidgets.QLabel(parent)
        self.label.setMinimumSize(GAUGE_LABEL_SIZE)
        self.label.setMaximumSize(GAUGE_LABEL_SIZE)
        self.label.setFont(GaugeLabelFont())
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Value")
        self.addWidget(self.label)
