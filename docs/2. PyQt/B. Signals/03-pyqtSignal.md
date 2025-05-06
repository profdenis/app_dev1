# 3. Defining and using custom signal

## What is `pyqtSignal` and How Do You Use It?

**`pyqtSignal`** is used in PyQt6 to define custom signals that your objects can emit. Signals are a core part of Qt's
event-driven architecture, enabling communication between objects. You use them to notify other parts of your
application when something happens-such as a value changing, a task completing, or a user action occurring.

### When and Why to Use `pyqtSignal`

- Use `pyqtSignal` when you want your custom class (typically a subclass of `QObject`) to notify other objects about
  events or state changes.
- This is especially useful for decoupling: the object emitting the signal doesn't need to know who receives it.

### How to Define and Use a Custom Signal

#### 1. Define the Signal as a Class Attribute

Signals must be defined as class attributes in a subclass of `QObject`:

```python
from PyQt6.QtCore import QObject, pyqtSignal


class Counter(QObject):
    # Define a signal that emits an integer
    valueChanged = pyqtSignal(int)
```

#### 2. Connect the Signal to a Slot

A slot is any callable (function or method) that should respond to the signal:

```python
def print_value(value):
    print(f"Counter value: {value}")


counter = Counter()
counter.valueChanged.connect(print_value)
```

#### 3. Emit the Signal

When your object wants to notify others, it calls `.emit()` on the signal:

```python
counter.valueChanged.emit(42)  # This will call print_value(42)
```

#### 4. Putting It All Together: A Minimal Example

```python
from PyQt6.QtCore import QObject, pyqtSignal


class Counter(QObject):
    valueChanged = pyqtSignal(int)  # Define a custom signal

    def __init__(self):
        super().__init__()
        self._value = 0

    def increment(self):
        self._value += 1
        self.valueChanged.emit(self._value)  # Emit the signal


def handle_value(value):
    print(f"Counter value: {value}")


counter = Counter()
counter.valueChanged.connect(handle_value)
counter.increment()  # Output: Counter value: 1
```

### Key Points

- **Define** signals as class attributes using `pyqtSignal`.
- **Connect** signals to slots (functions/methods) using `.connect()`.
- **Emit** the signal with `.emit()` to notify all connected slots.
- Signals can carry arguments, and you can define their types (e.g., `pyqtSignal(int, str)`).
- Use custom signals to implement clean, decoupled communication between objects in your PyQt application[1][2][3][4].

### When to Use

- When you want your object to notify other parts of your program about something that happened, without hard-coding
  those relationships.
- Example: A data model emits a signal when its data changes, and a view updates itself in response.

---

!!! info "In summary" 

    `pyqtSignal` lets you define events that your objects can emit. Other objects can "listen" for these events by
    connecting slots to the signal. This is a fundamental way to structure event-driven, interactive applications in PyQt.

??? note "References"
    - [1] https://stackoverflow.com/questions/36434706/pyqt-proper-use-of-emit-and-pyqtsignal
    - [2] https://doc.bccnsoft.com/docs/PyQt5/signals_slots.html
    - [3] https://www.tutorialspoint.com/pyqt/pyqt_new_signals_with_pyqtsignal.htm
    - [4] https://www.w3resource.com/python-exercises/pyqt/python-pyqt-connecting-signals-to-slots-exercise-7.php
    - [5] https://www.tutorialspoint.com/pyqt/pyqt_signals_and_slots.htm
    - [6] https://doc.qt.io/qtforpython-5/PySide2/QtCore/Signal.html
    - [7] https://stackoverflow.com/questions/3891465/how-to-connect-pyqtsignal-between-classes-in-pyqt
    - [8] https://doc.qt.io/qtforpython-6/tutorials/basictutorial/signals_and_slots.html
    - [9] https://www.reddit.com/r/Python/comments/11ks1hl/pyqt_signal_tricks/
    - [10] https://www.youtube.com/watch?v=LfztdwaGOjs
    - [11] https://www.youtube.com/watch?v=3t8KhIdSGYQ
    - [12] https://forum.qt.io/topic/128626/sending-qwidgets-as-a-pyqtsignal
    - [13] https://www.linkedin.com/pulse/how-handle-widget-events-using-pyqt-signal-slot-mechanism-garcia
    - [14] https://wiki.qt.io/Qt_for_Python_Signals_and_Slots
    - [15] https://blog.manash.io/quick-pyqt5-1-signal-and-slot-example-in-pyqt5-bf502ccaf11d
    - [16] https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/
    - [17] https://stackoverflow.com/questions/36462003/pyqt5-signal-slot-decorator-example
    - [18] https://www.qtcentre.org/threads/70973-Proper-PyQt5-signal-amp-slot-syntax


---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.