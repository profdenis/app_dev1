# 1. OS Events Overview

To handle OS events like mouse interactions and window closing in PyQt6, you intercept events by subclassing widgets and
overriding their event handler methods. Here's an example of a structured approach:

??? info "Example: Mouse position"
   ```python
   from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
   from PyQt6.QtGui import QCursor
   import sys
   
   
   class CustomButton(QPushButton):
       def __init__(self, label, parent=None):
           super().__init__(label, parent)
           self.position_label = None
   
       def mousePressEvent(self, event):
           if self.position_label:
               pos = event.position()
               self.position_label.setText(f"Subclass method: {pos.x():.0f}, {pos.y():.0f}")
           super().mousePressEvent(event)
   
   
   class MainWindow(QWidget):
       def __init__(self):
           super().__init__()
           self.setWindowTitle("Mouse Position on QPushButton")
           self.resize(300, 200)
   
           layout = QVBoxLayout()
   
           # Label to show position
           self.position_label = QLabel("Click a button to see position")
           layout.addWidget(self.position_label)
   
           # Button using QCursor method
           self.cursor_button = QPushButton("Cursor Position Method")
           self.cursor_button.clicked.connect(self.show_cursor_position)
           layout.addWidget(self.cursor_button)
   
           # Button using subclass method
           self.subclass_button = CustomButton("Subclass Method")
           self.subclass_button.position_label = self.position_label
           layout.addWidget(self.subclass_button)
   
           self.setLayout(layout)
   
       def show_cursor_position(self):
           pos = self.cursor_button.mapFromGlobal(QCursor.pos())
           self.position_label.setText(f"Cursor method: {pos.x()}, {pos.y()}")
   
   
   if __name__ == "__main__":
       app = QApplication(sys.argv)
       window = MainWindow()
       window.show()
       app.exec()
   ```



## Core Event Handling Mechanism

### 1. Subclassing Widgets

Create custom widget classes that inherit from PyQt6 widgets (e.g., `QPushButton`, `QMainWindow`) and override specific
event handlers:

```python
class CustomButton(QPushButton):
    def mousePressEvent(self, event):  # Override mouse press
        pos = event.position()
        print(f"Clicked at: {pos.x()}, {pos.y()}")
        super().mousePressEvent(event)  # Maintain default behavior
```

### 2. Accessing Event Details  
 
Use the event object parameter to get interaction details:

- Mouse position via `event.position()`
- Mouse button via `event.button() == Qt.MouseButton.LeftButton`
- Keyboard modifiers via `event.modifiers() & Qt.KeyboardModifier.ShiftModifier`

### 3. Window Close Events

Override `closeEvent` in your main window class ([menu example](../C.%20Menus/06-editor.md)) to intercept closure 
attempts:

```python
class MainWindow(QMainWindow):
    def closeEvent(self, event):
        print("Window closing attempted")
        event.ignore()  # Optional: prevent closing
        # OR event.accept() to allow closing
```

## Key Implementation Patterns

### Mouse Event Handling  
 
The example above demonstrates two effective approaches:

1. **Subclass Method** (Recommended)
    - Directly override `mousePressEvent` in custom widgets
    - Provides precise control over target elements
    - Shown in your `CustomButton` class

2. **Cursor Position Method**
    - Uses `QCursor.pos()` for global coordinates
    - Less precise for widget-specific interactions

### Event Propagation

When child widgets block events (common with text inputs, see example in the following section):

- Use `installEventFilter()` to intercept events from child widgets
- Set `setMouseTracking(True)` for continuous mouse movement detection
- Ensure focus policies are configured correctly

## Best Practices

1. **Chain to Parent Class**  
   Always call `super().eventHandler(event)` unless explicitly blocking default behavior
2. **Event Acceptance**  
   Use `event.accept()`/`event.ignore()` to control event propagation
3. **Multiple Buttons**  
   Handle different mouse buttons using Qt namespace constants:
   ```python
   if event.button() == Qt.MouseButton.RightButton:
       handle_right_click()
   ```


??? note "References"

     - [1] https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/
     - [2] https://forum.qt.io/topic/104050/qt-close-event-with-python-issue
     - [3] https://stackoverflow.com/questions/77613516/pyqt6-qplaintextedit-mouse-click-event
     - [4] https://en.ittrip.xyz/python/pyqt-event-signal-guide
     - [5] https://www.learnqt.guide/working-with-events
     - [6] https://stackoverflow.com/questions/38838354/how-to-override-event-dropevent-of-a-widget-in-dynamic-ui-of-pyqt
     - [7] https://doc.qt.io/qtforpython-6.6/overviews/eventsandfilters.html
     - [8] https://www.youtube.com/watch?v=N2JfygnWJaA
     - [9] https://www.youtube.com/watch?v=8drZhYQSI34
     - [10] https://www.pythonguis.com/tutorials/custom-title-bar-pyqt6/



---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.