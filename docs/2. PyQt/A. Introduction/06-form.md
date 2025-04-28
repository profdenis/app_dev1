# 6. Form Layout

Here is a complete example of a PyQt6 form for entering a new "Person" object, using `QFormLayout` and including fields
for first name, last name, email, date of birth, student status (checkbox), and several other attributes. This example
follows best practices as described here[2][4]:

```python
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QFormLayout, QLineEdit,
    QDateEdit, QCheckBox, QComboBox, QSpinBox, QPushButton
)
from PyQt6.QtCore import QDate


class PersonForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Person Entry Form")

        # Create the form layout
        layout = QFormLayout()

        # First name
        self.first_name_edit = QLineEdit()
        layout.addRow("First Name:", self.first_name_edit)

        # Last name
        self.last_name_edit = QLineEdit()
        layout.addRow("Last Name:", self.last_name_edit)

        # Email
        self.email_edit = QLineEdit()
        layout.addRow("Email:", self.email_edit)

        # Date of Birth
        self.dob_edit = QDateEdit()
        self.dob_edit.setCalendarPopup(True)
        self.dob_edit.setDate(QDate.currentDate())
        layout.addRow("Date of Birth:", self.dob_edit)

        # Student (checkbox)
        self.student_checkbox = QCheckBox("Is a student")
        layout.addRow("Student:", self.student_checkbox)

        # Gender (combobox)
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Select...", "Female", "Male", "Other"])
        layout.addRow("Gender:", self.gender_combo)

        # Age (spinbox)
        self.age_spin = QSpinBox()
        self.age_spin.setRange(0, 120)
        layout.addRow("Age:", self.age_spin)

        # Country (combobox)
        self.country_combo = QComboBox()
        self.country_combo.addItems(["Select...", "Canada", "USA", "Other"])
        layout.addRow("Country:", self.country_combo)

        # Add a submit button at the end
        self.submit_button = QPushButton("Submit")
        layout.addRow(self.submit_button)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PersonForm()
    window.show()
    sys.exit(app.exec())
```

![img.png](form.png)

**Features:**

- Uses `QFormLayout` for a clean, two-column form[2][4].
- Each row pairs a label with an input widget.
- Includes line edits, date picker, checkbox, combo boxes, and spin box for a realistic "Person" entry form.
- A submit button is provided at the bottom.

You can easily add or remove attributes by following the same pattern with `layout.addRow(label, widget)`. This form is
responsive and follows platform look-and-feel standards[2][4].

??? note "References"
      - [1] https://www.youtube.com/watch?v=cLoeJ7UVNno
      - [2] https://www.pythontutorial.net/pyqt/pyqt-qformlayout/
      - [3] https://www.youtube.com/watch?v=DM8Ryoot7MI
      - [4] https://www.tutorialspoint.com/pyqt/pyqt_qformlayout_class.htm
      - [5] https://www.youtube.com/watch?v=Cc_zaUbF4LM
      - [6] https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFormLayout.html
      - [7] https://doc.qt.io/qt-6/qformlayout.html
      - [8] https://realpython.com/python-pyqt-layout/
      - [9] https://doc-snapshots.qt.io/qtforpython-6.8/PySide6/QtWidgets/QFormLayout.html
      - [10] https://www.pythonguis.com/tutorials/pyqt6-widgets/
      - [11] https://www.pythonguis.com/tutorials/pyqt6-qt-designer-gui-layout/
      - [12] https://forum.qt.io/topic/4750/how-to-properly-handle-user-input-with-multiple-fields
      - [13] https://stackoverflow.com/questions/5219946/how-do-i-create-a-tree-view-with-checkbox-inside-a-combo-box-pyqt/5291844
      - [14] https://realpython.com/python-pyqt-gui-calculator/
      - [15] https://www.qtcentre.org/threads/8247-Suggestions-for-checkbox-form-layout
      - [16] https://www.pythonguis.com/tutorials/pyqt6-layouts/
      - [17] https://www.youtube.com/watch?v=h-gpcoiEVe4
      - [18] https://stackoverflow.com/questions/59418762/hwo-to-implement-qformlayout-with-multiple-rows-and-columns
      - [19] https://stackoverflow.com/questions/72665404/checkbox-in-qtableview-pyqt6
      - [20] https://stackoverflow.com/questions/26552108/setting-up-the-form-layout-in-correct-way-qgridlayout-addlayoutqlayout-int-i

---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by the
    author.
