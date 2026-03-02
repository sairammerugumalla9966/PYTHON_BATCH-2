# ASSIGNMENT 9
# ==================================================

# # LAMBDA & HIGHER-ORDER FUNCTIONS ASSIGNMENT
# ---

# ## SECTION 1: LAMBDA FUNCTIONS
# ---

# ### 1. Basic Lambda Function

# **Question:**
# Create a lambda function to find the square of a number.

# **Test Case 1:**
# Input:
# square = lambda x: x * x
# square(5)

# Expected Output:
# 25

# square = lambda x:x*x

# print(square(5))

# 25

# **Test Case 2:**
# square(8)

# Expected Output:
# 64

# square = lambda x:x*x

# print(square(8))

# 64

# ---

# ### 2. Lambda with Multiple Arguments

# **Question:**
# Create a lambda function to calculate the total price (price × quantity).

# **Test Case 1:**
# Input:
# total = lambda price, qty: price * qty
# total(100, 3)

# Expected Output:
# 300

# total = lambda price , qty: price * qty

# print(total(100 , 3))

# 300

# **Test Case 2:**
# total(250, 2)

# Expected Output:
# 500

# total = lambda price , qty : price * qty

# print(total(250 , 2))

# 500

# ---

# ### 3. Lambda with Conditional Expression

# **Question:**
# Create a lambda function that checks whether a number is even or odd.

# **Test Case 1:**
# Input:
# check = lambda x: "Even" if x % 2 == 0 else "Odd"
# check(10)

# Expected Output:
# Even

# check = lambda x:"Even" if x%2==0 else "odd"

# print(check(10))

# Even

# **Test Case 2:**
# check(7)

# Expected Output:
# Odd

# check = lambda x:"even" if x%2==0 else "odd"

# print(check(7))

# odd

# ---

# ## SECTION 2: HIGHER-ORDER FUNCTIONS

# (A higher-order function is a function that takes another function as an argument.)

# ---

# ### 4. Function as Argument

# **Question:**
# Create a function apply_operation(func, a, b)
# It should take a function and two numbers.

# **Test Case 1:**
# Input:
# apply_operation(lambda x, y: x + y, 5, 3)

# Expected Output:
# 8

# def apply_operation(func , a , b):
#     return func(a,b)

# result = apply_operation(lambda x , y : x+y , 5 ,3)
# print(result)

# 8

# **Test Case 2:**
# apply_operation(lambda x, y: x * y, 4, 6)

# Expected Output:
# 24

# def apply_operation(func , a , b):
#     return func(a , b)

# result = apply_operation(lambda x,y:x*y , 4 , 6)
# print(result)

# 24
# ---

# ### 5. Returning a Function

# **Question:**
# Create a function multiplier(n) that returns a function to multiply any number by n.

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

# ---

# ## SECTION 3: map()

# ---

# ### 6. Square All Numbers Using map()

# **Question:**
# Given a list of numbers, use map() to return a list of squares.

# **Test Case 1:**
# Input:
# [1, 2, 3, 4]

# Expected Output:
# [1, 4, 9, 16]

# num = [1 , 2 , 3 , 4]

# def square(x):
#     return x * x

# result = list(map(square,num))
# print(result)

# [1, 4, 9, 16]

# **Test Case 2:**
# Input:
# [5, 6, 7]

# Expected Output:
# [25, 36, 49]

# num = [5 , 6 , 7]

# def square(x):
#     return x * x

# result = list(map(square,num))
# print(result)

# [25, 36, 49]

# ---

# ### 7. Convert Strings to Uppercase Using map()

# **Question:**
# Convert a list of names to uppercase using map().

# **Test Case 1:**
# Input:
# ["sairam", "anjali", "rahul"]

# Expected Output:
# ["SAIRAM", "ANJALI", "RAHUL"]

# names = ["sairam" , "anjali" , "rahul"]

# def upper(s):
#     return s.upper()

# result = list(map(upper,names))
# print(result)

# ['SAIRAM', 'ANJALI', 'RAHUL']

# **Test Case 2:**
# Input:
# ["python", "django"]

# Expected Output:
# ["PYTHON", "DJANGO"]

# names = ["python" , "django"]

# def upper(s):
#     return s.upper()

# result = list(map(upper,names))
# print(result)

# ['PYTHON', 'DJANGO']

# ---

# ## SECTION 4: filter()

# ---

# ### 8. Filter Even Numbers

# **Question:**
# Use filter() to extract even numbers from a list.

# **Test Case 1:**
# Input:
# [1,2,3,4,5,6]

# Expected Output:
# [2,4,6]

# numbers = [1 , 2 , 3 , 4 , 5 , 6]
# def even(x):
#     return x%2==0

# result = list(filter(even,numbers))
# print(result)

# [2, 4, 6]

# **Test Case 2:**
# Input:
# [10,15,20,25]

# Expected Output:
# [10,20]

# ---

# numbers = [10 , 15 , 20 , 25]
# def even(x):
#     return x%2==0

# result = list(filter(even,numbers))
# print(result)

# [10, 20]

# ### 9. Filter Students with Passing Marks

# **Question:**
# Given a list of marks, filter students who scored 50 or above.

# **Test Case 1:**
# Input:
# [45, 67, 80, 30, 55]

# Expected Output:
# # [67, 80, 55]

# marks = [45 , 67 , 80 , 30 , 55]
# def student(x):
#     return x>=50

# result = list(filter(student,marks))
# print(result)

# [67, 80, 55]


# **Test Case 2:**
# Input:
# [90, 40, 49, 75]

# Expected Output:
# [90, 75]

# marks = [90 , 40 , 49 , 75]
# def student(x):
#     return x>=50

# result = list(filter(student,marks))
# print(result)

# [90, 75]

# ---

# ## SECTION 5: reduce()

# (Note: Import reduce from functools)

# ---

# ### 10. Find Sum of List Using reduce()

# **Question:**
# Use reduce() to find sum of elements.

# **Test Case 1:**
# Input:
# [1,2,3,4]

# Expected Output:
# 10

# from functools import reduce

# num = [1 , 2 , 3 , 4]

# def sum(x,y):
#     return x+y

# result = reduce(sum,num)
# print(result)

# 10

# **Test Case 2:**
# Input:
# [5,5,5]

# Expected Output:
# 15

# from functools import reduce

# num = [5 , 5 , 5]

# def sum(x,y):
#     return x+y

# result = reduce(sum,num)
# print(result)

# 15

# ---

# ### 11. Find Product of List Using reduce()

# **Question:**
# Use reduce() to find product of elements.

# **Test Case 1:**
# Input:
# [1,2,3,4]

# Expected Output:
# 24

# from functools import reduce
# numbers = [1,2,3,4]

# def product(x,y):
#     return x*y

# result = reduce(product,numbers)
# print(result)

# 24

# **Test Case 2:**
# Input:
# [2,3,5]

# Expected Output:
# 30

# from functools import reduce

# number = [2,3,5]
# def product(x,y):
#     return x*y

# result = reduce(product,number)
# print(result)

# 30

# ---

# ## SECTION 6: PRACTICAL REAL-TIME EXAMPLES

# ---

# ### 12. Apply 10% Discount Using map()

# **Question:**
# Given a list of prices, apply 10% discount to each price.

# **Test Case 1:**
# Input:
# [100, 200, 300]

# Expected Output:
# [90.0, 180.0, 270.0]

# numbers = [100 , 200 , 300]

# def discount(x):
#     return x*0.9

# result = list(map(discount,numbers))
# print(result)

# [90.0, 180.0, 270.0]

# **Test Case 2:**
# Input:
# [500, 1000]

# Expected Output:
# [450.0, 900.0]

# numbers = [500 , 1000]
# def discount(x):
#     return x*0.9

# result = list(map(discount,numbers))
# print(result)

# [450.0, 900.0]

# ---

# ### 13. Filter High Salary Employees

# **Question:**
# Given a list of salaries, filter salaries above 50,000.

# **Test Case 1:**
# Input:
# [30000, 60000, 45000, 80000]

# Expected Output:
# [60000, 80000]

# numbers = [30000 , 60000 , 45000 , 80000]
# def salary(x):
#     return x>50000

# result = list(filter(salary,numbers))
# print(result)

# [60000, 80000]

# **Test Case 2:**
# Input:
# [55000, 40000, 75000]

# Expected Output:
# [55000, 75000]

# numbers = [55000 , 40000 , 75000]
# def salary(x):
#     return x>50000

# result = list(filter(salary,numbers))
# print(result)

# [55000, 75000]

# ---

# ### 14. Calculate Total Bill Using reduce()

# **Question:**
# Given a list of item prices in cart, calculate total bill.

# **Test Case 1:**
# Input:
# [250, 150, 100]

# Expected Output:
# 500

# from functools import reduce
# numbers = [250 , 150 , 100]
# def total_Bill(x,y):
#     return x+y

# result = reduce(total_Bill,numbers)
# print(result)

# 500


# **Test Case 2:**
# Input:
# [999, 1]

# Expected Output:
# 1000

# from functools import reduce

# numbers = [999 , 1]

# def total_Bill(x,y):
#     return x+y

# result = reduce(total_Bill,numbers)
# print(result)

# 1000

# ---

# ### 15. Combined Example (map + filter)

# **Question:**
# Given a list of numbers:

# * First filter even numbers
# * Then square them using map()

# **Test Case 1:**
# Input:
# [1,2,3,4,5,6]

# Expected Output:
# [4,16,36]

# numbers = [1,2,3,4,5,6]
# def combined(x):
#     return x%2==0

# result = list(filter(combined,numbers))


# def square(result):
#     return result * result

# result1 = list(map(square,result))
# print(result1)

# [4, 16, 36]


# **Test Case 2:**
# Input:
# [10,15,20]

# Expected Output:
# [100,400]

# numbers = [10 , 15 , 20]

# def combined(x):
#     return x%2==0

# result = list(filter(combined,numbers))

# def square(result):
#     return result * result

# result1 = list(map(square,result))
# print(result1)

# [100, 400]