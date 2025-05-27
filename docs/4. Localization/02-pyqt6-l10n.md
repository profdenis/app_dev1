# PyQt6 Application Localization Guide

## PyQt6 Localization Basics

PyQt6 uses Qt's internationalization system, which relies on:

- **QTranslator**: Loads and applies translation files
- **QCoreApplication.translate()**: Marks strings for translation
- **lupdate**: Extracts translatable strings from source code
- **linguist**: GUI tool for creating translations
- **lrelease**: Compiles translation files

### Translation File Workflow

1. **Extract**: Use `lupdate` to scan source code and create `.ts` files
2. **Translate**: Use Qt Linguist to translate strings in `.ts` files
3. **Compile**: Use `lrelease` to compile `.ts` files into binary `.qm` files
4. **Load**: Use QTranslator in your application to load `.qm` files

## Hello World Localization Example

Let's create a simple PyQt6 application with English and French localization.

### Project Structure

```
hello_world_localized/
├── main.py
├── translations/
│   ├── hello_en.ts
│   ├── hello_fr.ts
│   ├── hello_en.qm
│   └── hello_fr.qm
└── resources.qrc (optional)
```

### Step 1: Create the Application (main.py)

```python
import sys
import os
import xml.etree.ElementTree as ET
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QComboBox
from PyQt6.QtCore import QTranslator, QLocale, QCoreApplication


class HelloWorldWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.translations = {}  # Store translations directly
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Language selector
        language_layout = QHBoxLayout()
        language_label = QLabel(self.tr("Language:"))
        self.language_combo = QComboBox()
        self.language_combo.addItem("English", "en")
        self.language_combo.addItem("Français", "fr")
        self.language_combo.currentTextChanged.connect(self.change_language)

        language_layout.addWidget(language_label)
        language_layout.addWidget(self.language_combo)
        language_layout.addStretch()

        # Main content
        self.hello_label = QLabel(self.tr("Hello, World!"))
        self.hello_label.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")

        self.description_label = QLabel(self.tr("This is a simple localization demo."))

        self.button = QPushButton(self.tr("Click me!"))
        self.button.clicked.connect(self.on_button_clicked)

        # Add widgets to layout
        layout.addLayout(language_layout)
        layout.addWidget(self.hello_label)
        layout.addWidget(self.description_label)
        layout.addWidget(self.button)
        layout.addStretch()

        # Set window properties
        self.setWindowTitle(self.tr("Hello World - Localization Demo"))
        self.resize(400, 300)

    def tr(self, text):
        """Translation method with direct .ts file support"""
        if hasattr(self, 'translations') and self.translations:
            key = f"HelloWorldWindow:{text}"
            return self.translations.get(key, text)
        return text  # Fallback to original text

    def change_language(self):
        """Change application language based on combo box selection"""
        language_code = self.language_combo.currentData()
        self.load_ts_directly(language_code)

    def load_ts_directly(self, language_code):
        """Load translations directly from .ts file"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ts_file = os.path.join(script_dir, "translations", f"hello_{language_code}.ts")

        print(f"Loading translation file: {ts_file}")

        if not os.path.exists(ts_file):
            print(f"Translation file not found: {ts_file}")
            self.translations = {}  # Clear translations, use original text
            self.retranslate_ui()
            return

        try:
            tree = ET.parse(ts_file)
            root = tree.getroot()

            self.translations = {}
            translation_count = 0

            for context in root.findall('context'):
                context_name_elem = context.find('name')
                if context_name_elem is None:
                    continue
                context_name = context_name_elem.text or "default"

                for message in context.findall('message'):
                    source_elem = message.find('source')
                    if source_elem is None:
                        continue
                    source = source_elem.text or ""

                    translation_elem = message.find('translation')
                    translation = source  # Default to source text

                    if translation_elem is not None and translation_elem.text:
                        translation = translation_elem.text

                    key = f"{context_name}:{source}"
                    self.translations[key] = translation
                    translation_count += 1

            print(f"Loaded {translation_count} translations from {ts_file}")
            self.retranslate_ui()

        except ET.ParseError as e:
            print(f"Error parsing {ts_file}: {e}")
            self.translations = {}
            self.retranslate_ui()
        except Exception as e:
            print(f"Error loading translations: {e}")
            self.translations = {}
            self.retranslate_ui()

    def retranslate_ui(self):
        """Update all UI text after language change"""
        self.setWindowTitle(self.tr("Hello World - Localization Demo"))
        self.hello_label.setText(self.tr("Hello, World!"))
        self.description_label.setText(self.tr("This is a simple localization demo."))
        self.button.setText(self.tr("Click me!"))

        # Update the language label (this one doesn't change in our simple example)
        # In a real app, you might want to translate this too

    def on_button_clicked(self):
        """Handle button click"""
        self.description_label.setText(self.tr("Button was clicked!"))


def main():
    app = QApplication(sys.argv)

    # Set application properties for translation
    app.setApplicationName("HelloWorldLocalized")
    app.setOrganizationName("YourCompany")

    window = HelloWorldWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
```

### Step 2: Create Translation Files

First, create the `translations` directory and a Qt project file (`hello.pro`) to help with translation extraction:

**hello.pro:**

```
SOURCES = main.py
TRANSLATIONS = translations/hello_en.ts translations/hello_fr.ts
```

### Step 3: Extract Translatable Strings

You need to create the `.ts` files individually for each language. Run these commands:

```bash
pylupdate6 main.py -ts translations/hello_en.ts
pylupdate6 main.py -ts translations/hello_fr.ts
```

**Note**: The Qt project file (`.pro`) approach that works with C++ Qt projects doesn't work reliably with `pylupdate6`
for Python files. Always use the individual command approach shown above.

This creates `.ts` files with all translatable strings extracted from your Python code.

??? info "pylupdate6"

    Here are the installation methods for `pylupdate6` on different operating systems:
    
    **Ubuntu/Debian:**
    
    ```bash
    sudo apt-get update
    sudo apt-get install pyqt6-dev-tools
    ```
    
    **Fedora/RHEL/CentOS:**
    
    ```bash
    sudo dnf install python3-pyqt6-devel
    # or on older versions:
    sudo yum install python3-pyqt6-devel
    ```
    
    **macOS:**
    
    ```bash
    # Using Homebrew
    brew install pyqt6
    
    # Or using pip
    pip install PyQt6-tools
    ```
    
    **Windows:**
    
    ```bash
    # Using pip (most common method)
    pip install PyQt6-tools
    
    # Or using conda
    conda install pyqt6-tools
    ```
    
    **Alternative - Using pip (cross-platform):**
    
    ```bash
    pip install PyQt6-tools
    ```
    
    **Note:** If you installed PyQt6 via pip, `pylupdate6` should already be available. If it's not in your PATH, you might
    need to find where pip installed it:
    
    ```bash
    # Find the location
    python -m pip show PyQt6-tools
    
    # Or try running it as a module
    python -m PyQt6.lupdate.pylupdate6
    ```
    
    The `PyQt6-tools` package is usually the most reliable way to get `pylupdate6` across all platforms.

### Step 4: Create Translations

**translations/hello_en.ts** (English - source language):

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="en_US">
    <context>
        <name>HelloWorldWindow</name>
        <message>
            <source>Language:</source>
            <translation>Language:</translation>
        </message>
        <message>
            <source>Hello, World!</source>
            <translation>Hello, World!</translation>
        </message>
        <message>
            <source>This is a simple localization demo.</source>
            <translation>This is a simple localization demo.</translation>
        </message>
        <message>
            <source>Click me!</source>
            <translation>Click me!</translation>
        </message>
        <message>
            <source>Hello World - Localization Demo</source>
            <translation>Hello World - Localization Demo</translation>
        </message>
        <message>
            <source>Button was clicked!</source>
            <translation>Button was clicked!</translation>
        </message>
    </context>
</TS>
```

**translations/hello_fr.ts** (French):

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="fr_FR">
    <context>
        <name>HelloWorldWindow</name>
        <message>
            <source>Language:</source>
            <translation>Langue :</translation>
        </message>
        <message>
            <source>Hello, World!</source>
            <translation>Bonjour le monde !</translation>
        </message>
        <message>
            <source>This is a simple localization demo.</source>
            <translation>Ceci est une démonstration simple de localisation.</translation>
        </message>
        <message>
            <source>Click me!</source>
            <translation>Cliquez-moi !</translation>
        </message>
        <message>
            <source>Hello World - Localization Demo</source>
            <translation>Bonjour le monde - Démonstration de localisation</translation>
        </message>
        <message>
            <source>Button was clicked!</source>
            <translation>Le bouton a été cliqué !</translation>
        </message>
    </context>
</TS>
```

### Step 5: Load Translations in Your Application

The code above uses the **direct .ts file loading approach**, which is simpler and more reliable
than compiling to .qm files. The application will:

1. Parse .ts files directly using Python's XML parser
2. Store translations in a dictionary
3. Use a custom `tr()` method to look up translations
4. Fall back to original text if no translation is found

**Advantages of direct .ts loading:**

- No need to compile .ts files to .qm files
- Easier debugging (you can see exactly what's being loaded)
- No binary format compatibility issues
- Works reliably across different systems

### Alternative: Using .qm Files (Advanced)

If you prefer the traditional Qt approach with compiled .qm files, you can use this alternative implementation:

```python
# Alternative implementation using QTranslator and .qm files
def load_language_qm(self, language_code):
    """Load translation from compiled .qm file"""
    app = QApplication.instance()

    # Remove previous translator
    if hasattr(self, 'translator') and self.translator:
        app.removeTranslator(self.translator)

    # Load new translator
    self.translator = QTranslator()

    # Get absolute path to translation file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    translation_file = os.path.join(script_dir, "translations", f"hello_{language_code}.qm")

    if os.path.exists(translation_file):
        if self.translator.load(translation_file):
            app.installTranslator(self.translator)
            self.retranslate_ui()
            print(f"Successfully loaded translation: {language_code}")
        else:
            print(f"Failed to load translation file: {translation_file}")
    else:
        print(f"Translation file not found: {translation_file}")


# And use this tr() method instead:
def tr_qm(self, text):
    """Translation method for .qm files"""
    return QCoreApplication.translate("HelloWorldWindow", text)
```

**To use .qm files, you need to:**

1. Compile .ts files using `lrelease`, `pyside6-lrelease`, or the Python compiler provided earlier
2. Replace the `load_ts_directly` method with `load_language_qm`
3. Replace the `tr` method with `tr_qm`

**Note**: The .qm approach is more complex and can have compatibility issues. The direct .ts loading approach shown in
the main example is recommended for learning and development.

This creates `hello_en.qm` and `hello_fr.qm` files that your application can load.

## Key Concepts Explained

### QCoreApplication.translate()

This function marks strings for translation. The first parameter is the context (usually the class name), and the second
is the source text.

### Context

Groups related translations together. Using class names as contexts helps organize translations and handle cases where
the same English word might need different translations in different contexts.

### Dynamic Language Switching

Our example demonstrates changing language at runtime by:

1. Removing the current translator
2. Loading a new translation file
3. Installing the new translator
4. Updating all UI elements

### Translation Workflow Best Practices

1. **Consistent Context Usage**: Use class names consistently as translation contexts
2. **Meaningful Source Text**: Write clear, descriptive source text
3. **Regular Updates**: Re-run `pylupdate6` when adding new translatable strings
4. **Testing**: Test your application with all supported languages
5. **Professional Translation**: For production apps, use professional translators

## Running the Example

1. Save the Python code as `main.py`
2. Create the `translations` directory
3. Create and compile the translation files as shown above
4. Run: `python main.py`
5. Use the language dropdown to switch between English and French

The interface will update in real-time, demonstrating how localization works in PyQt6 applications.

## Next Steps

This basic example covers the fundamentals. Advanced topics include:

- Plural forms handling
- Date and number formatting
- Resource file embedding
- Automatic language detection
- RTL language support
- Context-sensitive help localization