# 4. Text editor: Toolbar and Mouse Wheel Events

````python
import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                             QFileDialog, QScrollArea, QToolBar, QLabel)
from PyQt6.QtGui import QAction, QFont, QShortcut, QKeySequence
from PyQt6.QtCore import Qt, pyqtSignal


class TextEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Text Editor')
        self.setGeometry(100, 100, 800, 600)

        self.create_text_edit()

        self.create_file_menu()
        self.create_settings_menu()

        self.add_toolbar()
        self.add_shortcuts()

    def create_text_edit(self):
        # Create scroll area and text edit
        self.text_area = WheelAwareTextEdit()
        self.text_area.ctrl_wheel.connect(self.handle_ctrl_wheel)
        self.text_area.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.font_size = 12  # or whatever default you want
        font = QFont("Courier New")
        font.setStyleHint(QFont.StyleHint.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(self.font_size)
        self.text_area.setFont(font)

        scroll = QScrollArea()
        scroll.setWidget(self.text_area)
        scroll.setWidgetResizable(True)

        self.setCentralWidget(scroll)

    def create_file_menu(self):
        # Create menu bar
        menubar = self.menuBar()
        # File menu
        file_menu = menubar.addMenu('File')
        # New action
        new_action = QAction('New', self)
        new_action.triggered.connect(self.new_file)
        # Open action
        open_action = QAction('Open...', self)
        open_action.triggered.connect(self.open_file)
        # Save action
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_file)
        # Save As action
        save_as_action = QAction('Save As...', self)
        save_as_action.triggered.connect(self.save_file_as)
        # Quit action
        quit_action = QAction('Quit', self)
        quit_action.triggered.connect(self.close)
        # Add actions to menu
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)

    def new_file(self):
        self.current_file = None
        self.text_area.clear()

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt);;Markdown Files (*.md);;All Files (*)"
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.text_area.setText(file.read())
                self.current_file = file_path
            except Exception as e:
                self.show_error(str(e))

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(self.text_area.toPlainText())
            except Exception as e:
                self.show_error(str(e))
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_area.toPlainText())
                self.current_file = file_path
            except Exception as e:
                self.show_error(str(e))

    def show_error(self, message):
        error_dialog = QFileDialog(self)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.exec()

    def set_textedit_font(self):
        font = QFont("Source Code Pro")
        font.setStyleHint(QFont.StyleHint.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(self.font_size)
        self.text_area.setFont(font)

    def increase_font_size(self):
        self.font_size += 1
        self.set_textedit_font()

    def decrease_font_size(self):
        if self.font_size > 1:
            self.font_size -= 1
            self.set_textedit_font()

    def create_settings_menu(self):
        menubar = self.menuBar()
        settings_menu = menubar.addMenu('Settings')

        increase_font_action = QAction('Increase font size', self)
        increase_font_action.triggered.connect(self.increase_font_size)
        settings_menu.addAction(increase_font_action)

        decrease_font_action = QAction('Decrease font size', self)
        decrease_font_action.triggered.connect(self.decrease_font_size)
        settings_menu.addAction(decrease_font_action)

    def add_toolbar(self):
        toolbar = QToolBar("Font Tools")
        self.addToolBar(toolbar)

        toolbar.addWidget(QLabel("Font Size:"))
        toolbar.addAction("+", self.increase_font_size)
        toolbar.addAction("-", self.decrease_font_size)

    def add_shortcuts(self):
        QShortcut(QKeySequence("Ctrl++"), self).activated.connect(self.increase_font_size)
        QShortcut(QKeySequence("Ctrl+-"), self).activated.connect(self.decrease_font_size)

    def handle_ctrl_wheel(self, delta):
        if delta > 0:  # Wheel scrolled up
            self.increase_font_size()
        else:  # Wheel scrolled down
            self.decrease_font_size()


class WheelAwareTextEdit(QTextEdit):
    ctrl_wheel = pyqtSignal(int)  # Emit wheel delta

    def wheelEvent(self, event):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.ctrl_wheel.emit(event.angleDelta().y())
            event.accept()
        else:
            super().wheelEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditorApp()
    editor.show()
    sys.exit(app.exec())
````

## Key Changes in This Version

This version of the text editor introduces several significant enhancements to the user interface, particularly in how
users can interact with the application. Let's focus on the key differences from the previous version:

## 1. Code Organization

The code has been reorganized into more focused methods:

```python
def init_ui(self):
    self.setWindowTitle('Text Editor')
    self.setGeometry(100, 100, 800, 600)

    self.create_text_edit()
    self.create_file_menu()
    self.create_settings_menu()
    self.add_toolbar()
    self.add_shortcuts()
```

This modular approach makes the code more maintainable and easier to understand. Each UI component has its own dedicated
setup method.

## 2. Toolbar Integration

A major addition is the toolbar, which provides quick access to font size controls:

```python
def add_toolbar(self):
    toolbar = QToolBar("Font Tools")
    self.addToolBar(toolbar)

    toolbar.addWidget(QLabel("Font Size:"))
    toolbar.addAction("+", self.increase_font_size)
    toolbar.addAction("-", self.decrease_font_size)
```

This demonstrates how to:

- Create a toolbar using `QToolBar`
- Add a label to the toolbar using `addWidget()`
- Add actions to the toolbar that connect to the same methods used by menu items

The toolbar provides an alternative way to access functionality that's also available in the menus, which is a common
pattern in modern applications.

## 3. Keyboard Shortcuts

Another significant addition is keyboard shortcuts for common operations:

```python
def add_shortcuts(self):
    QShortcut(QKeySequence("Ctrl++"), self).activated.connect(self.increase_font_size)
    QShortcut(QKeySequence("Ctrl+-"), self).activated.connect(self.decrease_font_size)
```

This code:

- Creates `QShortcut` objects with specific key combinations
- Connects them to the same methods used by the menu items and toolbar actions
- Provides yet another way for users to access the same functionality

## 4. Custom Widget with Signal

The application now uses a custom `QTextEdit` subclass that emits a signal when the user scrolls with the Ctrl key
pressed:

```python
class WheelAwareTextEdit(QTextEdit):
    ctrl_wheel = pyqtSignal(int)  # Emit wheel delta

    def wheelEvent(self, event):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.ctrl_wheel.emit(event.angleDelta().y())
            event.accept()
        else:
            super().wheelEvent(event)
```

This custom widget:

- Defines a new signal `ctrl_wheel` using `pyqtSignal`
- Overrides the `wheelEvent` method to detect Ctrl+wheel combinations
- Emits the signal with the wheel delta value when Ctrl is pressed
- Otherwise, passes the event to the parent class

## 5. Signal-Slot Connection for Wheel Events

The application connects to the custom signal:

```python
def create_text_edit(self):
    # Create scroll area and text edit
    self.text_area = WheelAwareTextEdit()
    self.text_area.ctrl_wheel.connect(self.handle_ctrl_wheel)
    # ...
```

And handles it with a dedicated method:

```python
def handle_ctrl_wheel(self, delta):
    if delta > 0:  # Wheel scrolled up
        self.increase_font_size()
    else:  # Wheel scrolled down
        self.decrease_font_size()
```

This provides a third way to change the font size (Ctrl+wheel), in addition to the menu and toolbar.

## Multiple Access Paths to the Same Functionality

This example demonstrates a key principle in UI design: providing multiple ways to access the same functionality:

1. **Menu items** - Traditional access through hierarchical menus
2. **Toolbar buttons** - Quick access through visible buttons
3. **Keyboard shortcuts** - Efficient access for keyboard-oriented users
4. **Mouse gestures** (Ctrl+wheel) - Intuitive access using familiar gestures

Each of these methods connects to the same underlying functionality (`increase_font_size()` and `decrease_font_size()`),
which ensures consistent behavior regardless of how the user chooses to interact with the application.

## Menu Design in Context

The menus in this version serve as just one part of a comprehensive UI strategy. They provide a discoverable,
hierarchical organization of all available commands, while the toolbar, shortcuts, and gestures provide quicker access
to common operations.

This approach follows modern application design principles, where menus act as a complete catalog of functionality,
while other UI elements provide optimized paths to frequently used features.

## Practical Takeaways

1. **Multiple access paths** improve usability by accommodating different user preferences.
2. **Consistent functionality** ensures that the same action produces the same result, regardless of how it's triggered.
3. **Modular code organization** makes complex applications easier to maintain.
4. **Custom widgets and signals** allow for sophisticated user interactions.
5. **Toolbars complement menus** by providing quick access to common commands.


