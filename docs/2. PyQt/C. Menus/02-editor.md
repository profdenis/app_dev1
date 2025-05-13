# 2. Simple text editor

This example builds on our previous menu example by creating a functional text editor with a more complete menu system.
Let's focus on how the menus are implemented and how they connect to the application's functionality.

??? note "Version 2"
    
    ```python
    import sys
    
    from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                                 QFileDialog, QScrollArea)
    from PyQt6.QtGui import QAction
    
    
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
                self, "Save File", "", "Text Files (*.txt);;Markdown Files (*.md);;All Files (*)"
            )
            if file_path:
                try:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(self.text_area.toPlainText())
                    self.current_file = file_path
                except Exception as e:
                    self.show_error(str(e))
    
        def show_error(self, message):
            error_dialog = QFileDialog(self)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText(message)
            error_dialog.exec()
    
    
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        editor = TextEditorApp()
        editor.show()
        sys.exit(app.exec())
    ```

## Menu Structure in This Example

In this text editor application, we create a more sophisticated menu structure with multiple actions and a separator:

```python
# Create menu bar
menubar = self.menuBar()

# File menu
file_menu = menubar.addMenu('File')
```

Just like in our previous example, we start by getting the menu bar and adding a 'File' menu to it.

### Creating Multiple Menu Actions

```python
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
```

Here we create five different actions for our File menu:

1. **New** - Creates a new empty document
2. **Open...** - Opens an existing file
3. **Save** - Saves the current file
4. **Save As...** - Saves the current file with a new name
5. **Quit** - Exits the application

Each action follows the same pattern:

- Create a `QAction` with a descriptive label
- Connect its `triggered` signal to the appropriate method

### Adding Actions to the Menu with a Separator

```python
# Add actions to menu
file_menu.addAction(new_action)
file_menu.addAction(open_action)
file_menu.addAction(save_action)
file_menu.addAction(save_as_action)
file_menu.addSeparator()  # This adds a horizontal line in the menu
file_menu.addAction(quit_action)
```

After creating the actions, we add them to the menu. Notice the `addSeparator()` method, which adds a horizontal line
between menu items. This is a common UI pattern used to group related actions together. In this case, it separates the
file operations from the application exit command.

## Connecting Menu Actions to Functionality

Each menu action is connected to a method that performs the corresponding operation:

```python
def new_file(self):
    self.current_file = None
    self.text_area.clear()
```

The `new_file` method resets the current file to `None` and clears the text area.

```python
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
```

The `open_file` method uses `QFileDialog.getOpenFileName()` to display a file selection dialog. If a file is selected,
it reads the content and displays it in the text area.

Similar implementations exist for `save_file` and `save_file_as`.

## Key Menu Concepts Demonstrated

1. **Multiple Actions**: A real-world menu typically contains multiple related actions.

2. **Separators**: The `addSeparator()` method adds visual separation between groups of related menu items.

3. **Dialog Integration**: Menu actions often trigger dialogs, like the file open/save dialogs shown here.

4. **Conventional Naming**: Notice how menu items that open dialogs end with "..." (e.g., "Open..."). This is a UI
   convention indicating that selecting this option will require additional input.

5. **Error Handling**: The methods connected to menu actions include error handling to manage potential issues.

## Menu Design Best Practices

1. **Logical Grouping**: Group related actions together (file operations are grouped, with Quit separated).

2. **Standard Menus**: Follow conventions for menu names and organization (File, Edit, View, etc.).

3. **Clear Labels**: Use clear, concise labels for menu items.

4. **Consistent Terminology**: Use consistent terms across your application.

This example demonstrates how to create a practical menu system that follows standard UI conventions and connects to
actual application functionality. Students can use this as a template for creating their own menu-driven applications.



---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.