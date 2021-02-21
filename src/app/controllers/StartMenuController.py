from src.app.controllers.PortSelectionController import PortSelectionController
from src.app.views.ViewPreviousFlightWIndow import ViewPreviousFlightWindow
from src.app.views.StartMenuWindow import StartMenuWindow
from PySide2.QtWidgets import *


class StartMenuController(StartMenuWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUi(self.main_window)
        self.connect_buttons()

    def connect_buttons(self):
        self.new_flight_button.clicked.connect(self.start_new_flight)
        self.previous_flights_button.clicked.connect(self.view_previous_flight)

    def start_new_flight(self):
        self.new_flight_window = PortSelectionController(self.main_window)

    def view_previous_flight(self):
        if self.previous_flight_window:
            self.current_window.close()
            self.previous_flight_window.show()
        else:
            self.previous_flight_window = QMainWindow()
            self.previous_flight_window_ui = ViewPreviousFlightWindow()
            self.previous_flight_window_ui.setupUi(self.previous_flight_window, self.current_window)
            self.previous_flight_window.show()
            self.current_window.close()

            # self.previous_flight_window = QMainWindow()
            # self.previous_flight_window_ui = PreferenceSetting()
            # self.previous_flight_window_ui.setupUi(self.previous_flight_window)
            # self.previous_flight_window.show()
            # self.current_window.close()
