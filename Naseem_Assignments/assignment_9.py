'''
ASSIGNMENT 8
===================================================================================

# FUNCTIONS & RECURSION 
---------------------------------------------
## SECTION 1: BUILT-IN VS USER-DEFINED FUNCTIONS
===================================================================================

### 1. Built-in Functions Practice

**Question:**
Write a program that takes a list of numbers and uses built-in functions to print:

* Maximum value
* Minimum value
* Sum of elements
* Length of the list

**Test Case 1:**
Input:
[10, 20, 5, 40]

Expected Output:
Maximum: 40
Minimum: 5
Sum: 75
Length: 4

**Test Case 2:**
Input:
[3, 3, 3]

Expected Output:
Maximum: 3
Minimum: 3
Sum: 9
Length: 3

---
===============================================================================================
### 2. User-Defined Max, Min, Sum (Without Built-ins)

**Question:**
Write your own functions to calculate:

* Maximum
* Minimum
* Sum

Do NOT use max(), min(), sum().

**Test Case 1:**
Input:
[4, 8, 1, 9]

Expected Output:
Maximum: 9
Minimum: 1
Sum: 22

**Test Case 2:**
Input:
[-5, -2, -10]

Expected Output:
Maximum: -2
Minimum: -10
Sum: -17

=========================================================================================
## SECTION 2: PARAMETERS & ARGUMENTS
=========================================================================================

### 3. greet(name)

**Question:**
Create a function greet(name) that prints a greeting message.

**Test Case 1:**
Input:
greet("Sairam")

Expected Output:
Hello Sairam! Welcome to Python class.

**Test Case 2:**
Input:
greet("Anjali")

Expected Output:
Hello Anjali! Welcome to Python class.

========================================================

### 4. calculate_total(price, quantity)

**Question:**
Create a function that returns total amount.

**Test Case 1:**
Input:
calculate_total(100, 3)

Expected Output:
300

**Test Case 2:**
Input:
calculate_total(250, 2)

Expected Output:
500

=====================================================================================

### 5. create_account(name, role="User")

**Question:**
Create a function with default role.

**Test Case 1:**
Input:
create_account("Rahul")

Expected Output:
Account created for Rahul with role User

**Test Case 2:**
Input:
create_account("AdminUser", "Admin")

Expected Output:
Account created for AdminUser with role Admin

===========================================================================
## SECTION 3: RETURN VS PRINT
===========================================================================

### 6. Print vs Return (Square)

**Question:**
Create:

* One function that prints square
* One function that returns square

**Test Case 1:**

Input:
square_print(5)

Output:
25

Input:
result = square_return(5)
print(result * 10)

Output:
250

**Test Case 2:**
Input:
square_print(3)

Output:
9

=========================================================================================

### 7. Function Chaining

**Question:**
Create two functions: add(a, b) and multiply(a, b).
Call multiply using result of add.

**Test Case 1:**
Input:
multiply(add(2,3),4)

Expected Output:
20

**Test Case 2:**
Input:
multiply(add(10,5),2)

Expected Output:
30

==================================================================
## SECTION 4: LOGICAL THINKING WITH FUNCTIONS
===================================================================

### 8. Even & Odd Counter

**Question:**
Write a function that returns count of even and odd numbers.

**Test Case 1:**
Input:
[1,2,3,4,5]

Expected Output:
Even count: 2
Odd count: 3

**Test Case 2:**
Input:
[2,4,6]

Expected Output:
Even count: 3
Odd count: 0

=============================================================================

### 9. Palindrome Checker

**Question:**
Create function is_palindrome(word).
Return True if palindrome else False.

**Test Case 1:**
Input:
is_palindrome("madam")

Expected Output:
True

**Test Case 2:**
Input:
is_palindrome("python")

Expected Output:
False

==============================================================================
## SECTION 5: RECURSION
==============================================================================

### 10. Factorial Using Recursion

**Question:**
Write a recursive function to find factorial.

**Test Case 1:**
Input:
factorial(5)

Expected Output:
120

**Test Case 2:**
Input:
factorial(4)

Expected Output:
24

===========================================================================================

### 11. Fibonacci Using Recursion

**Question:**
Print first N Fibonacci numbers.

**Test Case 1:**
Input:
n = 5

Expected Output:
0 1 1 2 3

**Test Case 2:**
Input:
n = 7

Expected Output:
0 1 1 2 3 5 8

======================================================================================

### 12. Sum of Digits (Recursion)

**Question:**
Return sum of digits using recursion.

**Test Case 1:**
Input:
1234

Expected Output:
10

**Test Case 2:**
Input:
567

Expected Output:
18

===============================================================================

### 13. Reverse String (Recursion)

**Question:**
Reverse string using recursion.

**Test Case 1:**
Input:
"python"

Expected Output:
"nohtyp"

**Test Case 2:**
Input:
"madam"

Expected Output:
"madam"

=================================================================================
### 14. Countdown Using Recursion
**Question:**
Print countdown using recursion.

**Test Case 1:**
Input:
countdown(3)

Expected Output:
3
2
1
Done!

**Test Case 2:**
Input:
countdown(5)

Expected Output:
5
4
3
2
1
Done!
=================================================================================
### 15. Power Function Using Recursion
**Question:**
Find power without using ** operator.

**Test Case 1:**
Input:
power(2,3)

Expected Output:
8

**Test Case 2:**
Input:
power(5,2)

Expected Output:
25

**Test Case 3:**
Input:
power(3,0)

Expected Output:
1
====================================================================================


'''

# ### 1. Built-in Functions Practice

# **Question:**
# Write a program that takes a list of numbers and uses built-in functions to print:

# * Maximum value
# * Minimum value
# * Sum of elements
# * Length of the list



# Write a program that takes a list of numbers and uses built-in functions to print:

# * Maximum value
# * Minimum value
# * Sum of elements
# * Length of the list

# **Test Case 1:**
# Input:
# [10, 20, 5, 40]

# Expected Output:
# Maximum: 40
# Minimum: 5
# Sum: 75
# Length: 4

lst = [10, 20, 5, 40]

print("Maximum: ", max(lst))
print("Minimun: ", min(lst))
print("Sum of elements: ", sum(lst))
print("Length of the List: ", len(lst))

# **Test Case 2:**
# Input:
# [3, 3, 3]

# Expected Output:
# Maximum: 3
# Minimum: 3
# Sum: 9
# Length: 3

lst = list(map(int, input("Enter elements separated by space: ").split()))

print("List:", lst)
print("Sum:", sum(lst))
print("Minimum:", min(lst))
print("Maximum:", max(lst))
print("Length:", len(lst))

# 2. User-Defined Max, Min, Sum (Without Built-ins)
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

lst = list(map(int, input("Enter elements separated by space: ").split()))
print("List: ", lst)

def Max(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max
print("Maximum: ", Max(lst))

def Min(lst):
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min
print("Minimum: ", Min(lst))

def Sum(lst):
    sum = 0
    for i in lst:
        sum+= i
    return sum
print("Sum : ", Sum(lst))


### 3. greet(name)
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

def greet(Name):
    
    msg = "Hello" + Name + "!" + "Welcome to Python Class"
    return msg
print(greet("Sairam"))

### 4. calculate_total(price, quantity)
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

def calculate_total(price, quantity):
    total = price * quantity
    return total
print(calculate_total(100, 3))

### 5. create_account(name, role="User")

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

def create_account(name, role='user'):
    msg = "Account Created For " + name + " " + "With Role " + role
    return msg
print(create_account("Rahul"))
print(create_account("AdminUser", "Admin"))



### 6. Print vs Return (Square)
# **Question:**
# Create:

# * One function that prints square
# * One function that returns square

# **Test Case 1:**

# Input:
# square_print(5)

# Output:
# 25

# Input:
# result = square_return(5)
# print(result * 10)

# Output:
# 250

# **Test Case 2:**
# Input:
# square_print(3)

# Output:
# 9

def square_ret(num):
    square = num * num
    return(square)
print(square_ret(5))

result = square_ret(5)
print(result * 10)

### 7. Function Chaining

# **Question:**
# Create two functions: add(a, b) and multiply(a, b).
# Call multiply using result of add.

# **Test Case 1:**
# Input:
# multiply(add(2,3),4)

# Expected Output:
# 20

# **Test Case 2:**
# Input:
# multiply(add(10,5),2)

# Expected Output:
# 30

def add(a, b):
    sum = a + b 
    return sum
print(add(2,3))

def mul(a, b):
    mul = a * b 
    return mul
print(mul(add(2,3), 4))


### 8. Even & Odd Counter

# **Question:**
# Write a function that returns count of even and odd numbers.

# **Test Case 1:**
# Input:
# [1,2,3,4,5]

# Expected Output:
# Even count: 2
# Odd count: 3

# **Test Case 2:**
# Input:
# [2,4,6]

# Expected Output:
# Even count: 3
# Odd count: 0

num = list(map(int,input("Enter a list : ").split(",")))

def count(num):
    eve_count = 0 
    odd_count = 0
    for i in num:
        if i % 2 == 0:
            eve_count += 1
        else:
            odd_count += 1

    return "Even Count: " + str(eve_count) + "\nOdd Count: " + str(odd_count)
        
print(count(num))


### 9. Palindrome Checker
# **Question:**
# Create function is_palindrome(word).
# Return True if palindrome else False.

# **Test Case 1:**
# Input:
# is_palindrome("madam")

# Expected Output:
# True

# **Test Case 2:**
# Input:
# is_palindrome("python")

# Expected Output:
# False

def Palindrome(Name):
    if Name == Name[::-1]:
        return True
    else:
        return False

print(Palindrome("Naseem"))
print(Palindrome("madam"))

### 10. Factorial Using Recursion

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

def Factorial(num):
    if num == 1:
        return 1
    else:
        return  num * Factorial(num - 1)

print(Factorial(5))


### 12. Sum of Digits (Recursion)

# **Question:**
# Return sum of digits using recursion.

# **Test Case 1:**
# Input:
# 1234

# Expected Output:
# 10

# **Test Case 2:**
# Input:
# 567

# Expected Output:
# 18

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n//10)
print(sum_of_digits(1234))

# 1234 % 10 --> 4 
# 1234 // 10 --> 

### 13. Reverse String (Recursion)

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

def reverse(name):
    if len(name) == 0:
        return name
    else:
        return reverse(name[1:]) + name[0]
print(reverse("Python"))

"""s[0]   → "p"        (first character)
s[1:]  → "ython"    (everything except first character)
"""

# # ### 14. Countdown Using Recursion
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
