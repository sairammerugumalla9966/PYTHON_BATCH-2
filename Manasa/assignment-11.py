# Assignment 11
# =============================================

# EXCEPTION HANDLING – ASSIGNMENT
# ================================================================

# ERRORS VS EXCEPTIONS
# ------------------------------------------------

### 1. Identify Error Type

# **Question:**
# Write a program that intentionally produces:

# * A Syntax Error
# * A ZeroDivisionError
# * A NameError

a = 10
print(a

# OUTPUT:
# ========
# SyntaxError: '(' was never closed

a = 10
b = 0
print(a/b)

# OUTPUT:
# ========          
# ZeroDivisionError: division by zero

a = 10
print(b)

# OUTPUT:
# ========
# NameError: name 'b' is not defined

# Explain which are errors and which are exceptions.

# **Task:**
# Handle only the runtime exceptions properly using try-except.

try:
    a=10
    b=0
    print(a/b)

except ZeroDivisionError:
    print("Error Occured due to ZeroDivisionError")

# OUTPUT:
# ========
# Error Occured due to ZeroDivisionError

try:
    a = 10
    print(x)

except NameError:
    print("Error Occured due to NameError")

# OUTPUT:
# ========
# Error Occured due to NameError

# ================================================================

# ### 2. Division Calculator with Exception Handling

# **Question:**
# Write a program that:

# * Takes two numbers from user
# * Performs division
# * Handles ZeroDivisionError and ValueError

# **Test Case 1:**
# Input:
# 10
# 2

# Expected Output:
# Result: 5.0

number1 = int(input("enter first number"))
number2 = int(input("enter second number"))

try:
    Result = number1 / number2
    print(Result)

except (ZeroDivisionError,ValueError):
    print("error occured")

# OUTPUT:
# =========
# enter first number10
# enter second number2
# 5.0

# **Test Case 2:**
# Input:
# 10
# 0

# Expected Output:
# Error: Cannot divide by zero.

number1 = int(input("enter first number"))
number2 = int(input("enter second number"))

try:
    result = number1/number2
    print(result)

except ZeroDivisionError:
    print("cannot divide by zero")

except NameError:
    print("error occured")

# OUTPUT:
# =========
# enter first number10
# enter second number0
# cannot divide by zero

# **Test Case 3:**
# Input:
# 10
# abc

# Expected Output:
# Error: Invalid input. Please enter numbers only.

number1 = int(input("enter first number"))
number2 = int(input("enter second number"))

try:
    result = number1/number2
    print(result)

except ZeroDivisionError:
    print("error occured")

except ValueError:
    print("Invalid input.please enter numbers only")

# OUTPUT:
# =========
# ValueError: invalid literal for int() with base 10: 'abc'

# ================================================================

## SECTION 2: try, except, else, finally

### 3. Number Validation Program

# **Question:**
# Take input from user and:

# * Convert to integer
# * Print square of number

# Use:

# * try
# * except
# * else
# * finally

# **Test Case 1:**
# Input: 5

# Expected Output:
# Square: 25
# Execution completed.

try:
    number = int(input("enter a number:"))

except ValueError:
    print("enter valid number for an integer")

else:
    result = number*number
    print("Square :" , result)

finally:
    print("Execution completed")

# OUTPUT:
# =========
# enter a number:5
# Square : 25
# Execution completed

# **Test Case 2:**
# Input: abc

# Expected Output:
# Invalid input.
# Execution completed.

try:
    number = int(input("enter a number:"))

except ValueError:
    print("Invalid input")

else:
    result = number*number
    print("Square :" , result)

finally:
    print("Execution completed")

# OUTPUT:
# =========
# enter a number:abc
# Invalid input
# Execution completed

# ================================================================

### 4. File Reader with finally

# **Question:**
# Write a program to:

# * Open a file
# * Read contents
# * Handle FileNotFoundError
# * Ensure file is closed using finally

try:
    f = open("sample.txt" , "r")
    print(f.read())

except FileNotFoundError:
    print("File not found")

finally:
      f.close()

#  OUTPUT:
# =========  
#  Manasa Annapureddy       
   
# ================================================================

### 5. Multiple Exception Handling

# **Question:**
# Write a program that:

# * Takes index input from user
# * Prints element from list
# * Handles IndexError and ValueError

# **Test Case 1:**
# List: [10, 20, 30]
# Input: 1

# Output:
# Element: 20

number = [10 , 20 , 30]

try:
    index = int(input("enter index value:"))
    print("Element:" , number[index])

except IndexError:
    print("Index value is not correct")

except ValueError:
    print("value is out of bound")

# OUTPUT:
# =========
# enter index value:1
# Element: 20

# **Test Case 2:**
# Input: 5

# Output:
# Error: Index out of range.

number = [10 , 20 , 30]

try:
    index = int(input("enter index value:"))
    print("Element:" , number[index])

except IndexError:
    print("Index out of range")

except ValueError:
    print("value is out of bound")

# OUTPUT:
# =========
# enter index value:5
# Index out of range

# **Test Case 3:**
# Input: abc

# Output:
# Error: Invalid index input.

number = [10 , 20 , 30]

try:
    index = int(input("enter index value:"))
    print("Element:" , number[index])

except IndexError:
    print("Index out of range")

except ValueError:
    print("Invalid index input")

# OUTPUT:
# =========
# enter index value:abc
# Invalid index input

# ================================================================

### 6. ATM Withdrawal Simulation

# **Question:**
# Simulate ATM withdrawal:

# * Ask user for withdrawal amount
# * If amount > balance → raise error
# * Handle invalid input

# Balance = 5000

# **Test Case 1:**
# Input: 2000

# Output:
# Withdrawal successful. Remaining balance: 3000

balance = 5000
try:
    amount = int(input("enter amount:"))
    if amount > balance:
        raise ValueError("Insufficient balance")
    else:
        balance-=amount
        print("Withdrawal successfull.Remaining balance" , balance)

except ValueError:
    print("Invalid input")

# OUTPUT:
# =========
# enter amount:2000
# Withdrawal successfull.Remaining balance 3000

# **Test Case 2:**
# Input: 6000

# Output:
# Error: Insufficient balance.

balance = 5000
try:
    amount = int(input("enter amount:"))
    if amount > balance:
        raise Exception("Insufficient balance")
    else:
        balance-=amount
        print("Withdrawal successfull.Remaining balance" , balance)

except Exception as f:
    print(f)

# OUTPUT:
# =========
# enter amount:6000
# Insufficient balance

# ================================================================

### 7. Login System with Limited Attempts

# **Question:**
# Create login system:

# * Correct password = "admin123"
# * Allow only 3 attempts
# * Raise exception after 3 failed attempts

# Expected Output:
# Access denied after 3 failed attempts.

password = "admin123"
attempts = 4

try:
    if attempts<=3:
        print("login successfull")

    else:
        raise Exception("Access denied after 3 failed attempts")

except Exception as f:
    print(f)

# OUTPUT:
# =========
# Access denied after 3 failed attempts

# ================================================================

## SECTION 3: CUSTOM EXCEPTIONS

### 8. Custom Age Validation Exception

# **Question:**
# Create custom exception:

# ```
# InvalidAgeError
# ```

# If age < 18 → raise exception.

# **Test Case 1:**
# Input: 20
# Output: Access granted.

class InvalidAgeError(Exception):
    pass
try:
    age = int(input("enter age:"))
    if age<18:
        raise InvalidAgeError("Age must be 18 or above")

    else:
        print("Access granted")

except InvalidAgeError as f:
    print(f)

# OUTPUT:
# =========
# enter age:20
# Access granted

# **Test Case 2:**
# Input: 15
# Output: InvalidAgeError: Age must be 18 or above.

class InvalidAgeError(Exception):
    pass
try:
    age = int(input("enter age:"))
    if age<18:
        raise InvalidAgeError("Age must be 18 or above")

    else:
        print("Access granted")

except InvalidAgeError as f:
    print(f)

# OUTPUT:
# =========
# enter age:15
# Age must be 18 or above

# ================================================================

### 9. Custom Login Exception

# **Question:**
# Create custom exception:

# ```
# LoginError
# ```

# Raise if username is incorrect.

# Expected Output Example:
# LoginError: Invalid username


class LoginError(Exception):
    pass

username = "ManasaAnnapureddy"
try:
    username1 = input("enter name:")
    if username == username1:
        print("valid username")

    else:
        raise LoginError("LoginError:Invalid username")

except LoginError as f:
    print(f)

# OUTPUT:
# =========
# enter name:manu
# LoginError:Invalid username

# ================================================================

### 10. Bank Minimum Balance Exception

# **Question:**
# Create custom exception:

# ```
# MinimumBalanceError
# ```

# If withdrawal makes balance < 1000 → raise exception.

class MinimumBalanceError(Exception):
    pass
balance = 5000

try:
    withdrawal = int(input("enter withdrawl amount:"))
    balance-=withdrawal
    if balance>1000:
        print(balance)

    else:
        raise MinimumBalanceError("MinimumBalanceError")

except MinimumBalanceError as f:
    print(f)

# OUTPUT:
# =========
# enter withdrawl amount:6000
# MinimumBalanceError

# ================================================================

### 11. Negative Number Not Allowed

# **Question:**
# Create custom exception:

# ```
# NegativeNumberError
# ```

# Raise exception if user enters negative number.

class NegativeNumberError(Exception):
    pass

number  = int(input("enter a number:"))

try:
    if number>=0:
        print("positive number")
    else:
        raise NegativeNumberError("NegativeNumberError")

except NegativeNumberError as a:
    print(a)

# OUTPUT:
# =========
# enter a number:-2
# NegativeNumberError

# enter a number:2
# positive number

# ================================================================

### 12. Student Marks Validation

# **Question:**
# Create custom exception:

# ```
# InvalidMarksError
# ```

# Marks should be between 0 and 100.

# **Test Case 1:**
# Input: 85
# Output: Valid marks.

# **Test Case 2:**
# Input: 120
# Output: InvalidMarksError: Marks must be between 0 and 100.

class InvalidMarksError(Exception):
    pass

marks = int(input("enter marks:"))

try:
    if marks>0 and marks<100:
        print("valid marks")

    else:
        raise InvalidMarksError

except:
    print("InvalidMarksError: Marks must be between 0 and 100.")

# OUTPUT:
# =========
# # enter marks:85
# # valid marks

# enter marks:120
# InvalidMarksError: Marks must be between 0 and 100.

# ================================================================

## SECTION 4: INTERMEDIATE LOGIC-BASED EXCEPTION HANDLING

### 13. Nested Try-Except Block

**Question:**
# Create program:

# * Take number input
# * Divide 100 by number
# * Inside that, convert another input to integer
# * Use nested try-except

# Handle:

# * ZeroDivisionError
# * ValueError

# ================================================================

### 14. Custom Exception with finally Block

# **Question:**
# Create custom exception:

# ```
# PasswordLengthError
# ```

# If password length < 6 → raise exception
# Ensure finally block always prints:
# "Validation process completed."

class PasswordLengthError(Exception):
    pass

password = input("enter password:")

try:
    if len(password) <6:
        raise PasswordLengthError("PasswordLengthError")
        

    else:
        print(password)
        

except PasswordLengthError as f:
    print("Error:" , f)

finally:
    print("validation process completed")

# OUTPUT:
# =========
# enter password:manu
# Error: PasswordLengthError
# validation process completed
    
# ================================================================

### 15. Mini Project: Online Payment System

# **Question:**
# Simulate payment system:

# * Input card number
# * Input amount
# * Raise custom exceptions for:

#   * Invalid card number (length not 16)
#   * Insufficient balance
#   * Invalid amount (non-numeric)

# Use:

# * try
# * multiple except
# * else
# * finally
# * custom exceptions

# Expected Output Example:
# Payment successful.
# Transaction completed.

# OR

# InvalidCardError: Card number must be 16 digits.
# Transaction completed.