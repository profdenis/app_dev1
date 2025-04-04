# 2. Classes

Python's class model provides a flexible and powerful way to implement object-oriented programming. Let's dive into the
details of Python's class structure and its various components.

## Class Definition

To define a class in Python, you use the `class` keyword followed by the class name:

```python
class MyClass:
    pass
```

## Attributes

Attributes in Python classes can be instance attributes or class attributes.

### Instance Attributes

Instance attributes are unique to each instance of a class. They are typically defined within the constructor method:

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute
```

### Class Attributes

Class attributes are shared among all instances of a class. They are defined outside any method within the class:

```python
class Person:
    species = "Homo sapiens"  # class attribute
```

## Methods

### Instance Methods

Instance methods are the most common type of methods in Python classes. They take `self` as the first parameter:

```python
class Person:
    def greet(self):
        return f"Hello, my name is {self.name}"
```

### Static Methods

Static methods don't have access to `cls` or `self`. They work like regular functions but belong to the class's
namespace. They are defined using the `@staticmethod` decorator:

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
```

### Class Methods

Class methods take `cls` as the first parameter and can access or modify class state. They are defined using the
`@classmethod` decorator:

```python
class Person:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1
```

## Constructor

The constructor in Python is the `__init__` method. It's called when an object is created:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

## String Representation

Python provides two methods for string representation of objects:

### __str__

The `__str__` method is used for creating a user-friendly string representation:

```python
class Person:
    def __str__(self):
        return f"Person named {self.name}"
```

### __repr__

The `__repr__` method is used for creating a detailed, unambiguous representation of the object, typically for
debugging:

```python
class Person:
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
```

## Public vs Private

Python doesn't have strict public/private distinctions, but it uses conventions:

### Public

By default, all attributes and methods in Python are public:

```python
class Person:
    def public_method(self):
        pass
```

### Private

To indicate that an attribute or method should be treated as private, prefix it with double underscores:

```python
class Person:
    def __init__(self):
        self.__private_attr = 42

    def __private_method(self):
        pass
```

This triggers name mangling, making it harder (but not impossible) to access from outside the class[6][8].

### Protected

A single underscore prefix is used to indicate that an attribute or method should be treated as protected:

```python
class Person:
    def __init__(self):
        self._protected_attr = 42

    def _protected_method(self):
        pass
```

This is just a convention and doesn't prevent access from outside the class[6][8].

In summary, Python's class model provides a flexible system for creating object-oriented code. While it doesn't enforce
strict access control like some other languages, it offers conventions that allow developers to communicate their
intentions regarding the visibility and usage of class members.

??? note "References"
     
      - [1] https://realpython.com/python-classes/
      - [2] https://www.digitalocean.com/community/tutorials/python-static-method
      - [3] https://pythonbasics.org/constructor/
      - [4] https://codedamn.com/news/python/what-is-repr-in-python
      - [5] https://hacktec.gitbooks.io/effective-python/content/en/Chapter3/item27.html
      - [6] https://llego.dev/posts/access-modifiers-python/
      - [7] https://www.tutorialsteacher.com/python/public-private-protected-modifiers
      - [8] https://dev.to/ankitmalikg/python-how-to-define-public-private-and-protected-variables-in-a-class-4g9
      - [9] https://jellis18.github.io/post/2022-01-15-access-modifiers-python/
      - [10] https://www.youtube.com/watch?v=xY__sjI5yVU
      - [11] https://www.datacamp.com/tutorial/python-private-methods-explained
      - [12] https://www.youtube.com/watch?v=tQ1n-ySubAM
      - [13] https://builtin.com/software-engineering-perspectives/python-attributes
      - [14] https://images.prismic.io/turing/65981105531ac2845a2729c7_Importance_of_Python_class_attributes_6495667a2b.webp?auto=format%2Ccompress&sa=X&ved=2ahUKEwjn6PH2-7yMAxXUrokEHX32Kl4Q_B16BAgDEAI
      - [15] https://www.turing.com/kb/introduction-to-python-class-attributes
      - [16] https://docs.python.org/3/reference/datamodel.html
      - [17] https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
      - [18] https://labex.io/tutorials/python-how-to-define-class-attributes-and-methods-at-runtime-398174
      - [19] https://www.w3schools.com/python/python_classes.asp
      - [20] https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
      - [21] https://stackoverflow.com/questions/2438473/what-is-the-purpose-of-static-methods-how-do-i-know-when-to-use-one
      - [22] https://www.youtube.com/watch?v=-LevVCuAi2E
      - [23] https://stackoverflow.com/questions/38280526/is-a-constructor-init-necessary-for-a-class-in-python
      - [24] https://realpython.com/python-multiple-constructors/
      - [25] https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define-objects-in-python-3
      - [26] https://docs.python.org/3/tutorial/classes.html
      - [27] https://realpython.com/python-class-constructor/
      - [28] https://www.reddit.com/r/learnprogramming/comments/83flwh/what_exactly_is_a_constructor_and_what_does_it_do/
      - [29] https://www.wscubetech.com/resources/python/constructors
      - [30] https://www.youtube.com/watch?v=uKmfhJA76Y4
      - [31] https://www.reddit.com/r/learnpython/comments/izjrbp/a_beginners_guide_to_str_and_repr/
      - [32] https://discuss.python.org/t/what-are-the-differences-between-str-and-repr-in-class-methods/44142
      - [33] https://www.youtube.com/watch?v=-lz5kRcoU5Q
      - [34] https://realpython.com/python-repr-vs-str/
      - [35] https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes
      - [36] https://www.reddit.com/r/learnpython/comments/pfkj1h/when_should_i_use_private_attributes_in_python/
      - [37] https://profound.academy/python-mid/private-variables-in-classes-km0x40ery3suTthPk3MB
      - [38] https://diveintopython.org/learn/classes/methods
      - [39] https://www.techwithtim.net/tutorials/python-programming/classes-objects-in-python/private-and-public-classes
      - [40] https://softwareengineering.stackexchange.com/questions/452995/should-private-attributes-or-public-attributes-be-the-default-in-python-classes
      - [41] https://stackoverflow.com/questions/55525463/public-and-private-methods-in-python
      - [42] https://stackoverflow.com/questions/46312470/difference-between-methods-and-attributes-in-python
      - [43] https://www.almabetter.com/bytes/tutorials/python/methods-and-attributes-in-python
      - [44] https://www.linkedin.com/pulse/exploring-differences-between-class-methods-static-python
      - [45] https://codeburst.io/python-3-how-to-use-a-instance-non-static-method-as-static-a2cf21bfd5b4
      - [46] https://www.boardinfinity.com/blog/class-and-static-method-in-python-differences/
      - [47] https://www.reddit.com/r/AskProgramming/comments/120mulm/good_example_for_static_vs_nonstatic_methods/
      - [48] https://realpython.com/instance-class-and-static-methods-demystified/
      - [49] https://www.tutorialspoint.com/python/python_constructors.htm
      - [50] https://wiingy.com/learn/python/constructors-in-python/
      - [51] https://codedamn.com/news/python/explaining-constructor-in-python-with-an-example
      - [52] https://www.shiksha.com/online-courses/articles/constructors-in-python-definition-types-and-rules/
      - [53] https://www.youtube.com/watch?v=neVmG4ljQiE
      - [54] https://hostman.com/tutorials/how-to-use-the-str-and-repr-methods-in-python/
      - [55] https://www.python-engineer.com/posts/difference-between-str-and-repr/
      - [56] https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
      - [57] https://www.digitalocean.com/community/tutorials/python-str-repr-functions
      - [58] https://how.dev/answers/what-is-the-difference-between-str-and-repr
      - [59] https://www.reddit.com/r/learnprogramming/comments/dgbnnf/python_whats_the_difference_between_str_and_repr/


---------------

??? info "Use of AI"
        Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
        explanations, examples and/or structure suggestions. All information has been verified, edited and completed by the
        author.