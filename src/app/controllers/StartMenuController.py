from PySide2 import QtWidgets

from src.app.controllers.PortSelectionController import PortSelectionController
from src.app.controllers.ViewPreviousFlightController import ViewPreviousFlightController
from src.app.views.StartMenuWindow import StartMenuWindow


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
        self.next_window = ViewPreviousFlightController(self.main_window)
