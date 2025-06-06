#!/usr/bin/env python3
"""
PyQt6 REST API CRUD Application - Approach 4
Refactored with helper methods for common UI patterns.
This version demonstrates how to eliminate code duplication with reusable helper methods.
"""

import sys
import json
import requests
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                             QWidget, QPushButton, QLineEdit, QTextEdit, QLabel,
                             QGroupBox, QMessageBox, QProgressBar)
from PyQt6.QtCore import QThread, pyqtSignal, QObject
from PyQt6.QtGui import QFont


class ApiWorker(QThread):
    """Worker thread for API operations to prevent UI freezing"""

    # Class-level mapping of operations to method names
    OPERATION_METHODS = {
        "create": "_create_post",
        "read": "_read_post",
        "update": "_update_post",
        "delete": "_delete_post",
        "read_all": "_read_all_posts"
    }

    # Signals to communicate with main thread
    operation_finished = pyqtSignal(bool, str, dict)  # success, message, data
    operation_started = pyqtSignal(str)  # operation description

    def __init__(self):
        super().__init__()
        self.base_url = "https://jsonplaceholder.typicode.com/posts"
        self.operation_method = None
        self.data = None

    def set_operation(self, operation, **kwargs):
        """Set the operation to perform and its parameters"""
        # Get method name from class-level mapping
        method_name = self.OPERATION_METHODS.get(operation)
        if not method_name:
            raise ValueError(f"Unknown operation: {operation}. Available: {list(self.OPERATION_METHODS.keys())}")

        # Get the actual method reference
        self.operation_method = getattr(self, method_name)
        self.data = kwargs

    def run(self):
        """Execute the API operation in the background thread"""
        try:
            # Simply call the method that was set in set_operation
            self.operation_method()
        except requests.exceptions.RequestException as e:
            self.operation_finished.emit(False, f"Network error: {str(e)}", {})
        except Exception as e:
            self.operation_finished.emit(False, f"Unexpected error: {str(e)}", {})

    def _create_post(self):
        """Create a new post"""
        self.operation_started.emit("Creating new post...")

        post_data = {
            "title": self.data["title"],
            "body": self.data["body"],
            "userId": int(self.data["user_id"])
        }

        response = requests.post(self.base_url, json=post_data, timeout=10)

        if response.status_code == 201:
            result = response.json()
            message = f"Post created successfully with ID: {result['id']}"
            self.operation_finished.emit(True, message, result)
        else:
            self.operation_finished.emit(False, f"Failed to create post. Status: {response.status_code}", {})

    def _read_post(self):
        """Read a specific post"""
        post_id = self.data["post_id"]
        self.operation_started.emit(f"Reading post {post_id}...")

        url = f"{self.base_url}/{post_id}"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            result = response.json()
            message = f"Post {post_id} retrieved successfully"
            self.operation_finished.emit(True, message, result)
        elif response.status_code == 404:
            self.operation_finished.emit(False, f"Post {post_id} not found", {})
        else:
            self.operation_finished.emit(False, f"Failed to read post. Status: {response.status_code}", {})

    def _update_post(self):
        """Update an existing post"""
        post_id = self.data["post_id"]
        self.operation_started.emit(f"Updating post {post_id}...")

        post_data = {
            "id": int(post_id),
            "title": self.data["title"],
            "body": self.data["body"],
            "userId": int(self.data["user_id"])
        }

        url = f"{self.base_url}/{post_id}"
        response = requests.put(url, json=post_data, timeout=10)

        if response.status_code == 200:
            result = response.json()
            message = f"Post {post_id} updated successfully"
            self.operation_finished.emit(True, message, result)
        else:
            self.operation_finished.emit(False, f"Failed to update post. Status: {response.status_code}", {})

    def _delete_post(self):
        """Delete a post"""
        post_id = self.data["post_id"]
        self.operation_started.emit(f"Deleting post {post_id}...")

        url = f"{self.base_url}/{post_id}"
        response = requests.delete(url, timeout=10)

        if response.status_code == 200:
            message = f"Post {post_id} deleted successfully"
            self.operation_finished.emit(True, message, {"id": post_id})
        else:
            self.operation_finished.emit(False, f"Failed to delete post. Status: {response.status_code}", {})

    def _read_all_posts(self):
        """Read all posts (limited to first 10 for demo)"""
        self.operation_started.emit("Loading all posts...")

        response = requests.get(self.base_url, timeout=10)

        if response.status_code == 200:
            posts = response.json()[:10]  # Limit to first 10 posts
            message = f"Retrieved {len(posts)} posts"
            self.operation_finished.emit(True, message, {"posts": posts})
        else:
            self.operation_finished.emit(False, f"Failed to load posts. Status: {response.status_code}", {})


class PostCrudApp(QMainWindow):
    """Main application window - Approach 4: Functional decomposition + helper methods"""

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_worker()

    def init_ui(self):
        """Initialize the user interface"""
        self.setup_window()
        main_layout = self.create_main_layout()
        self.add_title_section(main_layout)
        self.add_input_section(main_layout)
        self.add_buttons_section(main_layout)
        self.add_status_section(main_layout)
        self.add_results_section(main_layout)
        self.connect_signals()

    def setup_window(self):
        """Set up main window properties"""
        self.setWindowTitle("REST API CRUD Demo - Post Manager (Approach 4)")
        self.setGeometry(100, 100, 800, 600)

    def create_main_layout(self):
        """Create and set the main layout"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        return QVBoxLayout(central_widget)

    def add_title_section(self, main_layout):
        """Add the title label to the layout"""
        title_label = QLabel("Post Manager - REST API CRUD Operations (Helper Methods Version)")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)
        main_layout.addWidget(title_label)

    def add_input_section(self, main_layout):
        """Add the input fields section - using helper methods to reduce duplication"""
        input_group = self.create_group_box("Post Data")
        input_layout = QVBoxLayout(input_group)

        # Using helper methods for consistent label + input patterns
        self.post_id_input = self.create_labeled_input(
            input_layout,
            "Post ID:",
            "Enter post ID (for read/update/delete)"
        )

        self.title_input = self.create_labeled_input(
            input_layout,
            "Title:",
            "Enter post title"
        )

        self.body_input = self.create_labeled_textedit(
            input_layout,
            "Body:",
            "Enter post content",
            max_height=80
        )

        self.user_id_input = self.create_labeled_input(
            input_layout,
            "User ID:",
            "Enter user ID (default: 1)",
            default_text="1"
        )

        main_layout.addWidget(input_group)

    def add_buttons_section(self, main_layout):
        """Add the operation buttons section - using helper for button creation"""
        buttons_group = self.create_group_box("Operations")
        buttons_layout = QHBoxLayout(buttons_group)

        # Button configurations: (text, attribute_name)
        button_configs = [
            ("Create Post", "create_btn"),
            ("Read Post", "read_btn"),
            ("Update Post", "update_btn"),
            ("Delete Post", "delete_btn"),
            ("Load All Posts", "read_all_btn"),
            ("Clear", "clear_btn")
        ]

        # Create all buttons using helper method
        self.create_buttons(buttons_layout, button_configs)

        main_layout.addWidget(buttons_group)

    def add_status_section(self, main_layout):
        """Add progress bar and status label"""
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        main_layout.addWidget(self.progress_bar)

        # Status label
        self.status_label = QLabel("Ready")
        main_layout.addWidget(self.status_label)

    def add_results_section(self, main_layout):
        """Add the results display section"""
        results_group = self.create_group_box("Results")
        results_layout = QVBoxLayout(results_group)

        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        self.results_text.setPlaceholderText("API operation results will appear here...")
        results_layout.addWidget(self.results_text)

        main_layout.addWidget(results_group)

    def connect_signals(self):
        """Connect button signals to their handlers"""
        self.create_btn.clicked.connect(self.create_post)
        self.read_btn.clicked.connect(self.read_post)
        self.update_btn.clicked.connect(self.update_post)
        self.delete_btn.clicked.connect(self.delete_post)
        self.read_all_btn.clicked.connect(self.read_all_posts)
        self.clear_btn.clicked.connect(self.clear_form)

    # ===== HELPER METHODS - These reduce code duplication =====

    def create_group_box(self, title):
        """Helper: Create a group box with consistent styling"""
        group_box = QGroupBox(title)
        return group_box

    def create_labeled_input(self, parent_layout, label_text, placeholder="", default_text=""):
        """Helper: Create a label + QLineEdit pair in horizontal layout"""
        row_layout = QHBoxLayout()

        # Create label
        label = QLabel(label_text)
        row_layout.addWidget(label)

        # Create input
        input_widget = QLineEdit()
        if placeholder:
            input_widget.setPlaceholderText(placeholder)
        if default_text:
            input_widget.setText(default_text)
        row_layout.addWidget(input_widget)

        # Add to parent layout
        parent_layout.addLayout(row_layout)

        # Return the input widget so caller can store reference
        return input_widget

    def create_labeled_textedit(self, parent_layout, label_text, placeholder="", max_height=None):
        """Helper: Create a label + QTextEdit pair in horizontal layout"""
        row_layout = QHBoxLayout()

        # Create label
        label = QLabel(label_text)
        row_layout.addWidget(label)

        # Create text edit
        text_edit = QTextEdit()
        if placeholder:
            text_edit.setPlaceholderText(placeholder)
        if max_height:
            text_edit.setMaximumHeight(max_height)
        row_layout.addWidget(text_edit)

        # Add to parent layout
        parent_layout.addLayout(row_layout)

        return text_edit

    def create_buttons(self, parent_layout, button_configs):
        """Helper: Create multiple buttons from configuration list"""
        for button_text, attribute_name in button_configs:
            button = QPushButton(button_text)
            parent_layout.addWidget(button)
            # Store button as instance attribute using setattr
            setattr(self, attribute_name, button)

    # ===== BUSINESS LOGIC METHODS - Same as Approach 1 =====

    def init_worker(self):
        """Initialize the worker thread"""
        self.worker = ApiWorker()
        self.worker.operation_started.connect(self.on_operation_started)
        self.worker.operation_finished.connect(self.on_operation_finished)

    def create_post(self):
        """Handle create post button click"""
        if not self.validate_inputs(['title', 'body', 'user_id']):
            return

        self.worker.set_operation(
            "create",
            title=self.title_input.text(),
            body=self.body_input.toPlainText(),
            user_id=self.user_id_input.text()
        )
        self.start_operation()

    def read_post(self):
        """Handle read post button click"""
        if not self.validate_inputs(['post_id']):
            return

        self.worker.set_operation("read", post_id=self.post_id_input.text())
        self.start_operation()

    def update_post(self):
        """Handle update post button click"""
        if not self.validate_inputs(['post_id', 'title', 'body', 'user_id']):
            return

        self.worker.set_operation(
            "update",
            post_id=self.post_id_input.text(),
            title=self.title_input.text(),
            body=self.body_input.toPlainText(),
            user_id=self.user_id_input.text()
        )
        self.start_operation()

    def delete_post(self):
        """Handle delete post button click"""
        if not self.validate_inputs(['post_id']):
            return

        # Confirm deletion
        reply = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete post {self.post_id_input.text()}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.worker.set_operation("delete", post_id=self.post_id_input.text())
            self.start_operation()

    def read_all_posts(self):
        """Handle read all posts button click"""
        self.worker.set_operation("read_all")
        self.start_operation()

    def validate_inputs(self, required_fields):
        """Validate that required fields are filled"""
        errors = []

        if 'post_id' in required_fields and not self.post_id_input.text().strip():
            errors.append("Post ID is required")

        if 'title' in required_fields and not self.title_input.text().strip():
            errors.append("Title is required")

        if 'body' in required_fields and not self.body_input.toPlainText().strip():
            errors.append("Body is required")

        if 'user_id' in required_fields and not self.user_id_input.text().strip():
            errors.append("User ID is required")

        # Validate numeric fields
        if 'post_id' in required_fields:
            try:
                int(self.post_id_input.text())
            except ValueError:
                errors.append("Post ID must be a number")

        if 'user_id' in required_fields:
            try:
                int(self.user_id_input.text())
            except ValueError:
                errors.append("User ID must be a number")

        if errors:
            QMessageBox.warning(self, "Validation Error", "\n".join(errors))
            return False

        return True

    def start_operation(self):
        """Start an API operation"""
        self.set_buttons_enabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)  # Indeterminate progress
        self.worker.start()

    def on_operation_started(self, message):
        """Handle operation started signal"""
        self.status_label.setText(message)

    def on_operation_finished(self, success, message, data):
        """Handle operation finished signal"""
        self.set_buttons_enabled(True)
        self.progress_bar.setVisible(False)
        self.status_label.setText("Ready")

        if success:
            self.display_success(message, data)
        else:
            self.display_error(message)

    def display_success(self, message, data):
        """Display successful operation result"""
        result_text = f"✅ SUCCESS: {message}\n\n"

        if "posts" in data:  # Multiple posts
            result_text += "Posts:\n"
            for post in data["posts"]:
                result_text += f"ID: {post['id']} | Title: {post['title'][:50]}...\n"
        elif data:  # Single post data
            result_text += "Data:\n"
            result_text += json.dumps(data, indent=2)

        self.results_text.setPlainText(result_text)

        # For read operations, populate form with data
        if "id" in data and "title" in data:
            self.post_id_input.setText(str(data["id"]))
            self.title_input.setText(data["title"])
            self.body_input.setPlainText(data["body"])
            self.user_id_input.setText(str(data["userId"]))

    def display_error(self, message):
        """Display error message"""
        error_text = f"❌ ERROR: {message}"
        self.results_text.setPlainText(error_text)
        QMessageBox.critical(self, "Operation Failed", message)

    def set_buttons_enabled(self, enabled):
        """Enable or disable all operation buttons"""
        self.create_btn.setEnabled(enabled)
        self.read_btn.setEnabled(enabled)
        self.update_btn.setEnabled(enabled)
        self.delete_btn.setEnabled(enabled)
        self.read_all_btn.setEnabled(enabled)

    def clear_form(self):
        """Clear all input fields and results"""
        self.post_id_input.clear()
        self.title_input.clear()
        self.body_input.clear()
        self.user_id_input.setText("1")
        self.results_text.clear()
        self.status_label.setText("Ready")


def main():
    """Main function to run the application"""
    app = QApplication(sys.argv)

    # Set application properties
    app.setApplicationName("REST API CRUD Demo - Approach 4")
    app.setApplicationVersion("1.0")

    # Create and show the main window
    window = PostCrudApp()
    window.show()

    # Run the application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()