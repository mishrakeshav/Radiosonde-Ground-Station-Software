import os
import json

from PySide2.QtWidgets import QMainWindow

from src.app.controllers.FlightDashboardController import FlightDashboardController
from src.app.utils.Alerts import Alert
from src.app.utils.ValidateJson import validate_surface_values
from src.app.views.ParameterInputWindow import ParameterInputWindow


class PreviousParameterInputController(ParameterInputWindow):
    def __init__(self, main_window, flight_folder_path):
        self.main_window = main_window
        self.flight_folder_path = flight_folder_path
        self.setupUi(main_window=self.main_window)
        self.proceed_button.clicked.connect(self.open_next_window)
        self.back_button.clicked.connect(self.open_previous_window)
        self.fill_parameters()
        self.main_window.show()

    def open_next_window(self):
        self.main_window.close()
        self.next_window = FlightDashboardController(main_window=QMainWindow(),
                                                     flight_folder_path=self.flight_folder_path)

    def open_previous_window(self):
        from src.app.controllers.ViewPreviousFlightController import ViewPreviousFlightController
        self.next_window = ViewPreviousFlightController(self.main_window)

    def fill_parameters(self):
        file_path = os.path.join(self.flight_folder_path, 'params.json')
        try:
            with open(file_path) as file_input:
                data = json.load(file_input)
            is_valid = validate_surface_values(data)
            if not is_valid:
                raise (Exception(f"Invalid json file located at {file_path}"))
        except Exception as e:
            Alert(
                main_text="Invalid Json File",
                info_text=str(e),
                alert_type=Alert.CRITICAL
            )
            return

            # Set the text for all the QLineEdit
        self.temperature_input.setText(str(data['data']['temperature']))
        self.pressure_input.setText(str(data['data']['pressure']))
        self.altitude_input.setText(str(data['data']['altitude']))
        self.windspeed_input.setText(str(data['data']['windspeed']))
        self.latitude_input.setText(str(data['data']['latitude']))
        self.humidity_input.setText(str(data['data']['humidity']))
        self.longitude_input.setText(str(data['data']['longitude']))
        self.frequency_input.setCurrentText(str(data['data']['frequency']))
