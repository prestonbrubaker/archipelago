import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QAction, qApp, QMenuBar

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('PyQt5 Fullscreen Toggle')
        self.setGeometry(100, 100, 600, 400)  # Set default size
        
        self.createMenu()

        self.centralWidget = QWidget(self)  # Central widget to hold layout
        self.setCentralWidget(self.centralWidget)
        
        layout = QVBoxLayout()  # Use a vertical layout
        
        self.title = QLabel("My Application", self)
        layout.addWidget(self.title)  # Add a title
        
        toggleButton = QPushButton("Toggle Fullscreen", self)
        toggleButton.clicked.connect(self.toggleFullscreen)
        layout.addWidget(toggleButton)  # Add a button to toggle fullscreen
        
        self.centralWidget.setLayout(layout)

    def createMenu(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')

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

