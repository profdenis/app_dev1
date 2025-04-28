# 2. Example with a slider and a dial

Here's a PyQt6 example with a slider, dial, and label that stay synchronized (values 1-10):

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QDial, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


class LinkedControlsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create controls with range 1-10
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.dial = QDial()
        self.label = QLabel("Value: 1")

        # Set ranges
        self.slider.setRange(1, 10)
        self.dial.setRange(1, 10)

        # Add to layout
        layout.addWidget(self.slider)
        layout.addWidget(self.dial)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Connect signals with loop prevention
        self.slider.valueChanged.connect(self.update_controls)
        self.dial.valueChanged.connect(self.update_controls)

    def update_controls(self, value):
        # Prevent signal loops
        sender = self.sender()

        if isinstance(sender, QSlider):
            widget = self.dial 
        else:
            widget = self.slider

        widget.blockSignals(True)
        widget.setValue(value)
        widget.blockSignals(False)
        
        self.label.setText(f"Value: {value}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinkedControlsApp()
    window.setWindowTitle("Linked Controls Demo")
    window.show()
    sys.exit(app.exec())
```

![slider.png](slider.png)

**Key Features:**

1. **Synchronized Controls** (`QSlider` and `QDial`):
    - Moving either control updates the other instantly[4]
    - `blockSignals()` prevents infinite update loops[4]

2. **Value Display** (`QLabel`):
    - Automatically shows current value (1-10)
    - Updates on any control change

3. **Range Management**:
    - Both controls restricted to 1-10 using `setRange()`
    - Integer-only values by default

**Usage:**

- Slide the horizontal slider or rotate the dial
- Both controls and label will stay synchronized
- Values wrap automatically between 1 and 10

This demonstrates PyQt6's signal/slot mechanism while handling common synchronization challenges in GUI
development[1][4].

??? note "References"
     - [1] https://www.w3resource.com/python-exercises/pyqt/python-pyqt-connecting-signals-to-slots-exercise-10.php
     - [2] https://forum.qt.io/topic/44417/placing-a-label-next-to-a-slider-handle
     - [3] https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QRadioButton.html
     - [4] https://stackoverflow.com/questions/75156906/how-to-make-a-slider-which-has-a-label-can-show-above-the-handle-with-pyside2
     - [5] https://www.youtube.com/watch?v=Adg2zQaAF-g
     - [6] https://stackoverflow.com/questions/76745611/pyqt6-slider-not-moving
     - [7] https://stackoverflow.com/questions/43251692/how-to-make-button-like-radiobuttons-in-pyqt
     - [8] https://forum.qt.io/topic/159776/accessibility-issue-with-radio-buttons-in-pyqt6-setting
     - [9] https://www.reddit.com/r/Python/comments/wedvzi/what_is_the_best_gui_library_for_python/
     - [10] https://stackoverflow.com/questions/53532276/how-to-display-the-range-values-in-slider
     - [11] https://www.qtcentre.org/threads/3904-array-of-radio-buttons
     - [12] https://www.pythonguis.com/tutorials/pyqt6-widgets/
     - [13] https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QSlider.html
     - [14] https://www.pythonguis.com/tutorials/pyside6-widgets/
     - [15] https://forum.qt.io/topic/22609/qslider-needs-to-step-with-custom-step-value-on-mouse-slide
     - [16] https://coderslegacy.com/python/pyqt6-qradiobutton/
     - [17] https://pysdr.org/content/pyqt.html
     - [18] https://www.youtube.com/watch?v=DZ3-ij_JHE0
     - [19] https://stackoverflow.com/questions/68931326/how-switch-between-two-graphs-and-maintain-radio-button-and-slider-updates-worki
     - [20] https://stackoverflow.com/questions/47494941/python-pyqt4-qslider-interval-bigger-than-1
   

---------------

??? info "Use of AI"
        Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
        explanations, examples and/or structure suggestions. All information has been verified, edited and completed by 
        the author.