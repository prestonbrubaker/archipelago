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
        self.timer.start(100)                                   #Refresh rate

    def loadData(self):                                         #Read text file
        try:
            with open('locations.txt', 'r') as file:
                data_string = file.read()
                self.data_array = ast.literal_eval(data_string)
        except Exception as e:
            print(f"Error loading data: {e}")
        self.repaint()                                          #Make sure points are displayed on top

    def paintEvent(self, event):
        painter = QPainter(self)                                #Set POV
        painter.setRenderHint(QPainter.Antialiasing)            #This smooths. Really just aesthetic
        for node in self.data_array:                            #Find all lil nodes in array!
            self.drawNode(painter, *node)

    def drawNode(self, painter, type_, x_unit, y_unit):
        color_dict = {                                          #Dictionary defines colors corresponding to node types
            0: QColor(255, 0, 0),
            1: QColor(0, 255, 0),
            2: QColor(0, 0, 255),
            3: QColor(255, 0, 255)
        }
        color = color_dict.get(type_, QColor(255, 255, 255))    #Set color based on node type dictionary
        x = int(x_unit * self.width())                          #Normalized X
        y = int(y_unit * self.height())                         #Normalized Y
        painter.setPen(QPen(color, 10))                         #Set pen to color previously defined, also give it a weight
        painter.setBrush(QBrush(color, Qt.SolidPattern))       #This fills circles
        painter.drawEllipse(x, y, 5, 5)                         #Draw node!

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataDisplay()
    sys.exit(app.exec_())
