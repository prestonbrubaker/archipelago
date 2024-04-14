# Draw squares on the screen!

from client_backend import get_positions_of_nodes
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import QTimer, Qt

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.data_generator = get_positions_of_nodes()
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)  
        self.timer.start(100)

    def initUI(self):
        self.setWindowTitle('Archipelago')
        self.showMaximized()

    def paintEvent(self, event):
        painter = QPainter(self)
        try:
            orgs = next(self.data_generator)
            if len(orgs) >= 1: 
                self.drawNode(painter, orgs[0])
                self.drawNode(painter, orgs[1])
        except StopIteration:
            self.timer.stop()
        finally:
            painter.end()


    def drawNode(self, painter, node):
        type_, x, y = node
        x = int(x * self.width())
        y = int(y * self.height())
    
        if type_ == 0:
            color = QColor(0, 0, 255)  # Blue
        elif type_ == 1:
            color = QColor(255, 0, 0)  # Red
        elif type_ == 2:
            color = QColor(0, 0, 0)  # Green
        elif type_ == 3:
            color = QColor(0, 255, 0)  # Photosynthesis

        painter.setPen(QPen(color, 2, Qt.SolidLine))
        painter.drawRect(x, y, 10, 10)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
