# Python - Variable Annotations
This repository provides examples and explanations of using type annotations in Python 3 for specifying variable types, function signatures, and the concept of duck typing. It also demonstrates how to validate your code using mypy, a popular static type checker for Python.

##  Contents
* Python - Variable Annotations
* Table of Contents
* Introduction to Type Annotations
* Variable Type Annotations
* Function Signature Annotations
* Understanding Duck Typing
* Validating Code with Mypy
* Authors
## Introduction to Type Annotations
Type annotations are a way to explicitly specify the expected types of variables and function return values in Python. While Python is dynamically typed, meaning you don't have to declare types explicitly, type annotations can provide better code clarity and help catch errors early.

## Variable Type Annotations
In this section, you will find examples of how to use type annotations to specify the types of variables:

```
name: str = "Alice"
age: int = 30
is_student: bool = True
```

Function Signature Annotations
Type annotations can also be applied to function signatures to indicate the expected types of parameters and return values:
```
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

Understanding Duck Typing
Duck typing is a concept in programming where the type or the class of an object is less important than the methods and properties it exposes. If an object walks like a duck and quacks like a duck, it's considered a duck.

For example:
```
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def pet_speak(pet):
    print(pet.speak())

dog = Dog()
cat = Cat()

pet_speak(dog)  # Output: "Woof!"
pet_speak(cat)  # Output: "Meow!"
```

## Validating Code with Mypy
Mypy is a static type checker for Python that can be used to analyze your code and catch type-related errors before runtime. To use mypy, first, install it:
```
pip install mypy
```
Then, run mypy to check your code:
```
mypy your_code.py
```
Make sure to replace your_code.py with the actual filename.

## Authors
![GitHub Contributors Image](https://contrib.rocks/image?repo=anacardona0220/holbertonschool-higher_level_programming) Ana Maria Cardona Botero - <a href="https://github.com/anacardona0220" target="_blank"> @anacardona0220</a> :genie_woman:![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=anacardona0220&show_icons=true)


