from src.app.components.constants import *
from PySide2.QtGui import *


class ButtonFont(QFont):
    def __init__(self):
        super().__init__()
        self.setFamily(FONT_NAME)
        self.setPointSize(20)
        self.setBold(False)
        self.setWeight(50)


class GaugeLabelFont(QFont):
    def __init__(self):
        super().__init__()
        self.setFamily(FONT_NAME)
        self.setPointSize(18)
        self.setBold(True)
