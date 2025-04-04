# 3. Type System

Python's type system is a unique blend of dynamic and strong typing, with optional static type hints. Here's an overview
of its key characteristics:

## Dynamic Typing

Python is primarily a dynamically typed language[2][5]. This means:

1. Variable types are determined at runtime.
2. You don't need to declare variable types explicitly.
3. A variable can hold different types of data during its lifetime.

For example:

```python
x = 10  # x is an integer
x = "Hello"  # now x is a string
```

## Strong Typing

Despite being dynamic, Python employs strong typing[2][5]:

1. The type of a value doesn't change unexpectedly.
2. Explicit type conversions are required for most type changes.
3. Operations between incompatible types raise errors.

## Type Hints and Annotations

Python 3.5+ introduced optional static type hints[3][6]:

1. They provide additional metadata about expected types.
2. They don't affect runtime behavior but aid static analysis tools.
3. They improve code readability and maintainability.

Example of type hints:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## Gradual Typing

Python supports gradual typing[1], allowing developers to:

1. Add type annotations incrementally.
2. Mix statically typed and dynamically typed code.
3. Use the `Any` type for expressions with unknown types.

## Type Checking

While Python itself doesn't enforce type hints at runtime, external tools like mypy can perform static type
checking[6][8]:

1. These tools analyze code without executing it.
2. They can catch type-related errors before runtime.
3. They support gradual adoption of type hints.

## Custom Types

Python allows the creation of custom types using classes[5], providing flexibility in modeling domain-specific concepts.

In summary, Python's type system offers a balance between the flexibility of dynamic typing and the safety of strong
typing, with optional static type hints for improved code quality and tooling support.

??? note "References"

      - [1] https://typing.python.org/en/latest/spec/concepts.html
      - [2] https://stackoverflow.com/questions/11328920/is-python-strongly-typed
      - [3] https://fastapi.tiangolo.com/python-types/
      - [4] https://vickiboykis.com/2019/07/08/a-deep-dive-on-python-type-hints/
      - [5] https://beecrowd.com/blog-posts/typing-in-python/
      - [6] https://blog.logrocket.com/understanding-type-annotation-python/
      - [7] https://typing.python.org/en/latest/spec/type-system.html
      - [8] https://dagster.io/blog/python-type-hinting
      - [9] https://peps.python.org/pep-0484/
      - [10] https://cerfacs.fr/coop/python-typing
      - [11] https://mypy.readthedocs.io/en/stable/dynamic_typing.html
      - [12] https://runestone.academy/ns/books/published/fopp/Functions/TypeAnnotations.html
      - [13] https://docs.python.org/3/library/typing.html
      - [14] https://docs.python.org/3/library/types.html
      - [15] https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
      - [16] https://auth0.com/blog/typing-in-python/
      - [17] https://docs.python.org/3/library/stdtypes.html
      - [18] https://stackoverflow.com/questions/59023552/in-python-are-type-annotations-and-type-hints-the-same-thing
      - [19] https://weaviate.io/blog/typing-systems-in-python
      - [20] https://www.futurelearn.com/info/courses/python-in-hpc/0/steps/65121

