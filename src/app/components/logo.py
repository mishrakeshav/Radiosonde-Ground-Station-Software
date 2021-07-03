from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Logo:
    def __init__(self, parent, size, position, path):
        self.logo_databyte = QLabel(parent)
        self.logo_databyte.setGeometry(QRect(*position, *size))
        self.logo_databyte.setPixmap(QPixmap(path))
        self.logo_databyte.setScaledContents(True)
