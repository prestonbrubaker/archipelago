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
        self.showFullScreen()  # Set the application to full screen

        self.centralWidget = QWidget(self)  # Central widget to hold layout
        self.setCentralWidget(self.centralWidget)

        mainLayout = QVBoxLayout(self.centralWidget)  # Use a vertical layout for the central widget

        self.menuButton = QPushButton("X", self)
        self.menuButton.setFont(QFont("Arial", 18))
        self.menuButton.clicked.connect(self.displayMenu)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.menuButton, 0, Qt.AlignRight | Qt.AlignTop)  # Align button to the right

        buttonLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        mainLayout.addLayout(buttonLayout)

        self.title = QLabel("Archipelago", self)
        self.title.setAlignment(Qt.AlignCenter)  # Center alignment
        font = QFont("Arial", 24)
        self.title.setFont(font)
        self.title.setStyleSheet("color: red; margin-top: 10px;")  # Font color and top margin
        mainLayout.addWidget(self.title)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        mainLayout.addItem(spacer)

        self.centralWidget.setLayout(mainLayout)


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
