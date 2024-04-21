import sys
import ast
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import QTimer, Qt, QPropertyAnimation

class DataDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.data_array = []

        self.layout = QHBoxLayout(self)
        self.contentArea = QFrame(self)  # Main content area
        self.infoPanel = QFrame(self)    # Info panel
        self.infoPanel.setFixedWidth(0)  # Start with panel closed
        self.layout.addWidget(self.contentArea, 1)
        self.layout.addWidget(self.infoPanel)

        self.toggleButton = QPushButton("Toggle Info", self)
        self.toggleButton.clicked.connect(self.toggleInfoPanel)
        self.layout.addWidget(self.toggleButton)

        self.setWindowTitle("Archipelago")                      # Window title
        self.showMaximized()                                    # Sizes window to max window size without being fullscreened
        self.timer = QTimer(self)                               # This timer forces the screen to update/reload data
        self.timer.timeout.connect(self.loadData)               # Connect loadData to the timer
        self.timer.start(50)                                    # Refresh rate

    def toggleInfoPanel(self):
        width = self.infoPanel.width()
        new_width = 200 if width == 0 else 0  # Toggle between 0 and 200 pixels
        
        # Animation for smoother transition
        self.animation = QPropertyAnimation(self.infoPanel, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.start()

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
        self.repaint()                                          #Make sure points are displayed on top

    def paintEvent(self, event):
        painter = QPainter(self)                                #Set POV
        painter.setRenderHint(QPainter.Antialiasing)            #This smooths. Really just aesthetic
        painter.fillRect(self.rect(), QColor(192, 192, 192))  # Example with a gray background

        
        for node in self.data_array:                            #Find all lil nodes in array! This is where I need my thinking cap for some logic. 
            self.drawNode(painter, *node)

    def drawNode(self, painter, type_, x_unit, y_unit):
        x = int(x_unit * self.width())
        y = int(y_unit * self.height())
        color_dict = {
            0: QColor(255, 224, 189),   # Soul color ;)
            1: QColor(128, 128, 128),   # Structural 
            2: QColor(79, 79, 79),      # Gripper
            3: QColor(34, 139, 34)      # Photosynthesis
        }
        color = color_dict.get(type_, QColor(255, 255, 0))
        painter.setPen(QPen(color, 5))
        painter.setBrush(QBrush(color, Qt.SolidPattern))
        painter.drawEllipse(x, y, 5, 5)

if __name__ == "__main__":
    app = QApplication([])
    window = DataDisplay()
    window.show()
    sys.exit(app.exec_())