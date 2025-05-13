# 5. Text editor: Document State Management

??? note "Version 5"

    ```python
    import sys
    
    from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                                 QFileDialog, QScrollArea, QToolBar, QLabel, QMessageBox)
    from PyQt6.QtGui import QAction, QFont, QShortcut, QKeySequence
    from PyQt6.QtCore import Qt, pyqtSignal
    
    
    class TextEditorApp(QMainWindow):
        def __init__(self):
            super().__init__()
            self.is_modified = None
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
    
        def mark_modified(self):
            self.is_modified = True
    
        def create_text_edit(self):
            # Create scroll area and text edit
            self.text_edit = WheelAwareTextEdit()
            self.text_edit.ctrl_wheel.connect(self.handle_ctrl_wheel)
            self.text_edit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
            self.text_edit.textChanged.connect(self.mark_modified)
    
            self.font_size = 12  # or whatever default you want
            font = QFont("Courier New")
            font.setStyleHint(QFont.StyleHint.Monospace)
            font.setFixedPitch(True)
            font.setPointSize(self.font_size)
            self.text_edit.setFont(font)
    
            scroll = QScrollArea()
            scroll.setWidget(self.text_edit)
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
            if not self.maybe_save():
                return
            self.current_file = None
            self.text_edit.clear()
            self.is_modified = False
    
        def open_file(self):
            if not self.maybe_save():
                return
            file_path, _ = QFileDialog.getOpenFileName(
                self, "Open File", "", "Text Files (*.txt);;Markdown Files (*.md);;All Files (*)"
            )
            if file_path:
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        self.text_edit.setText(file.read())
                    self.current_file = file_path
                    self.is_modified = False
                except Exception as e:
                    self.show_error(str(e))
    
        def save_file(self):
            if self.current_file:
                try:
                    with open(self.current_file, 'w', encoding='utf-8') as file:
                        file.write(self.text_edit.toPlainText())
                    self.is_modified = False
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
                        file.write(self.text_edit.toPlainText())
                    self.current_file = file_path
                    self.is_modified = False
                except Exception as e:
                    self.show_error(str(e))
    
        def maybe_save(self):
            """
            Checks if there are unsaved changes and prompts the user to save them. If there are no changes
            or the user confirms an action, the method returns True. Otherwise, depending on the user's
            response, it may prompt to save, discard changes, or cancel.
    
            QMessageBox::StandardButton.Yes: Saves the file and proceeds after the user confirms.
            QMessageBox::StandardButton.No: Discards unsaved changes and proceeds after the user confirms.
            QMessageBox::StandardButton.Cancel: Cancels the operation and takes no further action.
    
            :return:
                True if the user opts to save or discard the changes, or if there are no unsaved changes.
                False if the user cancels the action.
            :rtype: bool
            """
            if self.is_modified:
                reply = QMessageBox.question(
                    self, "Unsaved Changes",
                    "You have unsaved changes. Do you want to save them?",
                    QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No |
                    QMessageBox.StandardButton.Cancel
                )
                if reply == QMessageBox.StandardButton.Yes:
                    self.save_file()
                    return True
                elif reply == QMessageBox.StandardButton.No:
                    return True
                else:
                    return False
            return True
    
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
            self.text_edit.setFont(font)
    
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
    
        def closeEvent(self, event):
            if self.maybe_save():
                event.accept()
            else:
                event.ignore()
    
    
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
    
    ```

## Key Changes in This Version

This version of the text editor introduces an important concept in document-based applications: tracking and managing
document modification state. Let's focus on these changes and how they affect the menu-driven workflow.

## 1. Document Modification Tracking

The most significant addition is tracking whether the document has been modified:

```python
def __init__(self):
    super().__init__()
    self.is_modified = None  # New state variable
    self.current_file = None
    self.init_ui()
```

The application now maintains an `is_modified` flag to track whether the document has unsaved changes.

```python
def create_text_edit(self):
    # ...
    self.text_edit.textChanged.connect(self.mark_modified)
    # ...
```

```python
def mark_modified(self):
    self.is_modified = True
```

The application connects to the `textChanged` signal of the text editor, which is emitted whenever the text is modified.
This automatically sets the `is_modified` flag to `True`.

## 2. Unsaved Changes Dialog

A major enhancement is the addition of a confirmation dialog when attempting to close a document with unsaved changes:

```python
def maybe_save(self):
    if self.is_modified:
        reply = QMessageBox.question(
            self, "Unsaved Changes",
            "You have unsaved changes. Do you want to save them?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No |
            QMessageBox.StandardButton.Cancel
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.save_file()
            return True
        elif reply == QMessageBox.StandardButton.No:
            return True
        else:
            return False
    return True
```

This method:

1. Checks if the document has been modified
2. If modified, displays a dialog asking the user if they want to save changes
3. Handles the user's response (Yes, No, or Cancel)
4. Returns `True` if the operation should continue, `False` if it should be canceled

## 3. Integration with File Operations

The `maybe_save()` method is now called before operations that would discard the current document:

```python
def new_file(self):
    if not self.maybe_save():
        return
    self.current_file = None
    self.text_edit.clear()
```

```python
def open_file(self):
    if not self.maybe_save():
        return
    # ... rest of open_file code ...
```

This ensures that users are prompted to save unsaved changes before these operations proceed.

## 4. Resetting the Modified Flag

When a file is saved or opened, the `is_modified` flag is reset to `False`:

```python
def save_file(self):
    if self.current_file:
        try:
            with open(self.current_file, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())
            self.is_modified = False  # Reset modified flag after saving
        except Exception as e:
            self.show_error(str(e))
    else:
        self.save_file_as()
```

Similar code appears in `save_file_as()` and `open_file()`.

## 5. Handling Application Close Events

The application now intercepts close events to check for unsaved changes:

```python
def closeEvent(self, event):
    if self.maybe_save():
        event.accept()
    else:
        event.ignore()
```

This ensures that users are prompted to save unsaved changes even when closing the application window.

## Impact on Menu-Driven Workflow

These changes significantly enhance the menu-driven workflow by:

1. **Preventing Data Loss**: The application now prevents users from accidentally losing unsaved work.

2. **Providing Context-Aware Choices**: Users are given appropriate options (Save, Don't Save, Cancel) when performing
   actions that would discard changes.

3. **Maintaining Document State**: The application tracks document state and provides appropriate feedback and options
   based on that state.

4. **Consistent Behavior**: The same document state management applies whether using menu commands, keyboard shortcuts,
   or window close events.

## Standard Application Behavior

This version implements behavior that users expect from professional document-editing applications:

1. **Modified Document Indicator**: The application tracks whether the document has been modified.

2. **Save Prompts**: Users are prompted to save changes before actions that would discard them.

3. **Cancel Option**: Users can cancel operations that would discard their work.

4. **Consistent State Management**: The modified state is consistently updated across all operations.

## Practical Takeaways for Students

1. **State Management**: Tracking application state (like document modification) is crucial for providing a good user
   experience.

2. **User Confirmation**: Always confirm with users before potentially destructive actions.

3. **Signal Connections**: Connect to appropriate signals (like `textChanged`) to keep state information updated.

4. **Event Handling**: Override events like `closeEvent` to integrate state management with system-level interactions.

5. **Consistent Behavior**: Ensure consistent behavior across all ways of triggering the same functionality.

This example demonstrates how to build a more robust, user-friendly application that protects users' work while
maintaining a clean, menu-driven interface.



---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.