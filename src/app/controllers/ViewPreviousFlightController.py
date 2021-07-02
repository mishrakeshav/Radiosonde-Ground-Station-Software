from PySide2.QtWidgets import *

from src.app.controllers.PreviousParameterInputController import PreviousParameterInputController
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
        self.flight_folder_path = QFileDialog.getExistingDirectory()
        self.flight_directory_input.setText(str(self.flight_folder_path))

    def connect_buttons(self):
        self.proceed_button.clicked.connect(self.open_next_window)
        self.back_button.clicked.connect(self.open_previous_window)
        self.browse_button.clicked.connect(self.get_folder)

    def open_next_window(self):
        if not self.flight_folder_path:
            Alert(main_text="PLS BROWSER WINDOW", info_text="Pls choose folder first lol")
            return
        else:
            self.next_window_ui = PreviousParameterInputController(main_window=self.main_window,
                                                                   flight_folder_path=self.flight_folder_path)

    def open_previous_window(self):
        from src.app.controllers.StartMenuController import StartMenuController
        self.next_window = StartMenuController(self.main_window)
