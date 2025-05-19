# 2. Example: Event Propagation and Bubbling in PyQt6

When you interact with widgets in a PyQt6 application, events (like mouse clicks) are first delivered to the widget
under the cursor. If that widget does not fully handle the event (i.e., it calls `event.ignore()`), the event is then "
bubbled up" to its parent widget, and so on, until it is handled or reaches the top-level window[1][6][9].

Below is a concise example that demonstrates this propagation using custom widgets and the `event()` method. The child
widget will print a message and ignore the event, allowing the parent to also respond:

```python
import sys
from PyQt6.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import QEvent


class ChildButton(QPushButton):
    def event(self, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print("ChildButton: MouseButtonPress event (ignored, propagates up)")
            event.ignore()  # Let the event propagate to parent
            return False
        return super().event(event)


class MainFrame(QFrame):
    def event(self, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print("MainFrame: MouseButtonPress event (received from child)")
        return super().event(event)


app = QApplication(sys.argv)
main_frame = MainFrame()
main_frame.setWindowTitle("Event Propagation Demo")
layout = QVBoxLayout(main_frame)

label = QLabel("Click the button below")
layout.addWidget(label)

button = ChildButton("Click Me")
layout.addWidget(button)

main_frame.setLayout(layout)
main_frame.show()
app.exec()
```

### What Happens Here?

- When you click the button, the `ChildButton`'s `event()` method is called first.
- It prints a message and calls `event.ignore()`, which allows the event to propagate up to the parent (`MainFrame`).
- The `MainFrame`'s `event()` method then receives the same event and prints its own message[1][2][9].

### Key Points

- **Accepting an event** (`event.accept()`) stops propagation.
- **Ignoring an event** (`event.ignore()`) allows it to bubble up to parent widgets.
- This pattern is essential for custom widgets that should sometimes defer event handling to their parent or to
  implement global event monitoring[1][6][9].

This example demonstrates how you can control event propagation in PyQt6 by choosing whether to accept or ignore events
in your widget's event handler methods.

??? note "References"

    - [1] https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/
    - [2] https://stackoverflow.com/questions/76857798/qt-event-is-not-propagating-from-child-to-parent
    - [3] https://zetcode.com/pyqt6/eventssignals/
    - [4] https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/
    - [5] https://www.tutorialspoint.com/pyqt/pyqt_event_handling.htm
    - [6] https://doc.qt.io/qtforpython-6.6/overviews/eventsandfilters.html
    - [7] https://www.youtube.com/watch?v=N2JfygnWJaA
    - [8] https://pyqtgraph.readthedocs.io/en/latest/qtcrashcourse.html
    - [9] https://doc.qt.io/qtforpython-6/PySide6/QtCore/QEvent.html
    - [10] https://www.reddit.com/r/learnpython/comments/1g31ffz/pyqt6_detecting_mouse_movement_with/

## What happens if a widget doesn't have a parent widget?

When an event is ignored (using `event.ignore()`) in a widget without a parent (a top-level window), the event **does
not disappear** but instead propagates to the **application-level event loop** for potential handling. Here's the
breakdown:

1. **No Parent Propagation**  
   Since the widget has no parent, there's no hierarchy to "bubble up" through. The event exits the widget's scope but
   remains in the application's processing queue.

2. **Application-Level Handling**  
   Qt's event loop may still process the event through:
    - Global event filters (`QApplication.instance().installEventFilter()`)
    - Default platform behavior (e.g., window manager actions for close events)
    - Other application-wide handlers

3. **Key Example: Window Close Events**  
   For a top-level window ignoring `closeEvent`:
   ```python
   class MainWindow(QMainWindow):
       def closeEvent(self, event):
           event.ignore()  # Window remains open
   ```
   The close request is ignored by the window but still reaches the application, which respects the `ignore()` call by
   not terminating.

**Critical Implications**

- Ignored events in parentless widgets *can* still trigger application-level behavior if not explicitly blocked
- Use `event.accept()`/`event.ignore()` strategically even in top-level windows to control default Qt behaviors[1][5]

??? note "References"
     - [1] https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/
     - [2] https://stackoverflow.com/questions/13788452/pyqt-how-to-handle-event-without-inheritance
     - [3] https://doc.qt.io/qtforpython-6.8/PySide6/QtWidgets/QWidget.html
     - [4] https://python-forum.io/thread-22877.html
     - [5] https://doc.qt.io/qt-6/qwidget.html
     - [6] https://zetcode.com/pyqt6/firstprograms/
     - [7] https://www.pythonguis.com/tutorials/pyqt6-creating-your-own-custom-widgets/
     - [8] https://www.youtube.com/watch?v=N2JfygnWJaA
     - [9] https://www.youtube.com/watch?v=Cc_zaUbF4LM
     - [10] https://www.qtcentre.org/threads/6313-Handling-Mouse-Events-of-a-parent-widget


## Global event handling

Using `QApplication.instance().installEventFilter()` allows you to monitor or intercept **all events in your
application**, not just those for a specific widget. This is especially useful for implementing global shortcuts,
accessibility features or custom event handling that should apply everywhere.

### Example: Blocking All Keyboard Input to Text Inputs Except '0' and '1'

Suppose you want to restrict every text input (`QLineEdit`, `QTextEdit`, etc.) in your application so that users can
only type the digits '0' and '1', regardless of which input widget is focused. Instead of subclassing every input
widget, you can install a single global event filter on the application object.

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
from PyQt6.QtCore import QObject, QEvent


class BinaryInputFilter(QObject):
    def eventFilter(self, obj, event):
        # Filter key presses for all widgets
        if event.type() == QEvent.Type.KeyPress:
            # Only filter QLineEdit widgets
            if isinstance(obj, QLineEdit):
                text = event.text()
                if text and text not in ('0', '1'):
                    # Block the event (do not let it reach the widget)
                    return True
        # Allow normal processing
        return False


app = QApplication(sys.argv)

# Install the filter on the application instance
binary_filter = BinaryInputFilter()
app.installEventFilter(binary_filter)

window = QWidget()
layout = QVBoxLayout(window)
layout.addWidget(QLabel("Only '0' and '1' allowed:"))
layout.addWidget(QLineEdit())
layout.addWidget(QLineEdit())
window.show()

app.exec()
```

#### How it works

- The `BinaryInputFilter` class checks every key press event for all widgets in the app.
- If the event is for a `QLineEdit` and the key is not '0' or '1', the event is blocked (`return True`), so the
  character never appears in the input.
- All other events are passed through normally (`return False`).

**This approach is powerful but should be used with care, as it affects the entire application and may have performance
implications if overused**[3][4].

---

!!! info "Global event filter: `installEventFilter`"
      This method is directly related to situations where you want to monitor or modify the behavior of events across many
      widgets, such as text inputs, without subclassing each one or worrying about event propagation between parent and child
      widgets. The global event filter sees the event *before* it reaches any widget, making it ideal for enforcing
      application-wide rules or behaviors[3][4].

??? note "References"

     - [1] https://stackoverflow.com/questions/57534440/how-to-correctly-attach-an-eventfilter-with-installeventfilter-to-a-qtwidget
     - [2] https://www.qtcentre.org/threads/24678-QPlainTextEdit-and-input-filtering
     - [3] https://doc.qt.io/qt-6/eventsandfilters.html
     - [4] https://doc.qt.io/qtforpython-6.6/overviews/eventsandfilters.html
     - [5] https://doc.qt.io/qtforpython-6/PySide6/QtCore/QCoreApplication.html
     - [6] https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
     - [7] https://www.pythonguis.com/tutorials/multithreading-pyqt6-applications-qthreadpool/
     - [8] https://stackoverflow.com/questions/76857798/qt-event-is-not-propagating-from-child-to-parent
     - [9] https://www.e-education.psu.edu/geog489/book/export/html/1871
     - [10] https://stackoverflow.com/questions/4827207/how-do-i-filter-the-pyqt-qcombobox-items-based-on-the-text-input


---------------

??? info "Use of AI"
      Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
      explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
      the author.