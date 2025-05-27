# Reading and Writing JSON Files

## Overview

JSON (JavaScript Object Notation) is a lightweight, human-readable data interchange format. Python's built-in `json`
module makes it easy to work with JSON data, converting between JSON strings and Python objects seamlessly.

## Why Use JSON?

JSON is ideal for:

- Web APIs and data exchange
- Configuration files
- Storing structured data
- Cross-platform data sharing
- Human-readable data storage

## JSON and Python Data Types

### JSON to Python Mapping

| JSON Type      | Python Type      |
|----------------|------------------|
| `null`         | `None`           |
| `true`/`false` | `True`/`False`   |
| `number`       | `int` or `float` |
| `string`       | `str`            |
| `array`        | `list`           |
| `object`       | `dict`           |

## Basic JSON Operations

### Reading JSON Files

```python
import json

# Read JSON from file
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
    print(type(data))  # Usually dict or list
```

### Writing JSON Files

```python
import json

# Sample data
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "cycling", "cooking"]
}

# Write JSON to file
with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
```

### Working with JSON Strings

```python
import json

# Convert Python object to JSON string
data = {"name": "Bob", "age": 25}
json_string = json.dumps(data, indent=2)
print(json_string)

# Convert JSON string to Python object
parsed_data = json.loads(json_string)
print(parsed_data)
print(type(parsed_data))  # <class 'dict'>
```

## Working with Standard Python Types

### Example 1: Simple Dictionary

```python
import json

# Create and save a simple configuration
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp",
        "ssl": True
    },
    "api": {
        "timeout": 30,
        "retries": 3,
        "endpoints": [
            "/api/users",
            "/api/products",
            "/api/orders"
        ]
    },
    "features": {
        "logging": True,
        "debug": False,
        "cache_size": 1000
    }
}

# Save configuration
with open('config.json', 'w', encoding='utf-8') as file:
    json.dump(config, file, indent=4)

# Load and use configuration
with open('config.json', 'r', encoding='utf-8') as file:
    loaded_config = json.load(file)

    db_host = loaded_config['database']['host']
    api_timeout = loaded_config['api']['timeout']
    print(f"Database host: {db_host}")
    print(f"API timeout: {api_timeout} seconds")
```

### Example 2: List of Dictionaries

```python
import json

# Student records
students = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice@email.com",
        "grades": {
            "math": 95,
            "science": 87,
            "english": 92
        },
        "active": True
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "email": "bob@email.com",
        "grades": {
            "math": 78,
            "science": 91,
            "english": 85
        },
        "active": True
    },
    {
        "id": 3,
        "name": "Charlie Brown",
        "email": "charlie@email.com",
        "grades": {
            "math": 82,
            "science": 79,
            "english": 88
        },
        "active": False
    }
]

# Save students data
with open('students.json', 'w', encoding='utf-8') as file:
    json.dump(students, file, indent=4)

# Load and process students data
with open('students.json', 'r', encoding='utf-8') as file:
    loaded_students = json.load(file)

    # Find active students with math grade > 80
    high_math_students = [
        student for student in loaded_students
        if student['active'] and student['grades']['math'] > 80
    ]

    print("High-performing math students:")
    for student in high_math_students:
        print(f"- {student['name']}: {student['grades']['math']}")
```

## Working with Custom Classes

### Basic Approach: Manual Conversion

```python
import json


class Person:
    def __init__(self, name, age, email, hobbies=None):
        self.name = name
        self.age = age
        self.email = email
        self.hobbies = hobbies or []

    def to_dict(self):
        """Convert Person object to dictionary"""
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'hobbies': self.hobbies
        }

    @classmethod
    def from_dict(cls, data):
        """Create Person object from dictionary"""
        return cls(
            name=data['name'],
            age=data['age'],
            email=data['email'],
            hobbies=data.get('hobbies', [])
        )

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"


# Create Person objects
people = [
    Person("Alice", 30, "alice@email.com", ["reading", "hiking"]),
    Person("Bob", 25, "bob@email.com", ["gaming", "cooking"]),
    Person("Charlie", 35, "charlie@email.com", ["photography"])
]

# Convert to dictionaries and save
people_data = [person.to_dict() for person in people]

with open('people.json', 'w', encoding='utf-8') as file:
    json.dump(people_data, file, indent=4)

# Load and convert back to Person objects
with open('people.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)

    loaded_people = [Person.from_dict(data) for data in loaded_data]

    print("Loaded people:")
    for person in loaded_people:
        print(person)
```

### Advanced Approach: Custom JSON Encoder/Decoder

```python
import json
from datetime import datetime, date


class Person:
    def __init__(self, name, age, email, birth_date=None, hobbies=None):
        self.name = name
        self.age = age
        self.email = email
        self.birth_date = birth_date
        self.hobbies = hobbies or []

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


class PersonEncoder(json.JSONEncoder):
    """Custom JSON encoder for Person objects"""

    def default(self, obj):
        if isinstance(obj, Person):
            return {
                '__type__': 'Person',
                'name': obj.name,
                'age': obj.age,
                'email': obj.email,
                'birth_date': obj.birth_date.isoformat() if obj.birth_date else None,
                'hobbies': obj.hobbies
            }
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()

        # Let the base class handle other types
        return super().default(obj)


def person_decoder(dct):
    """Custom JSON decoder for Person objects"""
    if '__type__' in dct and dct['__type__'] == 'Person':
        birth_date = None
        if dct['birth_date']:
            birth_date = datetime.fromisoformat(dct['birth_date']).date()

        return Person(
            name=dct['name'],
            age=dct['age'],
            email=dct['email'],
            birth_date=birth_date,
            hobbies=dct['hobbies']
        )
    return dct


# Create Person objects with dates
people = [
    Person("Alice", 30, "alice@email.com", date(1993, 5, 15), ["reading", "hiking"]),
    Person("Bob", 25, "bob@email.com", date(1998, 8, 22), ["gaming", "cooking"]),
    Person("Charlie", 35, "charlie@email.com", date(1988, 12, 3), ["photography"])
]

# Save with custom encoder
with open('people_advanced.json', 'w', encoding='utf-8') as file:
    json.dump(people, file, cls=PersonEncoder, indent=4)

# Load with custom decoder
with open('people_advanced.json', 'r', encoding='utf-8') as file:
    loaded_people = json.load(file, object_hook=person_decoder)

    print("Loaded people with custom decoder:")
    for person in loaded_people:
        print(f"{person} - Born: {person.birth_date}")
```

## Complex Example: Library Management System

```python
import json
from datetime import datetime, date
from typing import List, Optional


class Book:
    def __init__(self, isbn, title, author, publication_year, genre=None):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre or "Unknown"

    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'publication_year': self.publication_year,
            'genre': self.genre
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            isbn=data['isbn'],
            title=data['title'],
            author=data['author'],
            publication_year=data['publication_year'],
            genre=data.get('genre', 'Unknown')
        )

    def __repr__(self):
        return f"Book('{self.title}' by {self.author})"


class Member:
    def __init__(self, member_id, name, email, join_date=None):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.join_date = join_date or date.today()
        self.borrowed_books = []

    def borrow_book(self, book, due_date):
        loan = {
            'book': book,
            'borrowed_date': date.today(),
            'due_date': due_date
        }
        self.borrowed_books.append(loan)

    def to_dict(self):
        return {
            'member_id': self.member_id,
            'name': self.name,
            'email': self.email,
            'join_date': self.join_date.isoformat(),
            'borrowed_books': [
                {
                    'book': loan['book'].to_dict(),
                    'borrowed_date': loan['borrowed_date'].isoformat(),
                    'due_date': loan['due_date'].isoformat()
                }
                for loan in self.borrowed_books
            ]
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(
            member_id=data['member_id'],
            name=data['name'],
            email=data['email'],
            join_date=datetime.fromisoformat(data['join_date']).date()
        )

        # Reconstruct borrowed books
        for loan_data in data['borrowed_books']:
            book = Book.from_dict(loan_data['book'])
            borrowed_date = datetime.fromisoformat(loan_data['borrowed_date']).date()
            due_date = datetime.fromisoformat(loan_data['due_date']).date()

            loan = {
                'book': book,
                'borrowed_date': borrowed_date,
                'due_date': due_date
            }
            member.borrowed_books.append(loan)

        return member

    def __repr__(self):
        return f"Member(ID: {self.member_id}, Name: '{self.name}')"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def to_dict(self):
        return {
            'name': self.name,
            'books': [book.to_dict() for book in self.books],
            'members': [member.to_dict() for member in self.members]
        }

    @classmethod
    def from_dict(cls, data):
        library = cls(data['name'])

        # Reconstruct books
        library.books = [Book.from_dict(book_data) for book_data in data['books']]

        # Reconstruct members
        library.members = [Member.from_dict(member_data) for member_data in data['members']]

        return library

    def save_to_json(self, filename):
        """Save library data to JSON file"""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.to_dict(), file, indent=4, ensure_ascii=False)

    @classmethod
    def load_from_json(cls, filename):
        """Load library data from JSON file"""
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return cls.from_dict(data)

    def get_overdue_books(self):
        """Find all overdue books"""
        today = date.today()
        overdue = []

        for member in self.members:
            for loan in member.borrowed_books:
                if loan['due_date'] < today:
                    overdue.append({
                        'member': member,
                        'book': loan['book'],
                        'due_date': loan['due_date'],
                        'days_overdue': (today - loan['due_date']).days
                    })

        return overdue


# Example usage
def create_sample_library():
    """Create a sample library with books and members"""
    library = Library("City Central Library")

    # Add books
    books = [
        Book("978-0-547-92822-7", "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy"),
        Book("978-0-06-112008-4", "To Kill a Mockingbird", "Harper Lee", 1960, "Classic"),
        Book("978-0-7432-7356-5", "The Da Vinci Code", "Dan Brown", 2003, "Thriller"),
        Book("978-0-14-303943-3", "1984", "George Orwell", 1949, "Dystopian")
    ]

    for book in books:
        library.add_book(book)

    # Add members
    member1 = Member(1, "Alice Johnson", "alice@email.com", date(2023, 1, 15))
    member2 = Member(2, "Bob Smith", "bob@email.com", date(2023, 3, 22))

    # Simulate book borrowing
    from datetime import timedelta
    member1.borrow_book(books[0], date.today() + timedelta(days=14))  # The Hobbit
    member1.borrow_book(books[1], date.today() - timedelta(days=5))  # Overdue book
    member2.borrow_book(books[2], date.today() + timedelta(days=7))  # The Da Vinci Code

    library.add_member(member1)
    library.add_member(member2)

    return library


# Create and save library
library = create_sample_library()
library.save_to_json('library.json')
print(f"Saved library '{library.name}' with {len(library.books)} books and {len(library.members)} members")

# Load library from JSON
loaded_library = Library.load_from_json('library.json')
print(f"Loaded library '{loaded_library.name}'")

# Check for overdue books
overdue = loaded_library.get_overdue_books()
if overdue:
    print("\nOverdue books:")
    for item in overdue:
        print(f"- {item['member'].name} has '{item['book'].title}' overdue by {item['days_overdue']} days")
else:
    print("\nNo overdue books!")

# Display all members and their books
print(f"\nLibrary members:")
for member in loaded_library.members:
    print(f"- {member.name} (joined {member.join_date})")
    if member.borrowed_books:
        for loan in member.borrowed_books:
            status = "OVERDUE" if loan['due_date'] < date.today() else "OK"
            print(f"  * '{loan['book'].title}' due {loan['due_date']} [{status}]")
    else:
        print("  * No borrowed books")
```

## Error Handling and Best Practices

### Robust JSON Reading

```python
import json


def safe_load_json(filename, default=None):
    """Safely load JSON with comprehensive error handling"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"File {filename} not found")
        return default

    except PermissionError:
        print(f"Permission denied accessing {filename}")
        return default

    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {filename}: {e}")
        return default

    except UnicodeDecodeError as e:
        print(f"Encoding error reading {filename}: {e}")
        return default

    except Exception as e:
        print(f"Unexpected error reading {filename}: {e}")
        return default


# Usage
data = safe_load_json('config.json', default={})
if data:
    print("Configuration loaded successfully")
else:
    print("Using default configuration")
```

### Validating JSON Structure

```python
import json


def validate_person_data(data):
    """Validate that data contains required Person fields"""
    required_fields = ['name', 'age', 'email']

    if not isinstance(data, dict):
        raise ValueError("Person data must be a dictionary")

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    if not isinstance(data['name'], str) or not data['name'].strip():
        raise ValueError("Name must be a non-empty string")

    if not isinstance(data['age'], int) or data['age'] < 0:
        raise ValueError("Age must be a non-negative integer")

    if not isinstance(data['email'], str) or '@' not in data['email']:
        raise ValueError("Email must be a valid email address")

    return True


def load_people_safely(filename):
    """Load people data with validation"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Expected a list of people")

        people = []
        for i, person_data in enumerate(data):
            try:
                validate_person_data(person_data)
                people.append(Person.from_dict(person_data))
            except ValueError as e:
                print(f"Invalid person data at index {i}: {e}")
                continue

        return people

    except Exception as e:
        print(f"Error loading people: {e}")
        return []


# Usage
people = load_people_safely('people.json')
print(f"Successfully loaded {len(people)} people")
```

## Advanced JSON Techniques

### Pretty Printing JSON

```python
import json


def pretty_print_json(data):
    """Pretty print JSON data with custom formatting"""
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


# Custom formatting options
data = {"name": "José", "age": 30, "hobbies": ["música", "fútbol"]}

# Different formatting options
print("Compact:")
print(json.dumps(data, separators=(',', ':')))

print("\nPretty with sorted keys:")
print(json.dumps(data, indent=2, sort_keys=True))

print("\nWith Unicode characters:")
print(json.dumps(data, indent=2, ensure_ascii=False))
```

### Working with Large JSON Files

```python
import json


def process_large_json_file(filename, process_item_func):
    """Process large JSON files item by item (assuming it's a list)"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if isinstance(data, list):
                for i, item in enumerate(data):
                    try:
                        process_item_func(item, i)
                    except Exception as e:
                        print(f"Error processing item {i}: {e}")
            else:
                process_item_func(data, 0)

    except Exception as e:
        print(f"Error processing file: {e}")


def process_person(person_data, index):
    """Example processing function"""
    print(f"Processing person {index + 1}: {person_data.get('name', 'Unknown')}")


# Usage
process_large_json_file('large_people.json', process_person)
```

## Key Points to Remember

1. **Always specify encoding** when opening files (use UTF-8)
2. **Handle JSON errors gracefully** with try-except blocks
3. **Validate data structure** before processing
4. **Use `ensure_ascii=False`** to preserve Unicode characters
5. **Consider memory usage** with large JSON files
6. **Create conversion methods** (`to_dict`, `from_dict`) for custom classes
7. **Use custom encoders/decoders** for complex objects
8. **Handle dates and datetime objects** explicitly (JSON doesn't have native date types)

## Common Mistakes to Avoid

- Not handling `JSONDecodeError` exceptions
- Forgetting that JSON doesn't support Python sets, tuples, or datetime objects directly
- Not validating JSON structure before processing
- Using `eval()` instead of `json.loads()` (security risk)
- Not specifying encoding when reading files
- Assuming JSON file structure without validation
- Not handling None/null values properly
- Forgetting to use `ensure_ascii=False` for international characters

This guide provides a comprehensive foundation for working with JSON in Python, from simple data structures to complex
custom classes with proper error handling and validation.


---------------

??? info "Use of AI"
    Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
    explanations, examples and/or structure suggestions. All information has been verified, edited and completed by
    the author.