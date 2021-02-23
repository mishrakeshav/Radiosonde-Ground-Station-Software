import serial
import os
import json
import datetime

from app.utils.Alerts import Alert
from app.utils.Wind import Wind


class SerialPort:

    def __init__(self, comport: str, baudrate: int = 9600, timeout: int = 1):
        self.MAXIMUM_PRESSURE = 1100
        self.MINIMUM_PRESSURE = 3

        self.MAXIMUM_TEMPERATURE = 60
        self.MINIMUM_TEMPERATURE = -90
        self.serial_port = serial.Serial(port=comport, baudrate=baudrate, timeout=timeout)

    def initialize_parameters(self, flight_file_path):
        path = os.path.join(flight_file_path, 'params.json')
        with open(path) as json_file:
            flight_data = json.load(json_file)
            self.previous_latitude = flight_data["data"]["latitude"]
            self.previous_longitude = flight_data["data"]["longitude"]
            self.previous_time = 0
            self.flight_init_time = None

    def get_wind_direction(self, latitude, longitude):
        return Wind.calculate_wind_direction(
            self.previous_latitude,
            self.previous_longitude,
            latitude,
            longitude
        )

    def get_wind_speed(self, latitude, longitude, time_elapsed):
        return Wind.calculate_wind_speed(
            self.previous_latitude,
            self.previous_longitude,
            latitude,
            longitude,
            self.previous_time,
            time_elapsed
        )

    def get_time_elapsed(self, time_):
        hour, mins, secs = int(time_[:2]), int(time_[2:4]), int(time_[4:])
        current_time = datetime.time(hour, mins, secs)
        current_time_second = current_time.hour * 60 * 60 + current_time.minute * 60 + current_time.second
        if not self.flight_init_time:
            self.flight_init_time = current_time_second
        return current_time_second - self.flight_init_time

    def initialize_port(self, flight_file_path):
        output_file = os.path.join(flight_file_path, 'output.csv')
        if not os.path.exists(output_file):
            Alert(
                main_text="File Not Found",
                info_text=f"File not found at {flight_file_path}",
                alert_type=Alert.CRITICAL
            )
            return

        self.initialize_parameters(flight_file_path)


if __name__ == '__main__':
    from serial.tools.list_ports import comports

    ports_avail = comports()
    for i, port in enumerate(ports_avail):
        print(i, str(port))
    index = int(input())

    serial_port = SerialPort(
        str(ports_avail[index]).split()[0]
    )

    flight_file_path = "/home/phoenix/Desktop/Projects/Radiosonde-Ground-Station-Software/src/export/sample"
    serial_port.read_port(flight_file_path)
