import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QAction, qApp, QMenuBar, QHBoxLayout, QSpacerItem, QSizePolicy, QMenu)
from PyQt5.QtGui import QFont,QColor,QPalette  # Corrected import for QFont
from PyQt5.QtCore import Qt

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        self.setWindowTitle('ARCHIPELAGO')
        self.showFullScreen()  

        self.centralWidget = QWidget(self) 
        self.setCentralWidget(self.centralWidget)

        mainLayout = QVBoxLayout(self.centralWidget) 

        self.menuButton = QPushButton("X", self)
        self.menuButton.setFont(QFont("Arial", 18))
        self.menuButton.clicked.connect(self.close)  # Directly close the application on click


        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.menuButton, 0, Qt.AlignRight | Qt.AlignTop)  # Align button to the right

        buttonLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        mainLayout.addLayout(buttonLayout)

        self.title = QLabel("Archipelago", self)
        self.title.setAlignment(Qt.AlignCenter)  # Center alignment
        font = QFont("Arial", 36)
        self.title.setFont(font)
        self.title.setStyleSheet("color: red; margin-top: 2rem;")  # Font color and top margin
        mainLayout.addWidget(self.title)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        mainLayout.addItem(spacer)

        self.centralWidget.setLayout(mainLayout)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
