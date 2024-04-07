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
        self.showFullScreen()  # Set default size
        
        self.centralWidget = QWidget(self)  # Central widget to hold layout
        self.setCentralWidget(self.centralWidget)
        
        mainLayout = QVBoxLayout()  # Use a vertical layout

        spacer = QWidget(self)
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        mainLayout.addWidget(spacer)

        self.menuButton = QPushButton("Menu", self)
        self.menuButton.setFont(QFont("Arial", 18))
        self.menuButton.clicked.connect(self.displayMenu)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.menuButton, 0, Qt.AlignRight | Qt.AlignTop)  # Align button to the right
        mainLayout.addLayout(buttonLayout)

        self.centralWidget.setLayout(mainLayout)
        
        self.title = QLabel("Archipelago", self)
        self.title.setAlignment(Qt.AlignCenter)  # Center alignment
        font = QFont("Arial", 24)  # Corrected font family name
        self.title.setFont(font)
        self.title.setStyleSheet("color: red;")  # Font color
        mainLayout.addWidget(self.title)
        mainLayout.setAlignment(self.title, Qt.AlignTop)

    def displayMenu(self):
        # Create the menu
        menu = QMenu(self)
        action1 = QAction('Option 1', self)
        action2 = QAction('Option 2', self)
        exitAction = QAction('Exit', self)
        
        action1.triggered.connect(lambda: print("Option 1 selected"))
        action2.triggered.connect(lambda: print("Option 2 selected"))
        exitAction.triggered.connect(self.close)
        
        menu.addAction(action1)
        menu.addAction(action2)
        menu.addSeparator()
        menu.addAction(exitAction)
        
        # Show the menu at the button's position
        menu.exec_(self.menuButton.mapToGlobal(self.menuButton.pos()))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
