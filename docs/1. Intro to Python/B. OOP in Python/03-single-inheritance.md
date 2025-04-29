# 3. Single Inheritance

Single inheritance in Python and Java allows a class to inherit properties and methods from a single parent class.
However, there are some key differences in how these languages implement single inheritance:

## Python Single Inheritance

In Python, single inheritance is implemented as follows:

```python
class ParentClass:
    # Parent class attributes and methods

class ChildClass(ParentClass):
    # Child class attributes and methods
```

Key features of Python's single inheritance:

1. Syntax simplicity: The child class is defined by specifying the parent class name in parentheses after the child
   class name.

2. Dynamic typing: Python's dynamic typing allows for more flexible attribute and method inheritance.

3. Method resolution: Python uses the Method Resolution Order (MRO) to determine which method to call when there are
   methods with the same name in different classes.

4. `super()` function: Used to call methods from the parent class, allowing the child class to extend functionality
   rather than completely replacing it.

## Java Single Inheritance

Java implements single inheritance like this:

```java
class ParentClass {
    // Parent class attributes and methods
}

class ChildClass extends ParentClass {
    // Child class attributes and methods
}
```

Key features of Java's single inheritance:

1. `extends` keyword: Java uses the `extends` keyword to indicate inheritance.

2. Static typing: Java's static typing system requires explicit type declarations for inherited members.

3. Access modifiers: Java provides strict access control with public, private, and protected modifiers.

4. `super` keyword: Used to call the parent class constructor or methods.

## Comparison

1. Syntax: Python's syntax is more concise, while Java's is more explicit with the `extends` keyword.

2. Multiple inheritance: Python supports multiple inheritance, while Java only allows single inheritance for classes
   (though it supports multiple interface implementation).

3. Type system: Python's dynamic typing offers more flexibility, while Java's static typing provides compile-time type
   checking.

4. Method overriding: Both languages support method overriding, but Python uses the `super()` function while Java uses
   the `super` keyword.

5. Constructor chaining: In Python, you explicitly call the parent constructor using `super().__init__()`, while in
   Java, the parent constructor is implicitly called unless specified otherwise.

6. Access control: Java has stricter access control with explicit modifiers, while Python uses naming conventions (e.g.,
   underscores for private members).

In both languages, single inheritance promotes code reuse and allows for the creation of hierarchical relationships
between classes. However, Python's implementation is generally more flexible and concise, while Java's offers more
structure and compile-time safety.

??? note "References"

     - [1] https://www.scientecheasy.com/2023/09/single-inheritance-in-python.html/
     - [2] https://www.scholarhat.com/tutorial/java/single-inheritance-in-java
     - [3] https://beginnersbook.com/2013/05/java-inheritance-types/
     - [4] https://www.shiksha.com/online-courses/articles/single-inheritance-in-java-blogId-159513
     - [5] https://geekpython.in/class-inheritance-in-python
     - [6] https://www.geekster.in/articles/java-inheritance/
     - [7] https://www.tutorialspoint.com/java/java_inheritance.htm
     - [8] https://www.simplilearn.com/tutorials/java-tutorial/inheritence-in-java
     - [9] https://www.wscubetech.com/resources/python/inheritance
     - [10] https://realpython.com/inheritance-composition-python/
     - [11] https://labex.io/tutorials/python-how-to-use-single-inheritance-in-python-398272
     - [12] https://www.codechef.com/learn/course/oops-concepts-in-python/CPOPPY03/problems/ADVPPY25
     - [13] https://www.tutorialspoint.com/python/python_inheritance.htm
     - [14] https://www.w3schools.com/python/python_inheritance.asp
     - [15] https://www.linkedin.com/pulse/in-depth-exploration-inheritance-java-nitin-singh
     - [16] https://www.tpointtech.com/inheritance-in-java
     - [17] https://www.ccbp.in/blog/articles/single-inheritance-in-java
     - [18] https://www.w3schools.com/java/java_inheritance.asp
     - [19] https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html
     - [20] https://www.studysmarter.co.uk/explanations/computer-science/computer-programming/java-inheritance/
     - [21] https://files.codingninjas.in/article_images/single-inheritance-in-java-17217.webp?sa=X&ved=2ahUKEwiQs_Pug72MAxXqma8BHTQQClAQ_B16BAgBEAI
     - [22] https://www.scaler.com/topics/python/inheritance-in-python/
     - [23] https://www.tutorjoes.in/python_programming_tutorial/single_inheritance_in_python
     - [24] https://www.datacamp.com/tutorial/python-inheritance
     - [25] https://www.scholarhat.com/tutorial/python/inheritance-in-python
     - [26] https://www.programiz.com/python-programming/inheritance
     - [27] https://wiingy.com/learn/python/inheritance-in-python/
     - [28] https://www.programiz.com/java-programming/inheritance
     - [29] https://timespro.com/blog/inheritance-in-java-understand-with-examples
   

## Overloading operators and `isinstance`

To use `isinstance()` when overloading the `+` operator in a class, you typically check the type of the second operand
to handle different addition scenarios. Here's an example with a `Vector` class that supports adding vectors or scalars:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector):  # Vector + Vector
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):  # Vector + scalar
            return Vector(self.x + other, self.y + other)
        else:
            raise TypeError(f"Unsupported type for +: 'Vector' and '{type(other).__name__}'")

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

**Key implementation details**[2][4]:

1. **Type checking**: `isinstance()` verifies if `other` is a `Vector` instance or numeric type
2. **Multiple type support**: The tuple `(int, float)` allows scalar addition with either integers or floats
3. **Error handling**: Raises `TypeError` for unsupported types

**Example usage**:
```python
v1 = Vector(2, 3)
v2 = Vector(1, 4)
scalar = 5

print(v1 + v2)    # Vector(3, 7)
print(v1 + 5)     # Vector(7, 8)
print(v1 + "str") # TypeError: Unsupported type for +: 'Vector' and 'str'
```

This pattern ensures type safety while allowing flexible operations. The `isinstance()` check properly handles 
inheritance hierarchies if you create subclasses of `Vector`[4]. For more complex scenarios, you might also implement
`__radd__` to handle cases where the vector is on the right side of the `+` operator[5].

??? note "References"

      - [1] https://www.w3schools.com/python/ref_func_isinstance.asp
      - [2] https://gist.github.com/699fb6f7c43ae1eb6e06
      - [3] https://stackoverflow.com/questions/69210526/new-to-python-use-add-method-for-more-than-2-instances
      - [4] https://pynative.com/python-isinstance-explained-with-examples/
      - [5] https://realpython.com/python-magic-methods/
      - [6] https://glennrowe.net/programmingpages/2021/06/13/overloading-arithmetic-operators/
      - [7] https://stackoverflow.com/questions/62115060/python-how-to-use-add-special-method-to-add-instances-of-the-same-class-tha
      - [8] https://www.pythonmorsels.com/every-dunder-method/
      - [9] https://stackoverflow.com/questions/66803769/different-return-types-overloading-add
      - [10] https://docs.python.org/3/tutorial/classes.html
      - [11] https://docs.python.org/3/library/functions.html
      - [12] https://testdriven.io/tips/aca1254d-ef6d-4de3-b4ba-8607c5d51737/
      - [13] https://www.reddit.com/r/learnpython/comments/a2sodz/how_does_this_code_work_classes_add_method/
      - [14] https://www.wscubetech.com/resources/python/operator-overloading
      - [15] https://realpython.com/operator-function-overloading/
      - [16] https://docs.python.org/3/library/operator.html
      - [17] https://openstax.org/books/introduction-python-programming/pages/11-4-overloading-operators
      - [18] https://hyperskill.org/university/python/isinstance-in-python
      - [19] https://www.codearmo.com/python-tutorial/object-orientated-programming-arithmetic-methods
      - [20] https://discuss.python.org/t/how-to-overload-add-method-in-a-self-made-class-to-sum-multiple-objects-of-the-class/40543

## Table of operator overloading methods

Here is a table summarizing the main operators that can be overloaded in Python, along with their corresponding 
special (magic/dunder) methods[2][3][4]:

| Operator Symbol | Operation Name          | Special Method  |
|-----------------|-------------------------|-----------------|
| +               | Addition                | `__add__`       |
| -               | Subtraction             | `__sub__`       |
| *               | Multiplication          | `__mul__`       |
| /               | True Division           | `__truediv__`   |
| //              | Floor Division          | `__floordiv__`  |
| %               | Modulo                  | `__mod__`       |
| **              | Power                   | `__pow__`       |
| +=              | In-place Addition       | `__iadd__`      |
| -=              | In-place Subtraction    | `__isub__`      |
| *=              | In-place Multiplication | `__imul__`      |
| /=              | In-place True Division  | `__itruediv__`  |
| //=             | In-place Floor Division | `__ifloordiv__` |
| %=              | In-place Modulo         | `__imod__`      |
| **=             | In-place Power          | `__ipow__`      |
| - (unary)       | Negation                | `__neg__`       |
| + (unary)       | Unary Plus              | `__pos__`       |
| ~               | Bitwise NOT             | `__invert__`    |
|                 | Greater Than            | `__gt__`        |
| >=              | Greater Than or Equal   | `__ge__`        |
| []              | Indexing                | `__getitem__`   |
| []=             | Item Assignment         | `__setitem__`   |
| del []          | Item Deletion           | `__delitem__`   |
| ()              | Call                    | `__call__`      |
| str()           | String Conversion       | `__str__`       |
| repr()          | Representation          | `__repr__`      |
| len()           | Length                  | `__len__`       |
| hash()          | Hashing                 | `__hash__`      |
| bool()          | Truth Value             | `__bool__`      |

This table covers the most commonly overloaded operators. There are additional magic methods for bitwise operations, 
attribute access, context management, and more, but these are the core operators you will typically overload in custom 
classes[2][3][4].

??? note "References"

      - [1] https://www.programiz.com/python-programming/operator-overloading
      - [2] https://wiingy.com/learn/python/operator-overloading-in-python/
      - [3] https://docs.python.org/3/reference/datamodel.html
      - [4] https://docs.python.org/3/library/operator.html
      - [5] https://www.wscubetech.com/resources/python/operator-overloading
      - [6] https://www.stat.berkeley.edu/~spector/extension/python/notes/node109.html
      - [7] https://pythonflood.com/python-operator-overloading-a-comprehensive-guide-c96c22176646
      - [8] https://peps.python.org/pep-0335/
      - [9] https://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html
      - [10] https://www.w3schools.com/python/python_operators.asp
      - [11] https://realpython.com/python-magic-methods/
      - [12] https://www.teach.cs.toronto.edu/~csc110y/fall/notes/A-python-builtins/03-special-methods.html
      - [13] https://openstax.org/books/introduction-python-programming/pages/11-4-overloading-operators
      - [14] https://python-course.eu/oop/magic-methods.php
      - [15] https://www.pythonmorsels.com/every-dunder-method/
      - [16] https://github.com/milaan9/06_Python_Object_Class/blob/main/004_Python_Operator_Overloading.ipynb
      - [17] https://stackoverflow.com/questions/64582940/table-of-python-operand-types
      - [18] https://www.algorystcorner.com/operator-overloading-in-python/
      - [19] https://stackoverflow.com/questions/2400635/comprehensive-guide-to-operator-overloading-in-python


---------------

??? info "Use of AI"
        Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
        explanations, examples and/or structure suggestions. All information has been verified, edited and completed by the
        author.