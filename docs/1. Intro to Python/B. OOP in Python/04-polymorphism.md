# 4. Polymorphism

Polymorphism in Python operates quite differently from Java, primarily due to Python's dynamic typing system and its
emphasis on behavior over explicit type declarations.

## Polymorphism in Python

Polymorphism in Python is the ability of different objects to respond to the same method or function call in different
ways. Python implements polymorphism through several mechanisms:

### Duck Typing

Python's most distinctive approach to polymorphism is duck typing, which follows the principle: *"If it walks like a 
duck and quacks like a duck, then it must be a duck."* This means Python focuses on an object's behavior (methods and
attributes) rather than its specific type[4][7].

For example:

```python
def make_it_sound(obj):
    obj.sound()


class Duck:
    def sound(self):
        print("Quack!")


class Person:
    def sound(self):
        print("I'm quacking like a duck!")


# Both objects work with the same function
duck = Duck()
person = Person()
make_it_sound(duck)  # Output: Quack!
make_it_sound(person)  # Output: I'm quacking like a duck!
```

The `make_it_sound` function doesn't care about the object's type; it only cares that the object has a `sound()`
method[4].

### Function Polymorphism

Python's built-in functions often exhibit polymorphic behavior. The `len()` function is a prime example:

```python
print(len("Hello"))  # 5 (string)
print(len([1, 2, 3, 4]))  # 4 (list)
print(len({"a": 1, "b": 2}))  # 2 (dictionary)
```

The same function behaves differently based on the input type[2].

### Operator Overloading

Python supports operator overloading through special methods like `__add__`, `__mul__`, etc.:

```python
# + operator with integers
a = 10 + 15  # 25

# + operator with strings
b = 'A' + 'B'  # 'AB'
```

## Polymorphism in Java vs. Python

The key differences in how polymorphism works in these languages include:

### Method Overloading

Java supports compile-time (static) polymorphism through method overloading:

```java
public static int add(int a, int b) {
    return a + b;
}

public static int add(int a, int b, int c) {
    return a + b + c;
}
```

Python doesn't support true method overloading. When you define multiple methods with the same name, only the last one
is considered[5]. Instead, Python typically uses default parameters:

```python
def add(a, b, c=None):
    if c is None:
        return a + b
    else:
        return a + b + c
```

### Type Checking

Java implements polymorphism through strict inheritance hierarchies and interfaces. It relies on static typing and type
checking at compile time.

Python uses duck typing, focusing on what an object can do rather than what it is. It doesn't require explicit
inheritance relationships for polymorphic behavior[3][6].

### Implementation Approach

Java's polymorphism is explicit and requires formal class relationships:

```java
@Override
public void makeSound() {
    System.out.println("Dog barks");
}
```

Python's polymorphism is implicit and more flexible:

```python
class Bird:
    def fly(self):
        pass


class Airplane:
    def fly(self):
        print("Airplane flies")


# Both can be used interchangeably despite no inheritance relationship
def perform_flight(flying_object):
    flying_object.fly()
```

## Duck Typing in Detail

Duck typing is a core concept in Python that emphasizes an object's behavior over its type. The principle states that "
if it walks like a duck and quacks like a duck, then it must be a duck"[4][6][7].

This approach offers several advantages:

- Creates more flexible and reusable code
- Supports polymorphism without rigid type hierarchies
- Results in simpler, more concise code

However, it also has disadvantages:

- Can lead to runtime errors if expected methods are missing
- May make code harder to understand without type hints

Duck typing is particularly powerful when creating generic functions that can work with any object that implements a
specific interface:

```python
class Duck:
    def quack(self):
        print("Quack!")


class Car:
    def quack(self):
        print("I can quack, too!")


def quacks(obj):
    obj.quack()


# Both work despite being completely different classes
quacks(Duck("Donald"))
quacks(Car("Tesla"))
```

This flexibility is a fundamental aspect of Python's design philosophy, allowing developers to focus more on what
objects can do rather than what they are.

??? note "References"

      - [1] https://codedamn.com/news/python/polymorphism-in-python-with-an-example
      - [2] https://www.almabetter.com/bytes/tutorials/python/python-inheritance-and-polymorphism
      - [3] https://www.datacamp.com/blog/python-vs-java
      - [4] https://www.kdnuggets.com/duck-duck-code-an-introduction-to-pythons-duck-typing
      - [5] https://stackoverflow.com/questions/61138173/polymorphism-in-python-vs-polymorphism-in-java
      - [6] https://builtin.com/articles/python-duck-typing
      - [7] https://realpython.com/duck-typing-python/
      - [8] https://realpython.com/python3-object-oriented-programming/
      - [9] https://www.reddit.com/r/learnpython/comments/13sdpoq/anyone_have_a_solid_understanding_in_polymorphism/
      - [10] https://www.youtube.com/watch?v=tHN8I_4FIt8
      - [11] https://www.w3schools.com/python/python_polymorphism.asp
      - [12] https://herovired.com/learning-hub/blogs/java-vs-python/
      - [13] https://www.reddit.com/r/javahelp/comments/13qow9l/are_javas_oop_concepts_much_different_than_pythons/
      - [14] https://edbennett.github.io/python-oop-novice/06-duck/index.html
      - [15] https://en.wikipedia.org/wiki/Duck_typing
      - [16] https://stackoverflow.com/questions/4205130/what-is-duck-typing
      - [17] https://www.reddit.com/r/learnpython/comments/14p49ua/confusion_about_duck_typing/
      - [18] https://www.youtube.com/watch?v=rIWQ4584Uqk
      - [19] https://www.simplilearn.com/polymorphism-in-python-article
      - [20] https://www.edureka.co/blog/polymorphism-in-python/
      - [21] https://www.programiz.com/python-programming/polymorphism
      - [22] https://discuss.python.org/t/polymorphism-in-python/25178
      - [23] https://www.activestate.com/blog/java-versus-python-key-programming-differences-in-2021/
      - [24] https://www.rose-hulman.edu/class/cs/csse220/201130/Resources/Python_vs_Java.html
      - [25] https://realpython.com/oop-in-python-vs-java/
      - [26] https://www.youtube.com/watch?v=Qe03kCuTMoU
      - [27] https://ioflood.com/blog/duck-typing/


---------------

??? info "Use of AI"
        Page written in part with the help of an AI assistant, mainly using Perplexity AI. The AI was used to generate
        explanations, examples and/or structure suggestions. All information has been verified, edited and completed by the
        author.