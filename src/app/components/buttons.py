from src.app.components.fonts import ButtonFont
from src.app.components.constants import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class PushButton(QPushButton):
    def __init__(self, parent, name, position=(0, 0), size=STANDARD_BUTTON_SIZE, accessible_name=u"btn_outline_secondary"):
        super().__init__(parent)
        self.setObjectName(name)
        self.setGeometry(QRect(*position, *size))
        self.setFont(ButtonFont())
        self.setText(name)
        self.setAccessibleName(accessible_name)

