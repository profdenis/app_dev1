# 3. Text editor: settings menu

??? note "Version 3"

    ```python
    import sys
    
    from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                                 QFileDialog, QScrollArea)
    from PyQt6.QtGui import QAction, QFont
    
    
    class TextEditorApp(QMainWindow):
        def __init__(self):
            super().__init__()
            self.current_file = None
            self.init_ui()
    
        def init_ui(self):
            self.setWindowTitle('Text Editor')
            self.setGeometry(100, 100, 800, 600)
    
            # Create scroll area and text edit
            scroll = QScrollArea()
            self.text_area = QTextEdit()
            self.text_area.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
            self.font_size = 12  # or whatever default you want
            font = QFont("Courier New")
            font.setStyleHint(QFont.StyleHint.Monospace)
            font.setFixedPitch(True)
            font.setPointSize(self.font_size)
            self.text_area.setFont(font)
    
            scroll.setWidget(self.text_area)
            scroll.setWidgetResizable(True)
            self.setCentralWidget(scroll)
    
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
    
            self.create_settings_menu()
    
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
    
    
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        editor = TextEditorApp()
        editor.show()
        sys.exit(app.exec())
    ```

## Key Differences from the Previous Example

This modified text editor example builds on the previous one by introducing several important new features, particularly
in the menu system. Let's focus on these differences:

## 1. Multiple Menus

The most significant difference is the addition of a second menu called "Settings":

```python
def create_settings_menu(self):
    menubar = self.menuBar()
    settings_menu = menubar.addMenu('Settings')

    # Add actions to the Settings menu
    increase_font_action = QAction('Increase font size', self)
    increase_font_action.triggered.connect(self.increase_font_size)
    settings_menu.addAction(increase_font_action)

    decrease_font_action = QAction('Decrease font size', self)
    decrease_font_action.triggered.connect(self.decrease_font_size)
    settings_menu.addAction(decrease_font_action)
```

This demonstrates how to create multiple menus in the menu bar. The application now has:

- A "File" menu for document operations
- A "Settings" menu for application preferences

## 2. Menu Organization with a Separate Method

The code uses a separate method `create_settings_menu()` to organize the creation of the Settings menu:

```python
def init_ui(self):
    # ... other code ...

    # Create File menu and its actions
    # ... (code for File menu) ...

    # Create Settings menu using a separate method
    self.create_settings_menu()
```

This is a good practice for organizing code when you have multiple menus. Each menu can have its own setup method,
making the code more modular and easier to maintain.

## 3. Font Configuration Actions

The Settings menu contains actions that affect the application's appearance:

```python
increase_font_action = QAction('Increase font size', self)
increase_font_action.triggered.connect(self.increase_font_size)

decrease_font_action = QAction('Decrease font size', self)
decrease_font_action.triggered.connect(self.decrease_font_size)
```

These actions demonstrate how menus can control application settings rather than just performing file operations.

## 4. State Management

The application now maintains state information for the font size:

```python
self.font_size = 12  # Default font size
```

This state variable is modified by the menu actions:

```python
def increase_font_size(self):
    self.font_size += 1
    self.set_textedit_font()


def decrease_font_size(self):
    if self.font_size > 1:
        self.font_size -= 1
        self.set_textedit_font()
```

This demonstrates how menu actions can update application state and trigger visual changes.

## 5. Helper Methods for Actions

The code includes helper methods that implement the functionality triggered by menu actions:

```python
def set_textedit_font(self):
    font = QFont("Source Code Pro")
    font.setStyleHint(QFont.StyleHint.Monospace)
    font.setFixedPitch(True)
    font.setPointSize(self.font_size)
    self.text_area.setFont(font)
```

This method is called by both font size actions, showing how to reuse functionality across multiple menu items.

## Menu Design Principles Demonstrated

1. **Logical Grouping**: Related functions are grouped in their own menus (file operations in "File", appearance
   settings in "Settings").

2. **Hierarchical Organization**: The menu bar contains multiple top-level menus, each with their own set of actions.

3. **Consistent Naming**: Menu items use clear, action-oriented names that describe what they do.

4. **Functional Separation**: Different types of functionality are separated into different menus.

5. **State Management**: Menu actions can both read and modify application state.

## Practical Applications

This enhanced menu system demonstrates patterns that students can apply to their own applications:

1. **Settings Control**: Menus can be used to control application settings and preferences.

2. **Multiple Menu Categories**: Applications can organize functionality into multiple logical categories.

3. **Dynamic UI Updates**: Menu actions can trigger visual changes in the application.

4. **Code Organization**: Menu creation can be organized into separate methods for better code structure.


---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.