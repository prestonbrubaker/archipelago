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
        
        self.title = QLabel("My Archipelago", self)
        self.title.setAlignment(Qt.AlignCenter)  # Center alignment
        font = QFont()
        font.setPointSize(24)  # Font size
        self.title.setFont(font)
        self.title.setStyleSheet("color: hotpink;margin-top: 1rem;")  # Font color
        mainLayout.addWidget(self.title)
        
        self.menuButton = QPushButton("☰", self)
        self.menuButton.setFont(QFont("Ariel", 18))
        self.menuButton.setFixedSize(60, 40)
        self.menuButton.clicked.connect(self.displayMenu)
        mainLayout.addWidget(self.menuButton, 0, Qt.AlignRight | Qt.AlignTop)

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
