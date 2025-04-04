# 4. Type Hints

Python type hints provide a way to indicate the expected types of variables, function parameters, and return values.
Let's explore this feature in depth with various examples.

## Basic Type Hints

Type hints use a simple syntax with colons to annotate variables and functions:

```python
# Variable annotations
age: int = 30
name: str = "Alice"
is_active: bool = True
price: float = 19.99
```

For functions, you can annotate both parameters and return values:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


def calculate_area(length: float, width: float) -> float:
    return length * width
```

## Built-in Collection Types

Python's typing module provides ways to annotate collection types:

```python
from typing import List, Dict, Tuple, Set

# Lists
numbers: List[int] = [1, 2, 3, 4, 5]
names: List[str] = ["Alice", "Bob", "Charlie"]

# Dictionaries
user_scores: Dict[str, int] = {"Alice": 95, "Bob": 87, "Charlie": 92}
config: Dict[str, str] = {"host": "localhost", "port": "8080"}

# Tuples
point: Tuple[int, int] = (10, 20)
person: Tuple[str, int, bool] = ("Alice", 30, True)

# Sets
unique_ids: Set[int] = {1, 2, 3, 4, 5}
fruits: Set[str] = {"apple", "banana", "orange"}
```

In Python 3.9+, you can use the built-in collection types directly:

```python
# Python 3.9+ syntax
numbers: list[int] = [1, 2, 3, 4, 5]
user_scores: dict[str, int] = {"Alice": 95, "Bob": 87}
point: tuple[int, int] = (10, 20)
unique_ids: set[int] = {1, 2, 3, 4, 5}
```

## Optional and Union Types

For variables that might be None or have multiple possible types:

```python
from typing import Optional, Union


# Optional - can be a specific type or None
def find_user(user_id: int) -> Optional[dict]:
    # Implementation that might return None if user not found
    pass


# Union - can be one of several types
def process_input(data: Union[str, bytes, list]) -> str:
    # Implementation that handles different input types
    pass
```

In Python 3.10+, you can use the pipe operator for unions:

```python
# Python 3.10+ syntax
def process_input(data: str | bytes | list) -> str:
    # Implementation
    pass
```

## Type Aliases

You can create aliases for complex types:

```python
from typing import Dict, List, Tuple

# Type aliases
UserID = int
Username = str
UserRecord = Dict[str, Union[str, int, bool]]
Matrix = List[List[float]]
Point = Tuple[float, float]


def get_user(user_id: UserID) -> UserRecord:
    # Implementation
    pass


def transform_matrix(m: Matrix) -> Matrix:
    # Implementation
    pass
```

## Callable Types

For functions that accept other functions as arguments:

```python
from typing import Callable


# A function that takes a callback function
def process_data(data: list, callback: Callable[[int], str]) -> list:
    return [callback(item) for item in data]


# Usage
def format_number(num: int) -> str:
    return f"Number: {num}"


result = process_data([1, 2, 3], format_number)
```

## User-Defined Classes

Classes work naturally with type hints:

```python
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


def create_greeting(user: User) -> str:
    return f"Hello, {user.name}!"


# Using Type for class references
from typing import Type


def create_user(user_class: Type[User], name: str, age: int) -> User:
    return user_class(name, age)
```

## Generic Types

For creating flexible, reusable components:

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def is_empty(self) -> bool:
        return not self.items


# Usage
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)

str_stack = Stack[str]()
str_stack.push("hello")
```

## Type Checking with mypy

Type hints don't enforce types at runtime, but tools like mypy can check them statically:

```python
# example.py
def double(x: int) -> int:
    return x * 2


result = double("hello")  # Type error!
```

Running mypy will catch this error:

```
$ mypy example.py
example.py:4: error: Argument 1 to "double" has incompatible type "str"; expected "int"
```

Type hints make your code more readable, maintainable, and help catch errors before runtime, especially when used with
static analysis tools like mypy.

??? note "References"

      - [1] https://realpython.com/lessons/type-hinting/ 
      - [2] https://realpython.com/python-type-hints-multiple-types/
      - [3] https://dagster.io/blog/python-type-hinting
      - [4] https://ryan.himmelwright.net/post/python-type-hinting-intro/
      - [5] https://fastapi.tiangolo.com/python-types/
      - [6] https://peps.python.org/pep-0484/
      - [7] https://codefinity.com/blog/A-Comprehensive-Guide-to-Python-Type-Hints
      - [8] https://www.youtube.com/watch?v=MaejDU6pelY
      - [9] https://docs.python.org/3/library/typing.html
      - [10] https://www.youtube.com/watch?v=79zeCq9raY0
      - [11] https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
      - [12] https://dagster.io/posts/python-type-hinting/python-type-hinting-min.jpg?sa=X&ved=2ahUKEwjck76X37yMAxVfHrkGHXoPAcgQ_B16BAgHEAI
      - [13] https://www.youtube.com/watch?v=C1ANuCyniOw
      - [14] https://stackoverflow.com/questions/37835179/how-can-i-specify-the-function-type-in-my-type-hints
      - [15] https://www.reddit.com/r/Python/comments/10zdidm/why_type_hinting_sucks/
      - [16] https://www.reddit.com/r/learnpython/comments/lgwdsd/whats_the_point_of_type_hints_in_python/
      - [17] https://www.infoworld.com/article/2268917/get-started-with-python-type-hints.html

---------------

??? info "Use of AI"
        Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
        explanations, examples and/or structure suggestions. All information has been verified, edited and completed by the
        author.