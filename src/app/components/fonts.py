from src.app.utils.constants import *
from PySide2.QtGui import *


class ButtonFont(QFont):
    def __init__(self):
        super().__init__()
        self.setFamily(FONT_NAME)
        self.setPointSize(17)
        self.setBold(False)
        self.setWeight(50)
