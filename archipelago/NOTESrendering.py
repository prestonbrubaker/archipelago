'''

Ideally, I would soon like to resture our application to match the following structure. This will help with clarity and ease of things such as 
understanding, testing, etc.


evolution_simulation/
│
├── main.py                 # Entry point of the application
├── requirements.txt        # Python dependencies
│
├── app/                    # Application specific modules
│   ├── __init__.py         # Makes app a Python package
│   ├── config.py           # Configuration settings and constants
│   ├── controller.py       # Control flow, connects the model and views
│   └── utils.py            # Utility functions and helpers
│
├── gui/                    # GUI components
│   ├── __init__.py         # Makes gui a Python package
│   ├── mainwindow.py       # Main window of the application
│   ├── settingsdialog.py   # Settings dialog or other sub-windows
│   ├── canvas.py           # OpenGL canvas widget
│   └── widgets.py          # Additional custom widgets
│
├── model/                  # Data handling (business logic)
│   ├── __init__.py         # Makes model a Python package
│   ├── simulation.py       # Handles simulation logic and state
│   ├── organism.py         # Organism definitions and behavior
│   └── environment.py      # Environmental factors and interactions
│
├── resources/              # Resource files like images, icons, etc.
│   └── icons/              # Icons used in the GUI
│       └── icon.png
│
└── tests/                  # Unit and integration tests
    ├── __init__.py         # Makes tests a Python package
    ├── test_simulation.py  # Tests for simulation logic
    ├── test_gui.py         # Tests for GUI components
    └── test_utils.py       # Tests for utility functions
    
    '''