# 5. Multiple Inheritance

Multiple inheritance in Python is a powerful feature that allows a class to inherit attributes and methods from more
than one parent class. This is a significant difference from Java, which only supports single inheritance for classes
(though Java does allow implementing multiple interfaces).

## How Multiple Inheritance Works in Python

In Python, multiple inheritance is implemented by listing all parent classes in the class definition, separated by
commas:

```python
class Parent1:
    def method1(self):
        print("Method from Parent1")


class Parent2:
    def method2(self):
        print("Method from Parent2")


class Child(Parent1, Parent2):
    pass


# Creating an instance
child = Child()
child.method1()  # Output: Method from Parent1
child.method2()  # Output: Method from Parent2
```

In this example, the `Child` class inherits methods from both `Parent1` and `Parent2`, allowing it to use both
`method1()` and `method2()`.

## Practical Example: The Mythical Unicorn

Let's consider a more concrete example using a mythical creature:

```python
class Horse:
    def __init__(self, name):
        self.name = name

    def run(self):
        return f"{self.name} is running."

    def eat_hay(self):
        return f"{self.name} is eating hay."


class Narwhal:
    def swim(self):
        return f"{self.name} is swimming."

    def has_horn(self):
        return True


class Unicorn(Horse, Narwhal):
    def magic_powers(self):
        return f"{self.name} is using magical powers!"
```

Here, `Unicorn` inherits characteristics from both `Horse` (running, eating hay) and `Narwhal` (swimming, having a
horn), plus adds its own unique ability.

## Method Resolution Order (MRO)

When a method is called on an instance, Python needs to determine which implementation to use, especially if multiple
parent classes define the same method. Python uses the C3 linearization algorithm to establish a Method Resolution
Order (MRO):

```python
class A:
    def greet(self):
        return "Hello from A"


class B:
    def greet(self):
        return "Hello from B"


class C(A, B):
    pass


c = C()
print(c.greet())  # Output: Hello from A
print(C.__mro__)  # Shows the method resolution order
```

The method from the first parent class in the inheritance list (`A` in this case) is used.

## Advantages of Multiple Inheritance

1. **Code Reusability**: Allows combining functionalities from different classes, reducing code duplication.

2. **Flexibility in Class Design**: Enables creating complex class structures by inheriting from multiple base classes.

3. **Modularity**: Supports creating mixins (specialized classes providing specific functionality) that can be combined
   with various classes.

## Disadvantages of Multiple Inheritance

1. **Ambiguity and Name Clashes**: When multiple parent classes define methods with the same name, it can lead to
   confusion.

2. **Complexity and Maintenance**: As the inheritance hierarchy grows, understanding and maintaining the relationships
   between classes becomes more challenging.

3. **Diamond Problem**: When a class inherits from two classes that have a common ancestor, ambiguity can arise about
   which implementation to use.

4. **Tight Coupling**: Changes in one base class may have unintended effects on derived classes.

## The Diamond Problem

The diamond problem is a specific challenge in multiple inheritance:

```python
class A:
    def method(self):
        print("Method from A")


class B(A):
    def method(self):
        print("Method from B")


class C(A):
    def method(self):
        print("Method from C")


class D(B, C):
    pass


d = D()
d.method()  # Which method gets called?
```

Python's MRO resolves this by following a specific order, but it's still a complexity to be aware of.

Multiple inheritance is a powerful tool in Python, but it should be used judiciously. When used appropriately, it can
lead to elegant, modular code. When overused, it can create maintenance challenges.

??? note "References"

     - [1] https://dev.to/gayathridevi_manojkumar_d/understanding-multiple-inheritance-in-python-and-java-1ig
     - [2] https://realpython.com/lessons/multiple-inheritance-python/
     - [3] https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
     - [4] https://www.scientecheasy.com/2023/09/multiple-inheritance-in-python.html/
     - [5] https://blog.stackademic.com/python-classes-and-the-power-of-multiple-inheritance-5a551e124603
     - [6] https://python.plainenglish.io/multiple-inheritance-in-python-a-basic-guide-with-examples-124ee08e7f62
     - [7] https://python-course.eu/oop/multiple-inheritance.php
     - [8] https://www.programiz.com/python-programming/multiple-inheritance
     - [9] https://pythonflood.com/python-multiple-inheritance-concept-of-mixins-39897e1fe363
     - [10] https://realpython.com/oop-in-python-vs-java/
     - [11] https://softwareengineering.stackexchange.com/questions/100993/multiple-inheritance-use-cases
     - [12] https://en.wikipedia.org/wiki/Multiple_inheritance
     - [13] https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
     - [14] https://stackoverflow.com/questions/7371765/overview-of-differences-between-inheritance-in-python-and-java
     - [15] https://www.youtube.com/watch?v=1-JBFJ8Xar0
     - [16] https://docs.python.org/3/tutorial/classes.html
     - [17] https://softwareengineering.stackexchange.com/questions/441290/what-is-the-use-of-multiple-inheritance-in-languages-like-c-and-python
     - [18] https://realpython.com/inheritance-composition-python/
     - [19] https://www.w3schools.com/python/python_inheritance.asp
     - [20] https://coderanch.com/t/776418/languages/multiple-inheritance-Python-diamond-Java
     - [21] https://www.datacamp.com/tutorial/python-inheritance
     - [22] https://stackoverflow.com/questions/31478542/when-does-multiple-inheritance-come-in-handy
     - [23] https://www.youtube.com/watch?v=Q8YlYHjksLo
     - [24] https://www.reddit.com/r/learnpython/comments/j3ji6h/is_inheritance_really_bad_practice/
     - [25] https://www.krayonnz.com/user/doubts/detail/61cecb93cecf1c00406d04b3/what-are-the-advantages-and-disadvantages-of-multiple-inheritance
     - [26] https://stackoverflow.com/questions/766441/what-are-the-pros-and-cons-of-having-multiple-inheritance
     - [27] https://stackoverflow.com/questions/66038465/multiple-inheritance-python-issue
     - [28] https://30dayscoding.com/blog/advantages-and-disadvantages-of-inheritance
     - [29] https://www.datacamp.com/tutorial/super-multiple-inheritance-diamond-problem
     - [30] https://trainings.internshala.com/blog/python-inheritance/
     - [31] https://softwareengineering.stackexchange.com/questions/218458/is-there-any-real-reason-multiple-inheritance-is-hated
     - [32] https://d3kfrrhrj36vzx.cloudfront.net/images/1647972785374_xtwhyoqe.jpg?sa=X&ved=2ahUKEwjAt9auhr2MAxXhdPUHHS99OoYQ_B16BAgMEAI
     - [33] https://www.digitalocean.com/community/tutorials/multiple-inheritance-in-java
     - [34] https://www.scaler.com/topics/multiple-inheritance-in-python/
     - [35] https://how.dev/answers/what-is-multiple-inheritance-in-python
     - [36] https://towardsai.net/p/l/python-inheritance-common-practices-and-pitfalls-diamond-problem-mixins-and-others
     - [37] https://data-flair.training/blogs/python-multiple-inheritance/
     - [38] https://openstax.org/books/introduction-python-programming/pages/13-5-multiple-inheritance-and-mixin-classes


---------------

??? info "Use of AI"
        Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
        explanations, examples and/or structure suggestions. All information has been verified, edited and completed by the
        author.
