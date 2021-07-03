from PySide2.QtWidgets import QMessageBox


class Alert:
    """
        Will create a Popup window to display the alert to the user

        Parameters:
            main_text -- The main title of the alert
            info_text -- Additional info given to the user on why the alert was shown
            alert_type -- The Alerts can be one of these four types
                - CRITICAL
                - WARNING
                - INFORMATION
                - QUESTION
    """

    alerts = {
        "CRITICAL": QMessageBox.Critical,
        "WARNING": QMessageBox.Warning,
        "INFORMATION": QMessageBox.Information,
        "QUESTION": QMessageBox.Question,
    }

    # Static variables
    CRITICAL = "CRITICAL"
    WARNING = "WARNING"
    INFORMATION = "INFORMATION"
    QUESTION = "QUESTION"

    def __init__(self, main_text: str, info_text="", alert_type="INFORMATION"):
        self.alert = QMessageBox()
        self.alert.setText(main_text)
        self.alert.setInformativeText(info_text)
        self.alert.setIcon(self.alerts[alert_type])

        _ = self.alert.exec_()
