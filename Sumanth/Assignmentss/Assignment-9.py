# 1) Basic Lambda Function

# **Question:**
# Create a lambda function to find the square of a number.

# **Test Case 1:**
# Input:
# square = lambda x: x * x
# square(5)

# Expected Output:
# 25

# **Test Case 2:**
# square(8)

# Expected Output:
# 64


print((lambda x: x*x)(4))

# output:
# 16

result = (lambda x: x*x)
print(result(8))

# output:
# 64

# ===========
# 2) Create a lambda function to calculate the total price (price × quantity).

# **Test Case 1:**
# Input:
# total = lambda price, qty: price * qty
# total(100, 3)

# Expected Output:
# 300

# **Test Case 2:**
# total(250, 2)

# Expected Output:
# 500

#lambda function using multiple parameters

print((lambda price,quantity: price*quantity)(250,2))

# output:
# 500

print((lambda price,quantity: price*quantity)(100,3))

# output:
# 300

# =========
# **Lambda with Conditional Expression
# 3) Create a lambda function that checks whether a number is even or odd.

# **Test Case 1:**
# Input:
# check = lambda x: "Even" if x % 2 == 0 else "Odd"
# check(10)

# Expected Output:
# Even

# **Test Case 2:**
# check(7)

# Expected Output:
# Odd

(lambda num: print("even") if num%2==0 else print("odd"))(2)

# output:
# ----
# even

result = lambda num: print("even") if num%2==0 else print("odd")
result(7)

# output:
# ----
# odd

# =========

# 4) Create a function apply_operation(func, a, b)
# It should take a function and two numbers.

# **Test Case 1:**
# Input:
# apply_operation(lambda x, y: x + y, 5, 3)

# Expected Output:
# 8

# **Test Case 2:**
# apply_operation(lambda x, y: x * y, 4, 6)

# Expected Output:
# 24

def apply():
    return (lambda x,y: x + y)(4,6)

print(apply())

# output:
# ---
# 10

def apply_operation(func , a , b):
    return func(a,b)

result = apply_operation(lambda x , y : x+y , 4 ,6)
print(result)

# output:
# ---
# 24

# ==========

# Returning a Function

# 5)Create a function multiplier(n) that returns a function to multiply any number by n.

# **Test Case 1:**
# Input:
# double = multiplier(2)
# double(5)

# Expected Output:
# 10

# **Test Case 2:**
# triple = multiplier(3)
# triple(4)

# Expected Output:
# 12

def multiplier(n):
    def multiply(x):
        return n * x
    return multiply
    
result = multiplier(2)
print(result(5))

# output:
# 10

# ================

# 6.Square All Numbers Using map()

# **Question:**
# Given a list of numbers, use map() to return a list of squares.

# **Test Case 1:**
# Input:
# [1, 2, 3, 4]

# Expected Output:
# [1, 4, 9, 16]

# **Test Case 2:**
# Input:
# [5, 6, 7]

# Expected Output:
# [25, 36, 49]


numbers = [1,2,3,4]

def func(n):
    return n*n

print(list(map(func,numbers)))  #map is used to iterable the each and every item on the list


# output:
# ----
# [1,4,9,16]

# ==========
# 7)Convert Strings to Uppercase Using map()

# **Question:**
# Convert a list of names to uppercase using map().

# **Test Case 1:**
# Input:
# ["sairam", "anjali", "rahul"]

# Expected Output:
# ["SAIRAM", "ANJALI", "RAHUL"]

# **Test Case 2:**
# Input:
# ["python", "django"]

# Expected Output:
# ["PYTHON", "DJANGO"]


s = ["sumanth","Leo","Rocky"]

def upp(s):
    return s.upper()

print(list(map(upp,s)))

# output:

# ['SUMANTH', 'LEO', 'ROCKY']

# =========

# 8)Filter Even Numbers

# **Question:**
# Use filter() to extract even numbers from a list.

# **Test Case 1:**
# Input:
# [1,2,3,4,5,6]

# Expected Output:
# [2,4,6]

# **Test Case 2:**
# Input:
# [10,15,20,25]

# Expected Output:
# [10,20]

numbers = [1,2,3,4,5,6]

def even(n):
    return n % 2 == 0 

print(list(filter(even,numbers)))

# output:

# [2,4,6]

# =========

# 9) Filter Students with Passing Marks

# **Question:**
# Given a list of marks, filter students who scored 50 or above.

# **Test Case 1:**
# Input:
# [45, 67, 80, 30, 55]

# Expected Output:
# [67, 80, 55]

# **Test Case 2:**
# Input:
# [90, 40, 49, 75]

# Expected Output:
# [90, 75]

nums = [45, 67, 80, 30, 55]

def score(n):
    return n>=50

print(list(filter(score,nums)))

# output:

# [67, 80, 55]

# =======

# 10)Use reduce() to find sum of elements.

# **Test Case 1:**
# Input:
# [1,2,3,4]

# Expected Output:
# 10

# **Test Case 2:**
# Input:
# [5,5,5]

# Expected Output:
# 15

from functools import reduce
nums =  [5,5,5]

def sum_ele(a,b):
    return a+b

print(int(reduce(sum_ele,nums)))

# output:
# -----
# 15

# =======

# 11)Find Product of List Using reduce()

# Use reduce() to find product of elements.
# **Test Case 1:**
# Input:
# [1,2,3,4]

# Expected Output:
# 24

# **Test Case 2:**
# Input:
# [2,3,5]

# Expected Output:
# 30

from functools import reduce
nums = [2,3,5]

def prod(a,b):
    return a * b

print(int(reduce(prod,nums)))

# output:
# -----
# 30

# ==========

# 12) Apply 10% Discount Using map()

# **Question:**
# Given a list of prices, apply 10% discount to each price.

# **Test Case 1:**
# Input:
# [100, 200, 300]

# Expected Output:
# [90.0, 180.0, 270.0]

# **Test Case 2:**
# Input:
# [500, 1000]

# Expected Output:
# [450.0, 900.0]

nums = [100, 200, 300]

def pri(n):
    return n * 0.90

print(list(map(pri,nums)))

# output:
# ----
# [90.0, 180.0, 270.0]

# ==========

# 13)Filter High Salary Employees

# **Question:**
# Given a list of salaries, filter salaries above 50,000.

# **Test Case 1:**
# Input:
# [30000, 60000, 45000, 80000]

# Expected Output:
# [60000, 80000]

# **Test Case 2:**
# Input:
# [55000, 40000, 75000]

# Expected Output:
# [55000, 75000]

salaries =  [55000, 40000, 75000]

def fil(n):
    return n>50000

print(list(filter(fil,salaries)))

# output:
# ---
# [55000, 75000]

# =======

# 14) Calculate Total Bill Using reduce()

# **Question:**
# Given a list of item prices in cart, calculate total bill.

# **Test Case 1:**
# Input:
# [250, 150, 100]

# Expected Output:
# 500

# **Test Case 2:**
# Input:
# [999, 1]

# Expected Output:
# 1000

from functools import reduce

prices = [250,150,100]

def total_bill(x,y):
    return x + y

print(int(reduce(total_bill,prices)))

# output:
# -----
# 500

# ========

# 15) Combined Example (map + filter)

# **Question:**
# Given a list of numbers:

# * First filter even numbers
# * Then square them using map()

# **Test Case 1:**
# Input:
# [1,2,3,4,5,6]

# Expected Output:
# [4,16,36]

# **Test Case 2:**
# Input:
# [10,15,20]

# Expected Output:
# [100,400]

numbers = [1,2,3,4,5,6]

def is_even(n):
    return n % 2 == 0

result = list(filter(is_even,numbers))
# print(result)

def square(n):
    return n * n

print(list(map(square,result)))

# output:
# -----
# [4, 16, 36]