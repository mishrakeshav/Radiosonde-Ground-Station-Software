from PySide2 import QtWidgets

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)


class Canvas(QtWidgets.QVBoxLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.graph = MplCanvas()
        self.graph.setObjectName("graph")

        self.nav_bar = NavigationToolbar(self.graph, parent)
        self.nav_bar.setObjectName("nav_bar")
        self.addWidget(self.nav_bar)

        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.addItem(spacerItem)
        self.addWidget(self.graph)

        self.setStretch(0, 10)
        self.setStretch(2, 90)
    
    def clear_canvas(self): self.graph.axes.cla()
    
    def set_xlabel(self, xlabel): self.graph.axes.set_xlabel(xlabel)
    
    def set_ylabel(self, ylabel): self.graph.axes.set_ylabel(ylabel)
    
    def set_title(self, title): self.graph.axes.set_title(title)
    
    def plot(self, x, y, c):
        self.graph.axes.plot(x, y, color=c)
