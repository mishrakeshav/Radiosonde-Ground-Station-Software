import os
import json
from serial.tools.list_ports import comports

PREFERENCES_PATH = os.path.join(".rsgs", "preferences.json")


class Preference:
    def __init__(self, name, description, value, default_value):
        self.name = name
        self.description = description
        self.value = value
        self.default_value = default_value

    def getDict(self):
        return {
            "name": self.name,
            "description": self.description,
            "value": self.value,
            "default_value": self.default_value,
        }


class PreferenceSetter:
    def __init__(self):
        self.frequency = ['400', '401', '402', '403', '404', '405', '406']
        with open(PREFERENCES_PATH, 'r') as fileinp:
            preferences_data = json.load(fileinp)

            self.preference_list = preferences_data['preference_list']

            self.preferences = {}
            for pref in preferences_data['data']:
                self.preferences[pref['name']] = Preference(
                    name=pref['name'],
                    description=pref['description'],
                    value=pref['value'],
                    default_value=pref['default_value'],
                )

            for i in self.preferences.values(): print(i)

    def set_frequency_options(self, frequency_input):
        for i in self.frequency:
            frequency_input.addItem(str(i))
        frequency_input.setCurrentIndex(self.frequency.index(self.preferences['Receiver Frequency'].value))

    def set_receiver_port(self, receiver_port_input):
        comport_list = self.get_comport_list()
        receiver_port_input.addItems(comport_list)
        if self.preferences['Receiver Port'] in comport_list:
            receiver_port_input.setCurrentIndex(comport_list.index(self.preferences['receiver_port'].value))

    def set_radiosonde_port(self, radiosonde_port_input):
        comport_list = self.get_comport_list()
        radiosonde_port_input.addItems(comport_list)
        if self.preferences['Radiosonde Port'] in comport_list:
            radiosonde_port_input.setCurrentIndex(comport_list.index(self.preferences['radiosonde_port'].value))

    def get_export_path(self):
        return self.preferences['Export Path'].value

    def set_defaults(self):
        for pref in self.preferences.values():
            pref.value = pref.default_value
        self.save_perferences()

    def save_perferences(self):
        result = {"preference_list": self.preference_list}
        result['data'] = []

        for pref in self.preference_list:
            result['data'].append(self.preferences[pref].getDict())

        with open(PREFERENCES_PATH, 'w') as file: json.dump(result, file)
        print("Preferences updated !")

    def get_comport_list(self):
        comport_list = comports()
        comport_list = list(map(lambda x: str(x).split()[0], comport_list))
        return comport_list
