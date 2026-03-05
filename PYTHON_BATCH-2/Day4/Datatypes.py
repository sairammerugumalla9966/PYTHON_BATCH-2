
'''
Docstring for Day4.Datatypes



# DATA TYPES IN PYTHON

## What is a Data Type? (Python Object Model)

# Simple definition

A **data type** tells Python:

* what kind of data a value holds
* what operations can be performed on it



# Python Object Model (VERY IMPORTANT 🔥)
In Python: Everything is an object

That means:
* Numbers are objects
* Strings are objects
* Lists, functions, even classes are objects
'''
# Example:

x = 10
#print(type(x))

name="sairam"
#print(type(name))

marks = [80, 85, 90]
names = ["Ram", "John", "Aldrin",23,89.99]
print(names)

names = ["Ram", "John", "Aldrin",23,89.99,66]
print(names)

'''
Output:
<class 'int'>


Here:

* `10` is an **object**
* `int` is its **data type (class)**


# Variables **don’t store values**, they **reference objects**



## Built-in Data Types (Categories)
Python groups data types into **6 main categories**:

| Category | Examples                |
| -------- | ----------------------- |
| Numeric  | int, float, complex     |
| Sequence | str, list, tuple, range |
| Mapping  | dict                    |
| Set      | set, frozenset          |
| Boolean  | bool                    |
| None     | NoneType                |



# NUMERIC DATA TYPES

## int (Integer)
Whole numbers (positive / negative / zero)

age = 25
salary = -10000


# Real-time example

* Age
* Number of students
* OTP digits


## float (Decimal numbers)


price = 99.75
temperature = 36.5


# Real-time example

* Bank balance
* Percentage
* Measurements


## complex (Rare but useful)

z = 3 + 5j


Used in:
* Electrical engineering
* Scientific calculations


# SEQUENCE DATA TYPES

Sequence = **ordered collection of elements**

## str (String)
Text data

name = "Sairam"
msg = 'Hello Python'


# Real-time examples
* Username
* Email
* Address

Strings are **immutable** (cannot be changed)


##  list (Mutable sequence)

marks = [80, 85, 90]
names = ["Ram", "John", "Aldrin",23,89.99]



# Real-time examples

* Student list
* Products in cart
* API response data

Can change values
Can add/remove elements



## tuple (Immutable sequence)

coordinates = (17.385, 78.4867)

# Real-time examples

* Latitude & longitude
* Fixed configuration values

Faster than list
Cannot modify values



## range

numbers = range(1, 6)

Used in:

* loops
* iteration

for i in range(1, 6):
    print(i)


    
# MAPPING DATA TYPE

# dict (Dictionary)
Key-value pair data


student = {
    "name": "Sairam",
    "age": 25,
    "course": "Python"
}


# Real-time examples

* JSON data
* Database records
* API responses

Fast lookup
Keys must be unique




# SET DATA TYPES
## set

Unordered + unique elements

skills = {"Python", "SQL", "Python"}

Output:
{'Python', 'SQL'}


# Real-time examples

* Unique emails
* Removing duplicates
* Permission lists



# frozenset (Immutable set)

permissions = frozenset(["read", "write"])

Used when:
* Data must not change
* Security rules


# BOOLEAN DATA TYPE
## bool (True / False)

is_logged_in = True
has_permission = False

# true 
# false

# Real-time examples

* Login status
* Feature enable/disable
* Validation checks


# NONE DATA TYPE

## NoneType

Represents **no value**
result = None


### Real-time examples

* Empty database result
* Function returns nothing
* Default value

def func():
    pass

print(func())   # None


# TYPE CASTING IN PYTHON
Converting one data type to another

# Implicit Type Casting (Automatic)
Python does it **automatically**

a = 10      # int
b = 2.5     # float
c = a + b
print(c)
print(type(c))


Output:
12.5
<class 'float'>


int → float (safe conversion)


# Invalid implicit casting


a = 10
b = "20"
print(a + b)

Error:
TypeError: unsupported operand type(s)
Python **will not guess** string → number


## Explicit Type Casting (Manual)

You force the conversion

# int()

x = int("100")




# String must contain digits only

# Error case:

int("abc")        # ValueError


# float()

price = float("99.75")


# str()

age = 25
msg = "Age is " + str(age)


# list()

text = "Python"
chars = list(text)

Output:
['P', 'y', 't', 'h', 'o', 'n']



# tuple(), set()

nums = [1, 2, 3]
print(tuple(nums))
print(set(nums))


# REAL-WORLD TYPE CASTING SCENARIOS

# User Input (MOST IMPORTANT 🔥)

age = input("Enter age: ")
print(type(age))   # str

Fix:
age = int(input("Enter age: "))



# Calculations

qty = int(input("Enter quantity: "))
price = float(input("Enter price: "))
total = qty * price




# INTERVIEW ONE-LINERS 

**Everything in Python is an object**
**Lists are mutable, tuples are immutable**
**Implicit casting happens only when safe**
**User input is always string**
**None represents absence of value**


'''

# dir() lists all attributes and methods available for an object.


# varibale , declaration , input , output , key words , identidiers 
#datatypes (numneric ---> int , float , complex )
#sequence (string , list , tuple)
#mapping (dictionary)
#set (set)
#boolean (bool)
#None 
#Mutable --> can be changed
#immutable ---> can't be changed 



fs = frozenset([1, 2, 3, "abc"])
print(fs)