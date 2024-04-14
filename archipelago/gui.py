import sys
import ast
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import QTimer, Qt

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.nodes = []
        self.current_index = 0
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_and_update)
        self.timer.start(100) 

    def load_nodes(self):
        nodes = []
        try:
            with open("locations.txt", "r") as file:
                data = file.read()
                # Assuming the entire file is one valid Python literal (e.g., a list of tuples)
                nodes = ast.literal_eval(data)
        except Exception as e:
            print(f"Failed to load data: {e}")
        return nodes

    def initUI(self):
        self.setWindowTitle('Archipelago')
        self.showMaximized()

    def refresh_and_update(self):
        # Reload data from file in case it has been updated
        self.nodes = self.load_nodes()
        self.current_index = 0  # Reset index to redraw from start
        self.update()  # Trigger repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.current_index + 1 < len(self.nodes):
            self.drawNode(painter, self.nodes[self.current_index])
            self.drawNode(painter, self.nodes[self.current_index + 1])
            self.current_index += 2
        else:
            self.timer.stop()
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
            color = QColor(0, 255, 0)  # Green
        elif type_ == 3:
            color = QColor(0, 0, 0)  # Black

        painter.setPen(QPen(color, 2, Qt.SolidLine))
        painter.drawRect(x, y, 10, 10)  # Draw rectangle representing the node

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
