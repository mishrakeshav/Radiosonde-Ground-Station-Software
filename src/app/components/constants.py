import os
from PySide2.QtCore import QSize

# Assets Directory Path
ASSETS_DIR = os.path.join("resources", "images", "assets")
# Preferences Path
PREFERENCES_PATH = os.path.join(".rsgs", "preferences.json")


SOMAIYA_LOGO_PATH = os.path.join(ASSETS_DIR, "somaiya_logo.png")
SOMAIYA_LOGO_POSITION = (330, 30)
SOMAIYA_LOGO_SIZE = (121, 111)

DATABYTE_LOGO_PATH = os.path.join(ASSETS_DIR, "databyte_logo.jpeg")
DATABYTE_LOGO_POSITION = (160, 20)
DATABYTE_LOGO_SIZE = (161, 141)

STANDARD_BUTTON_SIZE = (271, 51)

# Fonts
FONT_NAME = u"Ubuntu Mono"

# Gauge Constants
GAUGE_PATH = os.path.join("resources", "images")

GAUGE_MINIMUM_HEIGHT = 125
GAUGE_MINIMUM_WIDTH = 125
GAUGE_MINIMUM_SIZE = QSize(GAUGE_MINIMUM_WIDTH, GAUGE_MINIMUM_HEIGHT)

GAUGE_MAXIMUM_HEIGHT = 250
GAUGE_MAXIMUM_WIDTH = 16777215
GAUGE_MAXIMUM_SIZE = QSize(GAUGE_MAXIMUM_WIDTH, GAUGE_MAXIMUM_HEIGHT)

GAUGE_LABEL_WIDTH = 16777215
GAUGE_LABEL_HEIGHT = 30
GAUGE_LABEL_SIZE = QSize(GAUGE_LABEL_WIDTH, GAUGE_LABEL_HEIGHT)

# COLORS
COLOR_TEMPERATURE = "red"
COLOR_PRESSURE = "magenta"
COLOR_HUMIDITY = "blue"
COLOR_WINDSPEED = "green"
COLOR_ALTITUDE = "orange"

# SCALING
TEMPERATURE_MAXIMUM = 60
TEMPERATURE_MINIMUM = -90

PRESSURE_MAXIMUM = 1060
PRESSURE_MINIMUM = 3

HUMIDITY_MAXIMUM = 100
HUMIDITY_MINIMUM = 0

WIND_SPEED_MAXIMUM = 180
WIND_SPEED_MINIMUM = 0

WIND_DIRECTION_MAXIMUM = 360
WIND_DIRECTION_MINIMUM = 0

ALTITUDE_MAXIMUM = 40000
ALTITUDE_MINIMUM = 0

# Serial Communication constants
BAUD_RATE = 9600
TIMEOUT = 1
