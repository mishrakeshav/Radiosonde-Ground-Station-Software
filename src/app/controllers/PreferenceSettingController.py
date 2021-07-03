import json

from PySide2 import QtWidgets

from src.app.components.preference_component import PreferenceComponent
from src.app.views.PreferenceSettingWindow import PreferenceSettingWindow
from src.app.utils.constants import *


def generate_preferences(parent, preferences):
    column = QtWidgets.QVBoxLayout(parent)
    column.setObjectName("column")
    components = []
    for preference in preferences:
        pref = PreferenceComponent(preference)
        components.append(pref)
        column.addLayout(pref.get_ui_component(parent))
    return components


class PreferenceSettingController(PreferenceSettingWindow):
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.setObjectName("MainWindow")
        self.setupUi(self.main_window)
        self.preferences = []
        with open(PREFERENCES_PATH) as file_inp:
            self.preferences = json.load(file_inp)
            print(self.preferences)

        self.preferences = generate_preferences(parent=self.scrollAreaWidgetContents,
                                                preferences=self.preferences)

        self.save_button.clicked.connect(self.save_preferences)
        self.reset_button.clicked.connect(self.reset_preferences)
        self.back_button.clicked.connect(self.back)

    def save_preferences(self):
        result = list(map(
            lambda preference: {
                'label': preference.get_label(),
                'default_value': preference.get_default_value(),
                'current_value': preference.get_current_value(),
                'description': preference.get_description(),
            }, self.preferences
        ))

        with open(PREFERENCES_PATH, 'w') as file_op: json.dump(result, file_op)

    def reset_preferences(self):
        for pref in self.preferences: pref.reset()

    def back(self):
        self.main_window.close()
        pass
