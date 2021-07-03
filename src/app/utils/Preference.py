class Preference:
    def __init__(self, label: str, default_value: str, description: str, current_value: str):
        self._label = label
        self._default_value = default_value
        self._current_value = current_value
        self._description = description

    def get_label(self): return self._label

    def get_default_value(self): return self._default_value

    def get_current_value(self): return self._current_value

    def get_description(self): return self._description

    def set_current_value(self, val): self._current_value = val

    def reset_value(self): self._current_value = self._default_value
