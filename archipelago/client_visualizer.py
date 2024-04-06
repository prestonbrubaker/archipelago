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
        font = self.title.font()
        font.setPointSize(24)  # Font size
        self.title.setFont(font)
        self.title.setStyleSheet("color: hotpink;")  # Font color
        mainLayout.addWidget(self.title)
        
        # Layout for the toggle button
        topLayout = QHBoxLayout()
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        topLayout.addItem(spacer)  # Pushes the button to the right
        
        toggleButton = QPushButton("Fullscreen", self)
        toggleButton.setFixedSize(40, 40)  # Smaller, fixed size
        toggleButton.clicked.connect(self.toggleFullscreen)
        topLayout.addWidget(toggleButton)
        mainLayout.addLayout(topLayout)
        
        self.centralWidget.setLayout(mainLayout)

    def createMenu(self):
        menuBar = self.QPushButton()
        fileMenu = menuBar.addMenu("☰")
        fileMenu.setAlignment(Qt.AlignRight)

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)

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
