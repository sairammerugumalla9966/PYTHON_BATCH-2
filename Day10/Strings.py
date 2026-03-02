
'''
# STRINGS 

# STRINGS IN PYTHON

## What is a String?

# A "string" is an immutable sequence of Unicode characters.

name = "Python"
city = 'Hyderabad'

# **Immutable** → once created, it cannot be changed.

## Real-Time Uses

# User names
# Emails
# Passwords
# File paths
# API responses
# Messages & logs


## Example 1: User Name Storage

username = "sairam"
print(username)


## Example 2: Multiline String


address = """Hyderabad
Telangana
India"""
print(address)


## Example 3: Length of String

msg = "Welcome to Python"
print(len(msg))

## Example 4: Accessing a Character


language = "Python is my Favourite language."
print(language[0])
print(language[-1])



## Example 5: Immutability Proof

s = "Hello"
s = s + " World"
print(s)




# STRING METHODS (VERY IMPORTANT 🔥)

## Case Conversion Methods

# Example 1: `upper()` and `lower()`


text = "python"
print(text.upper())
print(text.lower())


## Example 2: `capitalize()` and `title()`


sentence = "python programming language"
print(sentence.capitalize()) # first word first letter will beconme capital (upper)
print(sentence.title())

## Whitespace & Replace Methods

## Example 3: `strip()`

email = "  user@gmail.com  "
print(email.strip())


## Example 4: `replace()`


msg = "I love Java"
print(msg.replace("Java", "Python"))

## Searching & Splitting

## Example 5: `find()` and `count()`


data = "python is easy"
print(data.find("is"))
print(data.count("o"))

## Example 6: `split()`

csv = "apple,banana,mango"
print(csv.split(","))



## Real-Time Example: Email Validation

email = "test@gmail.com"

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")


## INDEXING IN STRINGS

## What is Indexing?

# Accessing characters using **position numbers**.
# Index starts from **0**


## Example 1: Positive Indexing

word = "Python"
print(word[0])
print(word[3])


## Example 2: Negative Indexing

print(word[-1])
print(word[-3])


## Example 3: First and Last Character

name = "Sairam"
print(name[0])
print(name[-1])


## Example 4: Iterate Using Index

text = "Python"

for i in range(len(text)):
    print(text[i])


## Example 5: Character Validation

password = "Admin123"
print(password[0].isupper())


# SLICING IN STRINGS
#Syntax

# string[start : end : step]

## Example 1: Basic Slicing

word = "Python"
print(word[1:4])


## Example 2: Omit Start / End

print(word[:3])
print(word[3:])

## Example 3: Negative Slicing

print(word[-4:-1])

## Example 4: Step Value

print(word[::2])

## Example 5: Reverse String

print(word[::-1])

## Example: Mask Account Number

acc = "123456789012"
print("********" + acc[-4:])


# STRING FORMATTING (**)

## Method 1: `format()`

## Example 1


name = "Sairam"
age = 25

print("My name is {} and age is {}".format(name, age))


## Example 2: Positional Formatting
print("Name: {0}, Age: {1}".format(name, age))


## Example 3: Named Formatting
print("Name: {n}, Age: {a}".format(n=name, a=age))

## Method 2: f-Strings (MOST USED )

## Example 4: Simple f-String

print(f"My name is {name} and age is {age}")

## Example 5: Real-Time Invoice

item = "Laptop"
price = 50000
qty = 2

print(f"Item: {item}")
print(f"Total Amount: {price * qty}")


#  STRING IMMUTABILITY

s = "Python"
print(id(s))

s = s + "3"
print(id(s))

'''

s="sairam"
print(s)
s=s+"Hero"
print(s)

msg = "Welcome to Python"
print(len(msg))


text = "PythoN"
print(text.upper())
print(text.lower())


sentence = "python programming language"
print(sentence.capitalize()) # first word first letter will beconme capital (upper)
print(sentence.title())


csv = "apple banana mango sairam"
print(csv.split(" "))


# reverse of a string ??

name="Bahubali"
rev=" "
for char in name:
    rev=char+rev
print(rev)   

#username=" Sairam Merugumalla"

#for i in username:
    #print(username[-1])

## Example 4: Iterate Using Index

text = "Python"

for i in range(len(text)):
    print(text[i])



name = "Sairam"
age = 25
print("My name is {} and age is {}".format(name, age))
















