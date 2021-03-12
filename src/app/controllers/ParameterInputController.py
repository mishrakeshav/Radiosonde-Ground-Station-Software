import os
import datetime
import json

from PySide2.QtWidgets import QMainWindow

from src.app.controllers.DashboardController import DashboardController
from src.app.utils.Alerts import Alert
from src.app.utils.PreferenceSetter import PreferenceSetter
from src.app.views.ParameterInputWindow import ParameterInputWindow


class ParameterInputController(ParameterInputWindow):
    def __init__(self, receiver_port, radiosonde_port, main_window):
        self.main_window = main_window
        self.receiver_port = receiver_port
        self.radiosonde_port = radiosonde_port
        self.setupUi(main_window=self.main_window)
        self.proceed_button.clicked.connect(self.open_next_window)
        self.back_button.clicked.connect(self.open_previous_window)
        self.main_window.show()

    def open_next_window(self):
        try:
            data = {
                "frequency": float(self.frequency_input.currentText()),
                "temperature": float(self.temperature_input.text()),
                "pressure": float(self.pressure_input.text()),
                "altitude": float(self.altitude_input.text()),
                "latitude": float(self.latitude_input.text()),
                "longitude": float(self.longitude_input.text()),
                "windspeed": float(self.windspeed_input.text()),
                "humidity": float(self.humidity_input.text()),
            }
        except :
            Alert(
                main_text="Input Error",
                info_text="Provide appropriate values",
                alert_type=Alert.CRITICAL
            )
            return

        # Make the folder structure for the new flight
        preference_setter = PreferenceSetter()
        flight_folder_name = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")  # Folder name is todays date
        flight_folder_path = os.path.join(preference_setter.get_export_path(),
                                          flight_folder_name)  # get the folder path
        os.makedirs(flight_folder_path)  # make the folder

        with open(os.path.join(flight_folder_path, "output.csv"), 'w') as file_output:  # make the files
            cols = ['time', 'latitude', 'longitude', 'satellites', 'altitude', 'pressure', 'internal_temperature',
                    'external_temperature', 'humidity', 'time_elapsed', 'wind_direction', 'wind_speed',
                    'scaled_pressure', 'scaled_temperature', 'dew_point'
                    ]
            file_output.write(",".join(cols) + "\n")

        with open(os.path.join(flight_folder_path, "params.json"), 'w') as file_output:
            json.dump({"data": data, "time": datetime.datetime.utcnow().strftime("%H:%M:%S")}, file_output)

        self.main_window.close()
        self.next_window = DashboardController(main_window=QMainWindow(), flight_folder_path=flight_folder_path,
                                               comport_name=self.receiver_port)

    def open_previous_window(self):
        print("Woop go Doop")
        self.current_window.close()
