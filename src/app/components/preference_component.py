from PySide2 import QtWidgets, QtCore

from src.app.utils.Preference import Preference


class PreferenceComponent(Preference):
    def __init__(self, preference):
        super().__init__(
            label=preference['label'],
            default_value=preference['default_value'],
            current_value=preference['current_value'],
            description=preference['description'],
        )

    def get_ui_component(self, parent):
        column = QtWidgets.QVBoxLayout()
        column.setObjectName(f"column_{self.get_label()}")

        row = QtWidgets.QHBoxLayout()
        row.setObjectName(f"row_{self.get_label()}")

        self.preference_label = QtWidgets.QLabel(parent)
        self.preference_label.setMinimumSize(QtCore.QSize(200, 25))
        self.preference_label.setMaximumSize(QtCore.QSize(200, 25))
        self.preference_label.setObjectName(f"preference_label_{self.get_label()}")
        self.preference_label.setText(self.get_label())
        row.addWidget(self.preference_label)

        self.preference_value = QtWidgets.QLineEdit(parent)
        self.preference_value.setMinimumSize(QtCore.QSize(200, 25))
        self.preference_value.setMaximumSize(QtCore.QSize(200, 25))
        self.preference_value.setObjectName(f"preference_value_{self.get_label()}")
        self.preference_value.setText(self.get_current_value())
        self.preference_value.textChanged.connect(lambda: self.set_current_value(self.preference_value.text()))

        row.addWidget(self.preference_value)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        row.addItem(spacerItem)
        column.addLayout(row)

        self.preference_description = QtWidgets.QLabel(parent)
        self.preference_description.setText(self.get_description())
        column.addWidget(self.preference_description)

        return column

    def reset(self):
        self.reset_value()
        self.preference_value.setText(self.get_current_value())
