# 2. List with MVC

Here is a very simple example of the MVC (Model-View-Controller) pattern in PyQt6, adapted from the model/view
architecture described in the references[1][4]. This example uses a list of tasks (a simple to-do list) as the data
model, a `QListView` as the view, and a controller method to add tasks.

```python
import sys
from PyQt6.QtCore import Qt, QAbstractListModel, QModelIndex
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QListView, QLineEdit
)


# --- Model ---
class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.todos[index.row()]
        return None

    def rowCount(self, index):
        return len(self.todos)

    def addTodo(self, todo):
        self.beginInsertRows(
            QModelIndex(), self.rowCount(None), self.rowCount(None)
        )
        self.todos.append(todo)
        self.endInsertRows()


# --- View + Controller ---
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple MVC To-Do")

        # Model
        self.model = TodoModel()

        # View
        self.list_view = QListView()
        self.list_view.setModel(self.model)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Add a new task...")

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)  # Controller action

        layout = QVBoxLayout()
        layout.addWidget(self.list_view)
        layout.addWidget(self.input)
        layout.addWidget(self.add_button)
        self.setLayout(layout)

    # --- Controller logic ---
    def add_task(self):
        text = self.input.text()
        if text:
            self.model.addTodo(text)
            self.input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

**How it works:**

- The **Model** (`TodoModel`) manages the data and notifies the view when it changes.
- The **View** (`QListView`) displays the data from the model.
- The **Controller** logic is in the `add_task` method, which updates the model when the user adds a new task.

This structure keeps data, presentation, and logic separate, which is the essence of MVC in PyQt6[1][4].

??? note "References"
    - [1] https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/
    - [2] https://www.pythonguis.com/pyqt6-tutorial/
    - [3] https://stackoverflow.com/questions/26698628/mvc-design-with-qt-designer-and-pyqt-pyside
    - [4] https://www.pythontutorial.net/pyqt/pyqt-model-view/
    - [5] https://realpython.com/python-pyqt-gui-calculator/
    - [6] https://doc.qt.io/qt-6/modelview.html
    - [7] https://python-forum.io/thread-40616.html
    - [8] https://stackoverflow.com/questions/74252245/pyqt6-create-a-bar-with-minimum-features-on-minimizing-the-window/74256372
    - [9] https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_model_view_controller.htm
    - [10] https://github.com/phume03/PyCal

## Deleting a task

Here's the modified code with **delete functionality** added, along with necessary fixes to ensure proper model
behavior:

```python
import sys
from PyQt6.QtCore import Qt, QAbstractListModel, QModelIndex
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QListView, QLineEdit
)


# --- Model ---
class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole and index.isValid():
            return self.todos[index.row()]
        return None

    def rowCount(self, parent=QModelIndex()):
        # For flat lists, return 0 if parent is valid
        if parent.isValid():
            return 0
        return len(self.todos)

    def addTodo(self, todo):
        row = self.rowCount()
        self.beginInsertRows(QModelIndex(), row, row)
        self.todos.append(todo)
        self.endInsertRows()

    def removeTodo(self, row):
        if 0 <= row < self.rowCount():
            self.beginRemoveRows(QModelIndex(), row, row)
            del self.todos[row]
            self.endRemoveRows()


# --- View + Controller ---
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple MVC To-Do")

        # Model
        self.model = TodoModel(["Buy milk", "Write code"])

        # View
        self.list_view = QListView()
        self.list_view.setModel(self.model)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Add a new task...")

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)

        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.clicked.connect(self.delete_task)

        layout = QVBoxLayout()
        layout.addWidget(self.list_view)
        layout.addWidget(self.input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        self.setLayout(layout)

    # --- Controller logic ---
    def add_task(self):
        text = self.input.text()
        if text:
            self.model.addTodo(text)
            self.input.clear()

    def delete_task(self):
        selected = self.list_view.selectionModel().selectedIndexes()
        if selected:
            row = selected[0].row()  # Get first selected item's row
            self.model.removeTodo(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

**Key Additions:**

1. **Delete Button**: Added a "Delete Selected" button to the UI
2. **Model.removeTodo()**: New method in `TodoModel` to safely remove items using `beginRemoveRows/endRemoveRows`
3. **Selection Handling**: In `delete_task()`, we check which item is selected in the list view and delete its
   corresponding row in the model

**How to Use:**

1. Select an item in the list by clicking it
2. Click "Delete Selected" to remove it
3. Add new items using the text field and "Add Task" button

**Behavior:**

- The model automatically notifies the view about changes
- Invalid selections (no item selected) are ignored
- Works with multiple selection if enabled (though this implementation deletes only the first selected item)

## Saving/loading task lists

Here’s the modified version with **load/save functionality** and side-by-side buttons above the task list:

```python
import sys
from PyQt6.QtCore import Qt, QAbstractListModel, QModelIndex
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListView, QLineEdit, QFileDialog
)


# --- Model ---
class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole and index.isValid():
            return self.todos[index.row()]
        return None

    def rowCount(self, parent=QModelIndex()):
        # For flat lists, return 0 if parent is valid
        if parent.isValid():
            return 0
        return len(self.todos)

    def addTodo(self, todo):
        self.beginInsertRows(
            QModelIndex(), self.rowCount(), self.rowCount()
        )
        self.todos.append(todo)
        self.endInsertRows()

    def removeTodo(self, row):
        if 0 <= row < self.rowCount():
            self.beginRemoveRows(QModelIndex(), row, row)
            del self.todos[row]
            self.endRemoveRows()

    def setTodos(self, todos):
        # Reset model data entirely
        self.beginResetModel()
        self.todos = todos
        self.endResetModel()


# --- View + Controller ---
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List with Load/Save")

        # Model
        self.model = TodoModel(["Buy milk", "Write code"])

        # View Components
        self.list_view = QListView()
        self.list_view.setModel(self.model)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Add a new task...")

        # Buttons
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)

        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.clicked.connect(self.delete_task)

        self.load_button = QPushButton("Load Tasks")
        self.load_button.clicked.connect(self.load_tasks)

        self.save_button = QPushButton("Save Tasks")
        self.save_button.clicked.connect(self.save_tasks)

        # Layouts
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.save_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)  # Load/Save buttons at top
        main_layout.addWidget(self.list_view)
        main_layout.addWidget(self.input)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.delete_button)
        self.setLayout(main_layout)

    # --- Controller Logic ---
    def add_task(self):
        text = self.input.text()
        if text:
            self.model.addTodo(text)
            self.input.clear()

    def delete_task(self):
        selected = self.list_view.selectionModel().selectedIndexes()
        if selected:
            row = selected[0].row()
            self.model.removeTodo(row)

    def load_tasks(self):
        filepath, _ = QFileDialog.getOpenFileName(
            self, "Open Task File", "", "Text Files (*.txt)"
        )
        if filepath:
            with open(filepath, "r") as f:
                tasks = [line.strip() for line in f if line.strip()]
            self.model.setTodos(tasks)

    def save_tasks(self):
        filepath, _ = QFileDialog.getSaveFileName(
            self, "Save Task File", "", "Text Files (*.txt)"
        )
        if filepath:
            with open(filepath, "w") as f:
                for task in self.model.todos:
                    f.write(f"{task}\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

**Key Changes:**

1. Added `Load Tasks` and `Save Tasks` buttons in a horizontal layout above the list.
2. Implemented `setTodos()` in the model to reset data (using `beginResetModel/endResetModel`).
3. Added file dialog handling for loading/saving plain text files.
4. Fixed `rowCount()` signature and added parent index check for PyQt6 compliance.

**File Format Example** (`tasks.txt`):

```
Buy groceries
Finish homework
Call mom
```

**Usage:**

- Click **Load Tasks** to import tasks from a `.txt` file (one task per line).
- Click **Save Tasks** to export the current list to a `.txt` file.

------

## Would it be better to put the read/write logic in the model ?

It is generally **better to keep the file read/write logic in the controller (or MainWindow), not the model**, according
to both Qt/PyQt conventions and the MVC pattern as applied in GUI applications[1][2][5].

## Rationale

- **Model Responsibility:** In Qt's Model/View architecture (and classic MVC), the model's job is to manage and expose
  the *current in-memory data* and notify views of changes[1][5]. The model should not be concerned with *how* the data
  is persisted-whether that's a file, a database, or some other storage. This keeps the model focused and testable.
- **Controller Responsibility:** The controller (in PyQt, often the MainWindow or a dedicated controller class) is
  responsible for orchestrating application logic, including loading data from and saving data to persistent
  storage[2][5]. The controller tells the model to update its data, and the model notifies the view.
- **Separation of Concerns:** Keeping file I/O in the controller allows you to change the storage method (e.g., from a
  text file to a database) without changing your model, making your codebase more maintainable and flexible[2].

## PyQt Community Practice

- In many PyQt tutorials and real-world apps, the file loading/saving logic is implemented in the MainWindow/controller,
  which then updates the model using methods like `setTodos()` or directly modifying the model's internal data[1].
- The model should provide a clean API for updating its data (e.g., `setTodos(tasks)`), but not handle file dialogs or
  file I/O itself.

## Example (from your earlier code)

**Best practice:**

- The controller (MainWindow) opens the file, reads the tasks, and calls `model.setTodos(tasks)`.
- To save, the controller gets the data from the model (`model.todos`) and writes it to the file.

## Summary Table

| Task              | Best Location | Why                                                          |
|-------------------|---------------|--------------------------------------------------------------|
| In-memory data    | Model         | Model manages, exposes, and notifies about data changes      |
| File I/O          | Controller    | Controller manages persistence, keeps model storage-agnostic |
| Data presentation | View          | View displays model data                                     |


**In summary:**  

Keep file reading and writing in the controller, not the model. The model should only manage the in-memory data and
expose methods for updating it. This keeps your application modular and easier to maintain.

??? note "References"
    - [1] https://www.pythonguis.com/tutorials/modelview-architecture/
    - [2] https://softwareengineering.stackexchange.com/questions/293388/where-in-an-mvc-web-application-should-writing-files-locally-go
    - [3] https://stackoverflow.com/questions/1660474/pyqt-and-mvc-pattern
    - [4] https://www.reddit.com/r/learnpython/comments/egf9ir/question_about_mvc_architecture_on_pyqt5/
    - [5] https://stackoverflow.com/questions/26698628/mvc-design-with-qt-designer-and-pyqt-pyside
    - [6] https://softwareengineering.stackexchange.com/questions/331246/how-to-decouple-ui-from-logic-on-pyqt-qt-apps-properly
    - [7] https://realpython.com/lego-model-view-controller-python/
    - [8] https://github.com/SihabSahariar/PyQt5-MVC-Template
    - [9] https://www.pythontutorial.net/pyqt/pyqt-model-view/
    - [10] https://realpython.com/python-pyqt-gui-calculator/


---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.