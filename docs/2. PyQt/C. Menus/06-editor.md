# 6. Text editor: Keyboard Shortcut Integration

??? note "Version 6"

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
            new_action.setShortcut('Ctrl+N')
    
            # Open action
            open_action = QAction('Open...', self)
            open_action.triggered.connect(self.open_file)
            open_action.setShortcut('Ctrl+O')
    
            # Save action
            save_action = QAction('Save', self)
            save_action.triggered.connect(self.save_file)
            save_action.setShortcut('Ctrl+S')
    
            # Save As action
            save_as_action = QAction('Save As...', self)
            save_as_action.triggered.connect(self.save_file_as)
            save_as_action.setShortcut('Ctrl+Shift+S')
    
            # Quit action
            quit_action = QAction('Quit', self)
            quit_action.triggered.connect(self.close)
            quit_action.setShortcut('Ctrl+Q')
    
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
            elif self.text_edit.toPlainText() != "":
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
            increase_font_action.setShortcut('Ctrl++')
            settings_menu.addAction(increase_font_action)
    
            decrease_font_action = QAction('Decrease font size', self)
            decrease_font_action.triggered.connect(self.decrease_font_size)
            decrease_font_action.setShortcut('Ctrl+-')
            settings_menu.addAction(decrease_font_action)
    
        def add_toolbar(self):
            toolbar = QToolBar("Font Tools")
            self.addToolBar(toolbar)
    
            toolbar.addWidget(QLabel("Font Size:"))
            toolbar.addAction("+", self.increase_font_size)
            toolbar.addAction("-", self.decrease_font_size)
    
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

## Key Changes in This Final Version

This version introduces important refinements to keyboard shortcut handling and menu item presentation. Let's examine
the significant changes from the previous version:

## 1. Integrated Shortcut Management

The most noticeable change is how keyboard shortcuts are now defined directly on menu actions:

```python
def create_file_menu(self):
    # ...
    new_action = QAction('New', self)
    new_action.triggered.connect(self.new_file)
    new_action.setShortcut('Ctrl+N')  # Shortcut added directly to action

    open_action = QAction('Open...', self)
    open_action.triggered.connect(self.open_file)
    open_action.setShortcut('Ctrl+O')  # Shortcut here
```

This approach replaces the previous `add_shortcuts()` method. Shortcuts are now:

- Defined directly on their corresponding actions
- Automatically displayed in menu items
- More tightly integrated with the actions they trigger

## 2. Standard Shortcut Conventions

The application now uses conventional keyboard shortcuts:

```python
# File menu shortcuts
new_action.setShortcut('Ctrl+N')
open_action.setShortcut('Ctrl+O')
save_action.setShortcut('Ctrl+S')
save_as_action.setShortcut('Ctrl+Shift+S')
quit_action.setShortcut('Ctrl+Q')

# Settings menu shortcuts
increase_font_action.setShortcut('Ctrl++')
decrease_font_action.setShortcut('Ctrl+-')
```

This follows standard application conventions, making the shortcuts more discoverable and intuitive for users.

## 3. Improved Save Behavior

The save logic has been refined to prevent unnecessary save prompts for empty documents:

```python
def save_file(self):
    if self.current_file:
    # Existing save logic
    elif self.text_edit.toPlainText() != "":  # New check for empty content
        self.save_file_as()
```

This change prevents the application from prompting users to save empty files, improving the user experience.

## 4. Simplified Code Structure

The previous `add_shortcuts()` method has been removed, simplifying the code:

```python
def init_ui(self):
    # ...
    self.add_toolbar()  # No more add_shortcuts() call
```

Shortcut management is now handled entirely within menu creation methods.

## Impact on Menu Presentation

The menu items now automatically display their associated shortcuts, such as 
"New Ctrl+N", "Open... Ctrl+O", etc.

This provides better user feedback and helps users learn the application's shortcuts.

## Key Concepts Demonstrated

1. **Action-Shortcut Integration**: Shortcuts are directly associated with their corresponding actions
2. **Standard Shortcuts**: Using conventional combinations users expect
3. **Automatic Display**: The menu system automatically shows shortcuts next to menu items
4. **Context-Sensitive Saving**: Only prompt to save non-empty documents

## Practical Takeaways for Students

1. **Use setShortcut()** for better integration with menu items
2. **Follow Platform Conventions** for keyboard shortcuts
3. **Consider Empty States** when implementing save/load logic
4. **Keep Related Functionality Together** by defining shortcuts with their actions
5. **Leverage Automatic Display** of shortcuts in menus

This final version demonstrates how to create a professional-quality menu system with integrated keyboard shortcuts that
follows platform conventions and provides clear visual feedback to users.



---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.