# 6. Abstract Base Classes (ABC)

ABC in Python stands for Abstract Base Class, which is a class that cannot be instantiated on its own and serves as a
blueprint for other classes. ABCs are designed to define a common interface for a group of related classes, ensuring
that derived classes implement particular methods from the base class.

## Using ABCs in Python

To create an abstract base class in Python, you need to:

1. Import the necessary components from the `abc` module:
   ```python
   from abc import ABC, abstractmethod
   ```

2. Create a class that inherits from `ABC`:
   ```python
   class Shape(ABC):
       @abstractmethod
       def area(self):
           pass
           
       @abstractmethod
       def perimeter(self):
           pass
   ```

3. Use the `@abstractmethod` decorator to mark methods that must be implemented by subclasses.

Attempting to instantiate an abstract class or a subclass that hasn't implemented all abstract methods will raise a
`TypeError`.

## ABCs with Single Inheritance

In single inheritance, a class inherits from one abstract base class:

```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius
```

The concrete class `Circle` must implement all abstract methods defined in the `Shape` ABC. If any abstract method is
not implemented, Python will raise a `TypeError` when you try to instantiate the class.

## ABCs with Multiple Inheritance

Python supports multiple inheritance, allowing a class to inherit from multiple parent classes, including abstract base
classes:

```python
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Square(Shape, Drawable):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def draw(self):
        print("Drawing a square")
```

When using multiple inheritance with ABCs:

1. The derived class must implement all abstract methods from all parent ABCs.
2. Python uses Method Resolution Order (MRO) to determine which method to call when there are methods with the same name
   in different parent classes.
3. You can check the MRO using `ClassName.__mro__` or `ClassName.mro()`.

ABCs are particularly useful for:

- Enforcing that derived classes implement particular methods
- Designing frameworks or libraries where specific behavior needs to be enforced
- Implementing consistent APIs across classes
- Providing a foundational framework for a class hierarchy

Remember that ABCs are meant to be inherited from, not instantiated directly, making them an excellent tool for defining
interfaces and ensuring consistent implementation across related classes.

??? note "References"

     - [1] https://realpython.com/ref/glossary/abstract-base-class/
     - [2] https://dbader.org/blog/abstract-base-classes-in-python
     - [3] https://realpython.com/inheritance-composition-python/
     - [4] https://www.scholarhat.com/tutorial/python/inheritance-in-python
     - [5] https://edube.org/learn/python-advanced-1/abstract-classes-vs-method-overriding-multiple-inheritance
     - [6] https://www.programiz.com/python-programming/multiple-inheritance
     - [7] https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
     - [8] https://www.datacamp.com/tutorial/python-abstract-classes
     - [9] https://www.datacamp.com/tutorial/python-inheritance
     - [10] https://realpython.com/lessons/multiple-inheritance-python/
     - [11] https://30dayscoding.com/blog/abc-import-abc-abstractmethod-python
     - [12] https://geekpython.in/abc-in-python
     - [13] https://www.youtube.com/watch?v=97V7ICVeTJc
     - [14] https://stackoverflow.com/questions/3570796/why-use-abstract-base-classes-in-python
     - [15] https://blog.teclado.com/python-abc-abstract-base-classes/
     - [16] https://www.youtube.com/watch?v=kaZceE16m5A
     - [17] https://python-course.eu/oop/the-abc-of-abstract-base-classes.php
     - [18] https://docs.python.org/3/library/collections.abc.html
     - [19] https://stackoverflow.com/questions/76283254/inheriting-from-an-abstract-class-and-defining-an-abstract-method-to-be-an-exist
     - [20] https://softwareengineering.stackexchange.com/questions/445327/abstract-base-classes-and-mix-ins-in-python
     - [21] https://www.w3schools.com/python/python_inheritance.asp
     - [22] https://python.plainenglish.io/python-tutorial-21-python-inheritance-single-multiple-multilevel-5eca0f4ae257
     - [23] https://docs.python.org/3/tutorial/classes.html
     - [24] https://stackoverflow.com/questions/28799089/python-abc-multiple-inheritance
     - [25] https://docs.python.org/3/library/abc.html
     - [26] https://pybit.es/articles/elevate-your-python-harnessing-the-power-of-abstract-base-classes-abcs/
     - [27] https://earthly.dev/blog/abstract-base-classes-python/
     - [28] https://dev.to/dollardhingra/understanding-the-abstract-base-class-in-python-k7h
     - [29] https://stackoverflow.com/questions/56008847/when-should-one-inherit-from-abc
     - [30] https://www.cs.unb.ca/~bremner/teaching/cs2613/books/python3-doc/library/abc.html
     - [31] https://www.youtube.com/watch?v=mRIeUXhIAxg



---------------

??? info "Use of AI"
        Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
        explanations, examples and/or structure suggestions. All information has been verified, edited and completed by the
        author.