# 5. Menus

## Introduction to Menus

````python
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction

import sys

class SimpleMenuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Simple Menu App')
        self.setGeometry(100, 100, 400, 300)

        # Create a menu bar
        menubar = self.menuBar()

        # Add File menu
        file_menu = menubar.addMenu('File')

        # Add Quit action
        quit_action = QAction('Quit', self)
        quit_action.triggered.connect(self.close)  # Close the app when triggered
        file_menu.addAction(quit_action)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleMenuApp()
    ex.show()
    sys.exit(app.exec())
````

In this example, we're creating a simple PyQt6 application that demonstrates how to add a menu bar to your GUI
application. Menus are an essential part of most desktop applications, providing a way to organize commands and features
in a hierarchical structure.

## Breaking Down the Code

Let's analyze this example step by step, focusing on the menu implementation:

```python
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction

import sys
```

First, we import the necessary classes:

- `QMainWindow`: This is the main window class that provides a framework for building an application's UI with menus,
  toolbars, etc.
- `QAction`: This class provides an abstract user interface action that can be inserted into menus and toolbars.

```python
class SimpleMenuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
```

We create a class that inherits from `QMainWindow`, which automatically gives us the ability to add menus, toolbars, and
status bars.

### Menu Creation Process

```python
def init_ui(self):
    self.setWindowTitle('Simple Menu App')
    self.setGeometry(100, 100, 400, 300)

    # Create a menu bar
    menubar = self.menuBar()
```

The `menuBar()` method returns the menu bar for the main window. If the menu bar doesn't exist yet, a new one is
created. This is your first step in creating menus.

```python
    # Add File menu
file_menu = menubar.addMenu('File')
```

The `addMenu()` method creates a new menu in the menu bar with the title 'File'. This returns a `QMenu` object that we
can add actions to.

```python
    # Add Quit action
quit_action = QAction('Quit', self)
quit_action.triggered.connect(self.close)  # Close the app when triggered
file_menu.addAction(quit_action)
```

Here's where we create a menu item:

1. We create a `QAction` with the text 'Quit'
2. We connect its `triggered` signal to the `close()` method of our window
3. We add this action to our File menu using `addAction()`

When a user clicks on "File" in the menu bar, a dropdown will appear with "Quit" as an option. Clicking "Quit" will
trigger the action, which will call `self.close()` to close the application.

## Key Concepts About Menus

1. **Menu Hierarchy**: Menus in PyQt6 follow a hierarchy:
    - Menu Bar (top level)
    - Menus (like File, Edit, View)
    - Actions (the actual commands users can select)

2. **QAction**: This class represents an item that a user can select from a menu. Actions can:
    - Display text and/or an icon
    - Have a shortcut key
    - Show status tips
    - Trigger a signal when activated

3. **Signal-Slot Connection**: The line `quit_action.triggered.connect(self.close)` demonstrates PyQt's signal-slot
   mechanism. When the action is triggered (clicked), it emits a signal that is connected to the `close()` slot.


