from app.components.fonts import ButtonFont
from .constants import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class StartMenuButton(QPushButton):
    def __init__(self, parent, name, position):
        super().__init__(parent)
        self.setObjectName(name)
        self.setGeometry(QRect(*position, *START_MENU_BUTTON_SIZE))
        self.setFont(ButtonFont())
        self.setText(name)