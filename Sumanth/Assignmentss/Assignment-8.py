#1) #Write a program that takes a list of numbers and uses built-in functions to print:
#
# * Maximum value
# * Minimum value
# * Sum of elements
# * Length of the list

numbers = list(map(int, input("Enter the list of numbers: ").split()))

print(max(numbers))
print(min(numbers))
print(sum)
print(len(numbers))

# output:
# Enter the list of numbers: 1 2 3 4
# 4
# 1
# 10
# 4


# ====
# 2)User-Defined Max, Min, Sum (Without Built-ins)

# **Question:**
# Write your own functions to calculate:

# * Maximum
# * Minimum
# * Sum

# Do NOT use max(), min(), sum().

# **Test Case 1:**
# Input:
# [4, 8, 1, 9]

# Expected Output:
# Maximum: 9
# Minimum: 1
# Sum: 22

# **Test Case 2:**
# Input:
# [-5, -2, -10]

# Expected Output:
# Maximum: -2
# Minimum: -10
# Sum: -17


num = list(map(int,input("enter the numebrs: ").split()))


def maximum(num):
    max_value = num[0]
    for i in num:
        if i > max_value:
            max_value = i
    return max_value

print(maximum("maximum: ", num))

def minimum(num):
    min_value = num[0]
    for i in num:
        if i < min_value:
            min_value = i
    return min_value

print(minimum("minimum: ",num))
    
def summization(num):
    sum = 0
    for i in num:
        sum+=i
    return sum
print(summization("sum: ", num))


# output:
# ==
# enter numbers:4 8 1 9
# Maximum: 9
# Minimum: 1
# sum: 22

# enter numbers:-5 -2 -10
# [-5, -2, -10]
# Maximum: -2
# Minimum: -10
# sum: -17

# ========SECTION 2: PARAMETERS & ARGUMENTS

# 3)greet(name)

# **Question:**
# Create a function greet(name) that prints a greeting message.

# **Test Case 1:**
# Input:
# greet("Sairam")

# Expected Output:
# Hello Sairam! Welcome to Python class.

# **Test Case 2:**
# Input:
# greet("Anjali")

# Expected Output:
# Hello Anjali! Welcome to Python class.

#method-1
name = input("enter your name: ")
def greet(name):
    message =  "Hello" + " " + name+'!'+ " " + "welcome to python class." 
    return message

print(greet(name))

# output: 
# enter your name: sumanth
# Hello sumanth! Welcome to Python class

#method-2 using formatting strings

def greet(name):
    return f"Hello {name}! Welcome to Python class"

print(greet("sumanth"))

# output:
# Hello sumanth! Welcome to Python class

# ====
# 4)calculate_total(price, quantity)

# **Question:**
# Create a function that returns total amount.

# **Test Case 1:**
# Input:
# calculate_total(100, 3)

# Expected Output:
# 300

# **Test Case 2:**
# Input:
# calculate_total(250, 2)

# Expected Output:
# 500

def tot(price,quantity):
    total_amount = price * quantity
    return total_amount
print(tot(250,2))

# output:
# 500

# ====

# 5)create_account(name, role="User")

# **Question:**
# Create a function with default role.

# **Test Case 1:**
# Input:
# create_account("Rahul")

# Expected Output:
# Account created for Rahul with role User

# **Test Case 2:**
# Input:
# create_account("AdminUser", "Admin")

# Expected Output:
# Account created for AdminUser with role Admin


def create_account(name,role = "software developer"):
    message = f"Account created for {name} with {role}"
    return message
print(create_account("sumanth"))

# output:
# Account created for sumanth with software developer

# ====
# 6) Print vs Return (Square)

# **Question:**
# Create:

# * One function that prints square
# * One function that returns square

# **Test Case 1:**

# Input:
# square_print(5)

# Output:
# 25

def square(s):
    return s*s

print(square(5))

# OUTPUT:
# ==
# 25

def square(s):
    print(s*s)

square(5)

# OUTPUT:
# =====
# 25


# Input:
    
result = square(5)
print(result * 10)

# Output:
# 250

def square_return(x):
    return x * x

result  = square_return(5)
print(result * 10)

# OUTPUT:
# ===
# 250


# ====
# 7) Function Chaining

# **Question:**
# Create two functions: add(a, b) and multiply(a, b).
# Call multiply using result of add.

# **Test Case 1:**
# Input:
# multiply(add(2,3),4)

# Expected Output:
# 20

def add(a , b):
    return(a + b)

def multiply(a , b):
    return(a*b)

result = multiply(add(2 , 3) , 4)

print(result)

# OUTPUT:
# ===
# 20


# **Test Case 2:**
# Input:
# multiply(add(10,5),2)

# Expected Output:
# 30

def add(a , b):
    return(a + b)

def multiply(a , b):
    return(a*b)

result = multiply(add(10 , 5) , 2)

print(result)

# OUTPUT:
# ==
# 30

# ==== LOGICAL THINKING WITH FUNCTIONS

# 8)Even & Odd Counter

# **Question:**
# Write a function that returns count of even and odd numbers.

# **Test Case 1:**
# Input:
# [1,2,3,4,5]

# Expected Output:
# Even count: 2
# Odd count: 3

num = list(map(int, input("enter a list: ").split(",")))

def count(num):
    even_count = 0
    odd_count = 0
    
    for i in num:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

even, odd = count(num)

print("even_count: ", even)
print("odd_count: ", odd)

# OUTPUT:
# ========
# enter numbers:1,2,3,4,5
# even_count: 2
# odd_count: 3

# =====
# 9.Palindrome Checker

# **Question:**
# Create function is_palindrome(word).
# Return True if palindrome else False.

# **Test Case 1:**
# Input:
# is_palindrome("madam")

# Expected Output:
# True

def is_palindrome(name):
    if name == name[::-1]:
        return True
    else:
        return False
print(is_palindrome("madam"))

# OUTPUT:
# ====
# True

# **Test Case 2:**
# Input:
# is_palindrome("python")

# Expected Output:
# False

def is_palindrome(name):
    if name == name[::-1]:
        return True
    else:
        return False

print(is_palindrome("python"))

# OUTPUT:
# ====
# False

# =============

# 10)Factorial Using Recursion

# **Question:**
# Write a recursive function to find factorial.

# **Test Case 1:**
# Input:
# factorial(5)

# Expected Output:
# 120

# **Test Case 2:**
# Input:
# factorial(4)

# Expected Output:
# 24


def factio(num):

    if num == 1:
        return 1
    else:
        return num * factio(num-1)
    
print(factio(5))

# output:
# 120

# ======

# 11)Fibonacci Using Recursion

# **Question:**
# Print first N Fibonacci numbers.

# **Test Case 1:**
# Input:
# n = 5

# Expected Output:
# 0 1 1 2 3

# **Test Case 2:**
# Input:
# n = 7

# Expected Output:
# 0 1 1 2 3 5 8

num = int(input("Enter the number: "))
def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)
    
for i in range(num):
    print(fib(i),end=" ")

# output:

# 0 1 1 2 3 5 8 


# ==============

# 12)Sum of Digits (Recursion)

# **Question:**
# Return sum of digits using recursion.

# **Test Case 1:**
# Input:
# 1234

# Expected Output:
# 10

# **Test Case 2:**
# Input:
# 567+

# Expected Output:
# 18

def sum_of_digits(num):
    
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_digits(num//10)
    
print(sum_of_digits(1234))


# output:
# 10

# ===================

# 13)Reverse String (Recursion)

# **Question:**
# Reverse string using recursion.

# **Test Case 1:**
# Input:
# "python"

# Expected Output:
# "nohtyp"

# **Test Case 2:**
# Input:
# "madam"

# Expected Output:
# "madam"

name = input("Enter your name: ")
def rever(name):
    
    if name == "":
        return ""
    else:
        return rever(name[1:]) + name[0]
    
print(rever(name))

# output:
# Enter your name: madam
# madam


# ===============

# 14)Countdown Using Recursion

# **Question:**
# Print countdown using recursion.

# **Test Case 1:**
# Input:
# countdown(3)

# Expected Output:
# 3
# 2
# 1
# Done!

# **Test Case 2:**
# Input:
# countdown(5)

# Expected Output:
# 5
# 4
# 3
# 2
# 1
# Done!

def countdown(num):
    if num == 0:
        print("Done!")
    else:
        print(num)
        countdown(num-1)
countdown(5)

# output:
# 5
# 4
# 3
# 2
# 1
# Done!

# ==============

# 15) Power Function Using Recursion

# **Question:**
# Find power without using ** operator.

# **Test Case 1:**
# Input:
# power(2,3)

# Expected Output:
# 8

# **Test Case 2:**
# Input:
# power(5,2)

# Expected Output:
# 25

# **Test Case 3:**
# Input:
# power(3,0)

# Expected Output:
# 1

def power(num,pow):
    
    if num == 0:
        return 0
    if pow == 0:
        return 1
    else:
        return num ** pow

print(power(6,0))


# output:
# 1

# **Test Case 2:**
# Input:
# power(5,2)


def power(num,pow):
    
    if num == 0:
        return 0
    if pow == 0:
        return 1
    else:
        return num ** pow

print(power(5,2))

# output:
# 25
