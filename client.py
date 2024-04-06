import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Shapes and Text')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawShapes(qp)
        qp.end()

    def drawShapes(self, qp):
        # Set the brush to a nice blue color and draw a circle
        qp.setBrush(QColor(0, 0, 255))
        qp.drawEllipse(10, 10, 100, 100)

        # Draw a black line
        qp.setPen(QColor(0, 0, 0))
        qp.drawLine(120, 10, 220, 100)

        # Draw some text
        qp.setPen(QColor(255, 0, 0))
        qp.setFont(QFont('Arial', 10))
        qp.drawText(10, 150, "A circle, a line, and this text")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
