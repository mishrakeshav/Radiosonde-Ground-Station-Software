import os
import json

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
        self.frequency = [400, 401, 402, 403, 404, 405, 406]
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
        frequency_input.setCurrentIndex(self.frequency.index(self.preferences['frequency'].value))

    def set_receiver_port(self, comport_list, receiver_port_input):
        receiver_port_input.addItems(comport_list)
        print(comport_list)
        if self.preferences['receiver_port'] in comport_list:
            receiver_port_input.setCurrentIndex(comport_list.index(self.preferences['receiver_port'].value))

    def set_radiosonde_port(self, comport_list, radiosonde_port_input):
        radiosonde_port_input.addItems(comport_list)
        if self.preferences['radiosonde_port'] in comport_list:
            radiosonde_port_input.setCurrentIndex(comport_list.index(self.preferences['radiosonde_port'].value))

    def get_export_path(self):
        return self.preferences['export_path'].value

    def save_perferences(self):
        result = {"preference_list": self.preference_list}
        result['data'] = []
        
        for pref in self.preference_list:
            result['data'].append(self.preferences[pref].getDict())

        with open(PREFERENCES_PATH, 'w') as file: json.dump(result, file)
        print("Preferences updated !")

