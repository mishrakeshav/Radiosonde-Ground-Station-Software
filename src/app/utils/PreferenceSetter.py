import os
import json

PREFERENCES_PATH = os.path.join(".rsgs", "preferences.json")

class PreferenceSetter:
    def __init__(self):
        self.frequency = [400, 401, 402, 403, 404, 405, 406]
        with open(PREFERENCES_PATH, 'r') as fileinp:
            self.preferences = json.load(fileinp)

    def set_frequency_options(self, frequency_input):
        for i in self.frequency:
            frequency_input.addItem(str(i))
        frequency_input.setCurrentIndex(self.frequency.index(self.preferences['frequency']))
    
    def set_receiver_port(self, comport_list, receiver_port_input):
        receiver_port_input.addItems(comport_list)
        if self.preferences['receiver_port'] in comport_list:
            receiver_port_input.setCurrentIndex(comport_list.index(self.preferences['receiver_port']))

    def set_radiosonde_port(self, comport_list, radiosonde_port_input):
        radiosonde_port_input.addItems(comport_list)
        if self.preferences['radiosonde_port'] in comport_list:
            radiosonde_port_input.setCurrentIndex(comport_list.index(self.preferences['radiosonde_port']))
    
    def get_export_path(self):
        return self.preferences['export_path']

