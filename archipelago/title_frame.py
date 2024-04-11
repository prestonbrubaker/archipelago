import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QAction, qApp, QMenuBar, QHBoxLayout, QSpacerItem, QSizePolicy, QMenu)
from PyQt5.QtGui import QFont,QColor,QPalette  
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
        
        self.title = QLabel("Archipelago", self)
        self.title.setAlignment(Qt.AlignCenter)  
        font = QFont("Arial", 54)
        self.title.setFont(font)
        self.title.setStyleSheet("color: black; margin-top: 2rem;")
        mainLayout.addWidget(self.title)

        spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
        mainLayout.addItem(spacer)

        self.centralWidget.setLayout(mainLayout)

        self.menuButton = QPushButton("X", self)
        self.menuButton.setFont(QFont("Helvetica", 18))
        self.menuButton.clicked.connect(self.close)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.menuButton, 0, Qt.AlignRight | Qt.AlignTop)  # Button does not align right
        buttonLayout.addItem(QSpacerItem(50, 50, QSizePolicy.Expanding, QSizePolicy.Minimum))

        mainLayout.addLayout(buttonLayout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

