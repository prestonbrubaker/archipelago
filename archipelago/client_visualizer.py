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
        self.setGeometry(100, 100, 800, 600)  # Set default size
        
        self.createMenu()

        self.centralWidget = QWidget(self)  # Central widget to hold layout
        self.setCentralWidget(self.centralWidget)
        
        mainLayout = QVBoxLayout()  # Use a vertical layout
        
        self.title = QLabel("My Application", self)
        self.title.setAlignment(Qt.AlignCenter)  # Center alignment
        font = QFont()
        font.setPointSize(24)  # Font size
        self.title.setFont(font)
        self.title.setStyleSheet("color: hotpink;")  # Font color
        mainLayout.addWidget(self.title)
        
        # Hamburger menu setup
        self.menuButton = QPushButton("☰", self)
        self.menuButton.setFixedSize(40, 40)
        self.menuButton.clicked.connect(self.displayMenu)
        mainLayout.addWidget(self.menuButton, 0, Qt.AlignLeft | Qt.AlignTop)  # Aligns button top-left
        
        # Fullscreen toggle button (for demonstration, placed below title)
        toggleButton = QPushButton("Fullscreen", self)
        toggleButton.clicked.connect(self.toggleFullscreen)
        mainLayout.addWidget(toggleButton)  # Add the button directly to main layout for simplicity
        
        self.centralWidget.setLayout(mainLayout)

    def displayMenu(self):
        # Create the menu
        menu = QMenu(self)
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        menu.addAction(exitAction)
        
        # Show the menu at the button's position
        menu.exec_(self.menuButton.mapToGlobal(self.menuButton.pos()))

    def toggleFullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
