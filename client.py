import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTimer
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
import random

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)  # Window size changed to 1000x1000
        self.setWindowTitle('Shapes and Text')
        
        # Timer setup
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)  # Calls the update method, which triggers paintEvent
        self.timer.start(1000)  # Timer times out every 1000 milliseconds (1 second)

        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawShapes(qp)
        qp.end()

    def drawShapes(self, qp):
        # Randomly generate coordinates for the circle
        x = random.randint(0, 900)  # Adjusted for the circle's size to ensure it's fully visible
        y = random.randint(0, 900)

        # Set the brush to a nice blue color and draw a circle
        qp.setBrush(QColor(0, 0, 255))
        qp.drawEllipse(x, y, 100, 100)  # Use random coordinates for the circle

        # Draw a black line
        qp.setPen(QColor(0, 0, 0))
        qp.drawLine(120, 10, 220, 100)

        # Draw some text
        qp.setPen(QColor(255, 0, 0))
        qp.setFont(QFont('Arial', 10))
        qp.drawText(10, 950, "A circle, a line, and this text")  # Moved text to avoid overlap with the circle

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
