import json
from serial.tools.list_ports import comports

from src.app.utils.Preference import Preference
from src.app.utils.constants import *


def get_comport_list():
    comport_list = comports()
    comport_list = list(map(lambda x: str(x).split()[0], comport_list))
    return comport_list


class PreferenceSetter:
    def __init__(self):
        self.frequency = ['400', '401', '402', '403', '404', '405', '406']
        with open(PREFERENCES_PATH, 'r') as fileinp:
            preferences_data = json.load(fileinp)
            self.preferences = {}

            for pref in preferences_data:
                self.preferences[pref['label']] = Preference(
                    label=pref['label'],
                    description=pref['description'],
                    current_value=pref['current_value'],
                    default_value=pref['default_value'],
                )

    def set_frequency_options(self, frequency_input):
        for i in self.frequency:
            frequency_input.addItem(str(i))
        frequency_input.setCurrentIndex(
            self.frequency.index(self.preferences['Receiver Frequency'].get_current_value()))

    def set_receiver_port(self, receiver_port_input):
        comport_list = get_comport_list()
        receiver_port_input.addItems(comport_list)
        if self.preferences['Receiver Port'] in comport_list:
            receiver_port_input.setCurrentIndex(
                comport_list.index(self.preferences['Receiver Port'].get_current_value()))

    def set_radiosonde_port(self, radiosonde_port_input):
        comport_list = get_comport_list()
        radiosonde_port_input.addItems(comport_list)
        if self.preferences['Radiosonde Port'] in comport_list:
            radiosonde_port_input.setCurrentIndex(
                comport_list.index(self.preferences['Radiosonde Port'].get_current_value()))

    def get_export_path(self):
        return self.preferences['Export Path'].get_current_value()
