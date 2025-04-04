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

2. Multiple inheritance: Python supports multiple inheritance, while Java only allows single inheritance for classes (
   though it supports multiple interface implementation).

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
   


---------------

??? info "Use of AI"
        Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
        explanations, examples and/or structure suggestions. All information has been verified, edited and completed by the
        author.