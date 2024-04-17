import sys
import ast
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import QTimer, Qt

class DataDisplay(QWidget):
    def __init__(self):
        super().__init__()                                      # No idea what this does but necessary
        self.data_array = []                                    #This creates an array out of data pulled from txt file
        self.setWindowTitle("Archipelago")                      #Window title
        self.showMaximized()                                    #Sizes window to max window size without being fullscreened
        self.timer = QTimer(self)                               #This timer forces the screen to update/reload data
        self.timer.timeout.connect(self.loadData)               #See above
        self.timer.start(50)                                    #Refresh rate

    def loadData(self):
        try:
            with open('locations.txt', 'r') as file:
                data_string = file.read().strip()
            if data_string:
                self.data_array = ast.literal_eval(data_string)
            else:
                print("Warning: Data string is empty.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        self.repaint()                                    #Make sure points are displayed on top

    def paintEvent(self, event):
        painter = QPainter(self)                                #Set POV
        painter.setRenderHint(QPainter.Antialiasing)            #This smooths. Really just aesthetic
        for node in self.data_array:                            #Find all lil nodes in array!
            self.drawNode(painter, *node)

    def drawNode(self, painter, type_, x_unit, y_unit):
        x = int(x_unit * self.width())
        y = int(y_unit * self.height())
        color_dict = {
            0: QColor(255, 0, 0),
            1: QColor(0, 255, 255),
            2: QColor(0, 0, 255),
            3: QColor(0, 255, 0)
        }
        color = color_dict.get(type_, QColor(255, 255, 0))
        painter.setPen(QPen(color, 5))
        painter.setBrush(QBrush(color, Qt.SolidPattern))
        painter.drawEllipse(x, y, 5, 5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataDisplay()
    sys.exit(app.exec_())

