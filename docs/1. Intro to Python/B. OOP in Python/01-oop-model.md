# 1. Python's OOP Model

Python's OOP model provides a flexible approach to object-oriented programming that balances simplicity with power. Let
me describe Python's model first, then compare it to Java's approach.

## Python's OOP Model

Python implements object-oriented programming through classes and objects. In Python, a class serves as a blueprint that
defines attributes (data) and methods (functions) that objects of that class will possess[1]. Everything in Python is an
object, including numbers, strings, and functions[2].

Python's OOP model is built on four fundamental pillars:

1. **Encapsulation**: Python uses a convention-based approach with underscores (e.g., `_private_var`) rather than strict
   access modifiers[4].

2. **Inheritance**: Python supports both single and multiple inheritance, allowing a class to inherit attributes and
   methods from one or more parent classes[2][3].

3. **Polymorphism**: This allows methods to be implemented differently in different classes, enabling objects of
   different classes to respond to the same method call in class-specific ways[3].

4. **Abstraction**: Python allows you to hide complex implementation details and show only the necessary features of an
   object[2].

## Comparing Python's OOP to Java's OOP

### Type System

- **Python**: Uses dynamic typing where variable types are determined at runtime. Variables can change types throughout
  program execution[4][5].
- **Java**: Uses static typing where all variables must be explicitly declared with their types before use[4][5].

### Syntax and Structure

- **Python**: Uses indentation to define code blocks. Classes are defined with the `class` keyword and constructor with
  `__init__`[4][6].
- **Java**: Uses curly braces to define code blocks. Classes are typically defined in separate files with constructors
  named after the class[4][7].

### Inheritance

- **Python**: Supports multiple inheritance, allowing a class to inherit from multiple parent classes[2][3].
- **Java**: Supports only single inheritance for classes but allows multiple interface implementation[4].

### Encapsulation

- **Python**: Doesn't have strict access modifiers. Uses naming conventions (underscores) to indicate private
  attributes[4][8].
- **Java**: Enforces strict access modifiers (public, private, protected) to control access to class members[3][4].

### Performance

- **Python**: Generally slower due to its interpreted nature and dynamic typing[5][9].
- **Java**: Typically faster due to compilation to bytecode and Just-In-Time (JIT) compilation[5][9].

### Design Philosophy

- **Python**: Supports OOP but doesn't force it. You can write procedural or functional code without classes[8].
- **Java**: Designed as a pure OOP language where everything must be within a class[8].

In summary, while both languages implement the core principles of OOP, Python offers a more flexible, convention-based
approach with dynamic typing, while Java provides a stricter, more structured approach with static typing and explicit
access control.

??? note "References"
    
      - [1] https://www.datacamp.com/tutorial/python-oop-tutorial
      - [2] https://www.linkedin.com/pulse/python-four-pillars-object-oriented-programming-benjamin-b-phiri
      - [3] https://www.tutorialspoint.com/python/python_oops_concepts.htm
      - [4] https://www.datacamp.com/blog/python-vs-java
      - [5] https://www.imaginarycloud.com/blog/python-vs-java
      - [6] https://www.freecodecamp.org/news/how-to-use-oop-in-python/
      - [7] https://www.youngwonks.com/blog/python-vs-java
      - [8] https://www.activestate.com/blog/java-versus-python-key-programming-differences-in-2021/
      - [9] https://raygun.com/blog/java-vs-python/
      - [10] https://www.youtube.com/watch?v=q2SGW2VgwAM
      - [11] https://www.freecodecamp.org/news/object-oriented-programming-in-python/
      - [12] https://www.w3schools.com/python/python_classes.asp
      - [13] https://www.programiz.com/python-programming/object-oriented-programming
      - [14] https://www.wscubetech.com/resources/python/oops-concepts
      - [15] https://docs.python.org/3/reference/datamodel.html
      - [16] https://www.youtube.com/watch?v=ZVTuWsrjvyU
      - [17] https://www.pythoncheatsheet.org/cheatsheet/oop-basics
      - [18] https://www.freecodecamp.org/news/object-oriented-programming-python/
      - [19] https://www.youtube.com/watch?v=Ej_02ICOIgs
      - [20] https://files.realpython.com/media/Object-Oriented-Programming-OOP-in-Python-3_Watermarked.0d29780806d5.jpg?sa=X&ved=2ahUKEwi8ks_097yMAxXuCLkGHZFBI9cQ_B16BAgHEAI
      - [21] https://raygun.com/blog/images/java-vs-python/feature.png?sa=X&ved=2ahUKEwifuZT297yMAxUdklYBHX65EI0Q_B16BAgMEAI
      - [22] https://realpython.com/oop-in-python-vs-java/
      - [23] https://www.reddit.com/r/javahelp/comments/13qow9l/are_javas_oop_concepts_much_different_than_pythons/
      - [24] https://www.youtube.com/watch?v=dYLSFF2gjSs
      - [25] https://www.coursera.org/articles/python-vs-java
      - [26] https://dev.to/terrythreatt/the-four-principles-of-object-oriented-programming-in-python-1jbi
      - [27] https://www.geekster.in/articles/oops-concepts-in-python/
      - [28] https://realpython.com/python3-object-oriented-programming/
    
    

---------------

??? info "Use of AI"
        Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
        explanations, examples and/or structure suggestions. All information has been verified, edited and completed by the
        author.