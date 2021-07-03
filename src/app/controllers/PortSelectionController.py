from PySide2 import QtWidgets

from src.app.controllers.ParameterInputController import ParameterInputController
from src.app.utils.PreferenceSetter import PreferenceSetter

from src.app.utils.Alerts import Alert
from src.app.views.PortSelectionWindow import PortSelectionWindow


class PortSelectionController(PortSelectionWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUi(self.main_window)
        self.connect_buttons()
        preference_setter = PreferenceSetter()
        preference_setter.set_receiver_port(self.receiver_port_input)
        preference_setter.set_radiosonde_port(self.radiosonde_port_input)
        self.main_window.show()

    def connect_buttons(self):
        self.proceed_button.clicked.connect(self.open_next_window)
        self.back_button.clicked.connect(self.open_previous_window)

    def open_previous_window(self):
        from src.app.controllers.StartMenuController import StartMenuController
        self.previous_window = StartMenuController(self.main_window)

    def open_next_window(self):
        receiver_port = self.receiver_port_input.currentText()
        radiosonde_port = self.radiosonde_port_input.currentText()

        # TODO: test the equality of receiver and radiosonde port
        if False:
            Alert(
                main_text="Port Selection Error",
                info_text="The radiosonde and receiver port cannot be same",
                alert_type=Alert.WARNING,
            )
        else:
            self.next_window = ParameterInputController(receiver_port=receiver_port, radiosonde_port=radiosonde_port,
                                     main_window=self.main_window)
