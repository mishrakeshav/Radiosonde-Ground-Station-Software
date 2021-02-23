from PySide2.QtCore import *
from PySide2.QtWidgets import *

from src.app.controllers.ParameterInputController import ParameterInputController
from src.app.utils.Alerts import Alert
from src.app.views.ViewPreviousFlightWIndow import ViewPreviousFlightWindow


class ViewPreviousFlightController(ViewPreviousFlightWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUi(self.main_window)
        self.connect_buttons()

    def get_folder(self):
        print('Get Folder Called')
        self.folder_name = QFileDialog.getExistingDirectory()
        self.flight_directory_input.setText(str(self.folder_name))
        print(self.folder_name)

    def connect_buttons(self):
        self.proceed_button.clicked.connect(self.open_next_window)
        self.back_button.clicked.connect(self.open_previous_window)
        self.browse_button.clicked.connect(self.get_folder)

    def open_next_window(self):
        if not self.folder_name:
            Alert(main_text="PLS BROWSER WINDOW", info_text="Pls choose folder first lol")
            return
        else:
            self.next_window_ui = ParameterInputController(main_window=self.main_window)

    def open_previous_window(self):
        self.main_window.close()
