#  Python Placement Questions

---

# 1. Python Basics

## Print

```python
print("Hello World")
print(10)
print(10 + 20)
```

---

# 2. Comments

```python
# Single-line comment

"""
Multi-line
comment
"""
```

---

# 3. Variables

Python does not require declaring the data type.

```python
name = "Athmik"
age = 20
marks = 85.5
is_student = True
```

Check type:

```python
print(type(name))
print(type(age))
```

---

# 4. Data Types

## Main Data Types

```python
int       # 10
float     # 10.5
str       # "Hello"
bool      # True / False
complex   # 2 + 3j
```

## Collection Types

```python
list      # [1, 2, 3]
tuple     # (1, 2, 3)
set       # {1, 2, 3}
dict      # {"name": "Athmik"}
```

---

# 5. Type Conversion

```python
x = "10"

a = int(x)
b = float(x)
c = str(10)
```

Examples:

```python
int(10.5)      # 10
float(10)      # 10.0
str(100)       # "100"
```

---

# 6. Input

```python
name = input("Enter name: ")
print(name)
```

`input()` always returns a string.

```python
age = int(input("Enter age: "))
```

---

# 7. Operators

## Arithmetic

```python
+     # Addition
-     # Subtraction
*     # Multiplication
/     # Division
//    # Floor division
%     # Modulus
**    # Power
```

Example:

```python
10 // 3    # 3
10 % 3     # 1
2 ** 3     # 8
```

## Comparison

```python
== 
!=
>
<
>=
<=
```

## Logical

```python
and
or
not
```

Example:

```python
age = 20

print(age > 18 and age < 30)
```

## Assignment

```python
x = 10
x += 5
x -= 2
x *= 2
x /= 2
```

## Membership

```python
in
not in
```

```python
"a" in "apple"       # True
5 in [1, 2, 5]       # True
```

## Identity

```python
is
is not
```

`==` checks **value**.

`is` checks **object identity**.

---

# 8. Conditional Statements

## if

```python
age = 20

if age >= 18:
    print("Adult")
```

## if-else

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## if-elif-else

```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")
```

---

# 9. Ternary Operator

Short form of if-else:

```python
result = "Pass" if marks >= 40 else "Fail"
```

---

# 10. Loops

## for loop

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

## range()

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Example:

```python
range(1, 10)
range(1, 10, 2)
```

---

## while loop

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

# 11. break, continue, pass

## break

Stops the loop.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

## continue

Skips current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

## pass

Does nothing.

```python
if age > 18:
    pass
```

---

# 12. Strings

```python
name = "Athmik"
```

## Indexing

```python
name[0]
name[-1]
```

## Slicing

```python
name[0:3]
name[:3]
name[2:]
name[::-1]
```

Reverse string:

```python
name[::-1]
```

---

## Important String Methods

```python
upper()
lower()
strip()
replace()
split()
join()
find()
count()
startswith()
endswith()
```

Examples:

```python
text = " hello "

text.strip()
text.upper()
text.lower()
text.replace("hello", "hi")
```

---

# 13. f-Strings

Recommended way to format strings.

```python
name = "Athmik"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

---

# 14. Lists

List is **ordered, mutable, and allows duplicates**.

```python
numbers = [10, 20, 30, 40]
```

## Access

```python
numbers[0]
numbers[-1]
```

## Change

```python
numbers[0] = 100
```

## Important Methods

```python
append()
extend()
insert()
remove()
pop()
clear()
sort()
reverse()
index()
count()
```

Examples:

```python
numbers.append(50)

numbers.insert(1, 15)

numbers.remove(20)

numbers.pop()

numbers.sort()

numbers.reverse()
```

---

# 15. List Slicing

```python
numbers[1:4]
numbers[:3]
numbers[2:]
numbers[::-1]
```

---

# 16. List Comprehension

Very important for interviews.

Normal:

```python
squares = []

for i in range(5):
    squares.append(i ** 2)
```

List comprehension:

```python
squares = [i ** 2 for i in range(5)]
```

With condition:

```python
even = [i for i in range(10) if i % 2 == 0]
```

---

# 17. Tuples

Tuple is **ordered and immutable**.

```python
numbers = (10, 20, 30)
```

Access:

```python
numbers[0]
```

Tuple unpacking:

```python
a, b, c = (10, 20, 30)
```

Single-element tuple:

```python
x = (10,)
```

---

# 18. Sets

Set stores **unique values**.

```python
numbers = {1, 2, 3, 3}

print(numbers)
```

Output:

```text
{1, 2, 3}
```

Important methods:

```python
add()
remove()
discard()
union()
intersection()
difference()
```

Example:

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)
a.intersection(b)
a.difference(b)
```

---

# 19. Dictionaries

Dictionary stores:

```text
key : value
```

Example:

```python
student = {
    "name": "Athmik",
    "age": 20,
    "marks": 85
}
```

Access:

```python
student["name"]
```

Safer:

```python
student.get("name")
```

Add/update:

```python
student["age"] = 21
student["city"] = "Udupi"
```

Delete:

```python
student.pop("city")
```

Important methods:

```python
keys()
values()
items()
get()
update()
pop()
```

Loop:

```python
for key, value in student.items():
    print(key, value)
```

---

# 20. Functions

Basic syntax:

```python
def greet():
    print("Hello")

greet()
```

## Parameters

```python
def greet(name):
    print(f"Hello {name}")

greet("Athmik")
```

## Return

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

---

# 21. Default Arguments

```python
def greet(name="User"):
    print(f"Hello {name}")

greet()
greet("Athmik")
```

---

# 22. Keyword Arguments

```python
def student(name, age):
    print(name, age)

student(age=20, name="Athmik")
```

---

# 23. *args

Used for multiple positional arguments.

```python
def add(*numbers):
    return sum(numbers)

print(add(10, 20, 30))
```

Inside the function, `args` is a tuple.

---

# 24. **kwargs

Used for multiple keyword arguments.

```python
def display(**data):
    print(data)

display(name="Athmik", age=20)
```

Inside the function, `kwargs` is a dictionary.

---

# 25. Lambda Function

Small anonymous function.

```python
square = lambda x: x ** 2

print(square(5))
```

Another example:

```python
add = lambda a, b: a + b
```

---

# 26. map()

Applies a function to every element.

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

---

# 27. filter()

Filters elements based on a condition.

```python
numbers = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

---

# 28. enumerate()

Gives index + value.

```python
names = ["A", "B", "C"]

for index, name in enumerate(names):
    print(index, name)
```

---

# 29. zip()

Combines multiple iterables.

```python
names = ["A", "B", "C"]
marks = [80, 90, 70]

for name, mark in zip(names, marks):
    print(name, mark)
```

---

# 30. Exception Handling

Basic syntax:

```python
try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
```

## Multiple exceptions

```python
try:
    x = int(input())

except ValueError:
    print("Invalid input")

except Exception as e:
    print(e)
```

## finally

Always executes.

```python
try:
    print("Hello")

except:
    print("Error")

finally:
    print("Finished")
```

## else

Runs if no exception occurs.

```python
try:
    x = 10 / 2

except:
    print("Error")

else:
    print("Success")
```

---

# 31. File Handling

## Read

```python
with open("data.txt", "r") as file:
    data = file.read()

print(data)
```

## Write

```python
with open("data.txt", "w") as file:
    file.write("Hello")
```

## Append

```python
with open("data.txt", "a") as file:
    file.write("\nPython")
```

Modes:

```text
r = read
w = write
a = append
x = create
```

---

# 32. Modules

A module is a Python file containing reusable code.

```python
import math

print(math.sqrt(25))
```

Import specific function:

```python
from math import sqrt

print(sqrt(25))
```

Alias:

```python
import numpy as np
```

---

# 33. Important Built-in Functions

Know these:

```python
print()
input()
len()
type()
id()
range()
sum()
max()
min()
sorted()
abs()
round()
enumerate()
zip()
map()
filter()
any()
all()
```

Examples:

```python
numbers = [10, 20, 30]

len(numbers)
sum(numbers)
max(numbers)
min(numbers)
```

---

# 34. sorted() vs sort()

`sort()` modifies the original list.

```python
numbers.sort()
```

`sorted()` returns a new sorted object.

```python
new_numbers = sorted(numbers)
```

Descending:

```python
sorted(numbers, reverse=True)
```

---

# 35. Mutable vs Immutable

## Mutable

Can be changed after creation.

```text
list
dict
set
```

## Immutable

Cannot be changed after creation.

```text
int
float
str
tuple
bool
```

Interview question:

> Is a tuple mutable?

**No.**

---

# 36. Shallow Copy vs Reference

Be careful:

```python
a = [1, 2, 3]
b = a
```

Both refer to the same list.

Use:

```python
b = a.copy()
```

or:

```python
b = a[:]
```

---

# 37. `==` vs `is`

```python
a = [1, 2]
b = [1, 2]

print(a == b)   # True
print(a is b)   # False
```

`==` → values are equal.

`is` → same object in memory.

---

# 38. Scope

## Local Variable

```python
def test():
    x = 10
```

`x` exists inside the function.

## Global Variable

```python
x = 10

def test():
    print(x)
```

---

# 39. Recursion

A function calling itself.

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Important:

**Base condition is required.**

---

# 40. Iterators

An iterator produces values one at a time.

```python
numbers = iter([1, 2, 3])

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

Important:

```python
iter()
next()
```

---

# 41. Generators

Generators use `yield`.

```python
def numbers():
    yield 1
    yield 2
    yield 3

for n in numbers():
    print(n)
```

Difference:

```text
return → returns a value and ends function

yield → produces values one at a time
```

---

# 42. Decorators

A decorator modifies/enhances a function.

Basic syntax:

```python
def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper
```

Using decorator:

```python
@decorator
def hello():
    print("Hello")
```

---

# 43. Object-Oriented Programming

## Class

Blueprint for creating objects.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

Object:

```python
s1 = Student("Athmik")

s1.display()
```

---

# 44. Constructor

`__init__()` is commonly used as the constructor/initializer.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

# 45. self

`self` refers to the current object.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

# 46. Four Pillars of OOP

## Encapsulation

Combining data and methods inside a class.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

## Inheritance

One class inherits another.

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):
    pass
```

## Polymorphism

Same method name, different behavior.

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")
```

## Abstraction

Hiding implementation details and exposing necessary functionality.

Commonly implemented using:

```python
from abc import ABC, abstractmethod
```

---

# 47. Class Variable vs Instance Variable

```python
class Student:

    college = "SMVITM"       # Class variable

    def __init__(self, name):
        self.name = name      # Instance variable
```

Class variable is shared.

Instance variable belongs to each object.

---

# 48. `@staticmethod`

Does not require `self`.

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(10, 20))
```

---

# 49. `@classmethod`

Receives `cls`.

```python
class Student:

    college = "SMVITM"

    @classmethod
    def show_college(cls):
        print(cls.college)
```

---

# 50. Special / Dunder Methods

Methods surrounded by double underscores.

Examples:

```python
__init__()
__str__()
__len__()
__add__()
```

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
```

---

# 51. `__name__ == "__main__"`

Used to check whether a Python file is being run directly.

```python
if __name__ == "__main__":
    print("Program started")
```

---

# 52. Python `*` and `**`

## In function calls

```python
numbers = [1, 2, 3]

print(*numbers)
```

`*` unpacks a list/tuple.

Dictionary:

```python
data = {
    "name": "Athmik",
    "age": 20
}

def student(name, age):
    print(name, age)

student(**data)
```

`**` unpacks a dictionary.

---

# 53. Dictionary Comprehension

```python
squares = {x: x**2 for x in range(5)}
```

Output:

```python
{
    0: 0,
    1: 1,
    2: 4,
    3: 9,
    4: 16
}
```

---

# 54. Set Comprehension

```python
squares = {x**2 for x in range(5)}
```

---

# 55. `any()` and `all()`

## any()

Returns `True` if at least one condition is true.

```python
numbers = [1, 3, 5, 8]

print(any(x % 2 == 0 for x in numbers))
```

## all()

Returns `True` if every condition is true.

```python
numbers = [2, 4, 6]

print(all(x % 2 == 0 for x in numbers))
```

---

# 56. Common Interview Coding Patterns

## Reverse a string

```python
text = "Python"

print(text[::-1])
```

## Check palindrome

```python
text = "madam"

if text == text[::-1]:
    print("Palindrome")
```

## Find largest

```python
numbers = [10, 20, 5, 40]

print(max(numbers))
```

## Find second largest

```python
numbers = [10, 20, 5, 40]

unique = list(set(numbers))
unique.sort()

print(unique[-2])
```

## Count characters

```python
text = "hello"

for char in set(text):
    print(char, text.count(char))
```

## Count frequency using dictionary

```python
text = "hello"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
```

---

# 57. Swap Variables

Python allows direct swapping.

```python
a = 10
b = 20

a, b = b, a
```

---

# 58. Check Even/Odd

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# 59. Prime Number

```python
n = 7

if n < 2:
    print("Not Prime")
else:

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            print("Not Prime")
            break

    else:
        print("Prime")
```

---

# 60. Factorial

```python
n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)
```

---

# 61. Fibonacci

```python
a = 0
b = 1

for i in range(10):
    print(a)

    a, b = b, a + b
```

---

# 62. Important Differences

## List vs Tuple

```text
List:
Mutable
Uses []

Tuple:
Immutable
Uses ()
```

## Set vs List

```text
List:
Ordered
Duplicates allowed

Set:
Unique elements
No duplicate values
```

## `append()` vs `extend()`

```python
a = [1, 2]

a.append([3, 4])
# [1, 2, [3, 4]]

a = [1, 2]

a.extend([3, 4])
# [1, 2, 3, 4]
```

## `remove()` vs `pop()`

```python
remove(value)
pop(index)
```

## `sort()` vs `sorted()`

```text
sort()     → changes original list
sorted()   → returns sorted object
```

---

# 63. Common Python  Questions

### What is Python?

A high-level, interpreted, general-purpose programming language known for readable syntax and a large ecosystem.

### Is Python compiled or interpreted?

Python source code is typically compiled to bytecode and then executed by the Python virtual machine. Calling Python simply "interpreted" is an oversimplification.

### What is PEP 8?

Python's style guide for writing readable and consistent Python code.

### What is indentation?

Indentation defines code blocks in Python.

```python
if x > 10:
    print(x)
```

### What is dynamic typing?

You don't need to explicitly declare a variable's type.

```python
x = 10
x = "Hello"
```

### What is duck typing?

Python generally focuses on what an object **can do** rather than its explicit type.

### What is `None`?

`None` represents the absence of a value.

```python
x = None
```

### What is `pass`?

A placeholder that performs no operation.

### What is `yield`?

Used to create generators and produce values lazily.

### What is a lambda?

A small anonymous function.

### What is a decorator?

A mechanism for modifying or extending function/class behavior without directly changing the original implementation.

---

# 64. Python Data Structure Revision

```text
LIST
[1, 2, 3]
Mutable
Ordered
Duplicates allowed

TUPLE
(1, 2, 3)
Immutable
Ordered
Duplicates allowed

SET
{1, 2, 3}
Mutable
Unique elements

DICTIONARY
{"name": "Athmik"}
Key-value pairs
Keys must be hashable
```

---

# 65.  Syntax to Remember

```python
# Function
def function_name():
    pass

# Class
class Student:
    pass

# If
if condition:
    pass
elif condition:
    pass
else:
    pass

# For
for i in range(10):
    pass

# While
while condition:
    pass

# Exception
try:
    pass
except Exception:
    pass
finally:
    pass

# File
with open("file.txt", "r") as file:
    data = file.read()

# List comprehension
result = [x for x in numbers if x > 5]

# Lambda
square = lambda x: x ** 2

# Generator
def numbers():
    yield 1
```

---
