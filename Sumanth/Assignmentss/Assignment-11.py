# 1. Identify Error Type

# **Question:**
# Write a program that intentionally produces:

# * A Syntax Error
# * A ZeroDivisionError
# * A NameError

# Explain which are errors and which are exceptions.

# **Task:**
# Handle only the runtime exceptions properly using try-except.

#A Zero division error
try:
    a = 10
    print(a/0)
except:
    print("not valid")  #divided by zero because it runs during the runtime exceution
    
# ============
#Name error

# try:
#     #print(value)
# except NameError:
#     print("variable is not defined check ones")  #variable is not defined right but it exceutes runtime exception only
    
# #Syntax error
# if True
#     print("sumanth") #Errors is not handled in exceptions because it happens before the exceution

# =============

# 2. Division Calculator with Exception Handling

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

# **Test Case 2:**
# Input:
# 10
# 0

# Expected Output:
# Error: Cannot divide by zero.

# **Test Case 3:**
# Input:
# 10
# abc

# Expected Output:
# Error: Invalid input. Please enter numbers only.



try:
    a = int(input("Enter the number1: "))
    b = int(input("Enter the number2: "))
    result = a/b
    print(result)
    
except ZeroDivisionError:
    print("number cannot divided by zero")
    
except ValueError:
    print("Invalid input please enter numbers only")
 

#SECTION 2: try, except, else, finally

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

# **Test Case 2:**
# Input: abc

# Expected Output:
# Invalid input.
# Execution completed.

try:
    a = input("Enter the number: ")
    b = int(a)
    square = b * b  #try block runs only risky code if no error it goes to else block 

except ValueError:
    print("Invalid input") #if error in try block it comes to except block
else:
    print(f"square of {b}:",square) #no error in try block it exceutes the else block
finally:
    print("Exceution completed") #its always exceute when you run the program



# ### 4. File Reader with finally

# **Question:**
# Write a program to:

# * Open a file
# * Read contents
# * Handle FileNotFoundError
# * Ensure file is closed using finally

try:
    f = open("sample.txt","r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("file not respond")
    
finally:
    try:
        f.close()
        print("file closed successfully")
    except:
        pass


# 5. Multiple Exception Handling

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

# **Test Case 2:**
# Input: 5

# Output:
# Error: Index out of range.

# **Test Case 3:**
# Input: abc

# Output:
# Error: Invalid index input.

numbers = [10,20,30,2]

try:
    index = int(input("Enter a index number: "))
    print("The value is: ",numbers[index])
except IndexError:
    print("index is out of bound")
except ValueError:
    print("please enter valid index")


# 6. ATM Withdrawal Simulation

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

# **Test Case 2:**
# Input: 6000

# Output:
# Error: Insufficient balance.

balance = 10000
try:
    amount = int(input("Enter your withdrawl amount: "))
    if amount <= balance:
        withdrawl = balance - amount
        print("Withdrawl successful. Remaining balance: ",withdrawl)
    else:
        print("Error: Inssufficient balance")
except:
    print("invalid input")
    
# output:
# Enter your withdrawl amount: 1000
# Withdrawl successful. Remaining balance:  9000

# 7. Login System with Limited Attempts

# **Question:**
# Create login system:

# * Correct password = "admin123"
# * Allow only 3 attempts
# * Raise exception after 3 failed attempts

# Expected Output:
# Access denied after 3 failed attempts.

correct_password = "admin123"
attempts = 0
max_attempts=3
try:
    while attempts < max_attempts:   
        password = input("Enter the password: ")
    
        if password == correct_password:
            print("Access success")
            break
        else:
            attempts+=1
            print("password Incorrect")
    if attempts == max_attempts:       
        raise Exception("Acess Denied after 3 failed attempts")
except Exception as e:
    print(e)


#  8. Custom Age Validation Exception

# **Question:**
# Create custom exception:

# ```
# InvalidAgeError
# ```

# If age < 18 → raise exception.

# **Test Case 1:**
# Input: 20
# Output: Access granted.

# **Test Case 2:**
# Input: 15
# Output: InvalidAgeError: Age must be 18 or above.

try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Access Granted")
    if age <= 18:
        raise Exception("Invalid age Error: Age must be 18 or above")
except Exception as e:
    print(e)

#  9. Custom Login Exception

# **Question:**
# Create custom exception:

# ```
# LoginError
# ```

# Raise if username is incorrect.

# Expected Output Example:
# LoginError: Invalid username

class LoginError(Exception):  #We are inheriting from Exception
    pass

username = "sumanth"
try:
    new_username = input("Enter your username: ")
    
    if new_username != username:
        raise LoginError("Invalid username") #we use login error instead of Exception it handles all login errors
    
    print("Login successful")

except LoginError as e:
    print(f"LoginError: {e}")

    
# 10. Bank Minimum Balance Exception

# **Question:**
# Create custom exception:

# ```
# MinimumBalanceError
# ```

# If withdrawal makes balance < 1000 → raise exception.

class MinimumBalanace(Exception):
    pass

try:
    balance = 10000
    withdrawl_amount = int(input("Enter your amount: "))
    if balance - withdrawl_amount < 1000:
        raise MinimumBalanace("sorry withdrawl is not support because minimum balance error")
    else:
        balance-=withdrawl_amount
        print(balance)
except MinimumBalanace as e:
    print(e)
except ValueError:
    print("please enter valid keywords")


# 11. Negative Number Not Allowed

# **Question:**
# Create custom exception:

# ```
# NegativeNumberError
# ```

# Raise exception if user enters negative number.
class Negativenumbererror(Exception):
    pass
try:
    numbers = int(input("Enter the number properly: "))
    if numbers < 0:
        raise Negativenumbererror("negative number not allowed")
    else:
        print("sucess")
except Negativenumbererror as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    

# 12. Student Marks Validation

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
try:
    marks = int(input("Enter your marks: "))
    if marks>=85 and marks <=100:
        print("Valid marks")
    elif marks > 100:
        print("marks must be 0 to 100")
    else:
        raise InvalidMarksError("not valid marks")
except InvalidMarksError as e:
    print(e)
except ValueError:
    print("Invalid inputs")
    

# 13. Nested Try-Except Block

# **Question:**
# Create program:

# * Take number input
# * Divide 100 by number
# * Inside that, convert another input to integer
# * Use nested try-except

# Handle:

# * ZeroDivisionError
# * ValueError

try:
    num = int(input("Enter the number: "))
    try:
        result = num / 100
        print("result: ",result)
        sec_num = int(input("Enter second number: "))        
        final_result = result / sec_num
        print(final_result)
    except ZeroDivisionError:
        print("num is not divided by zero")
except ValueError:
    print("provide valid numbers")
        

# 14. Custom Exception with finally Block

# **Question:**
# Create custom exception:

# ```
# PasswordLengthError
# ```

# If password length < 6 → raise exception
# Ensure finally block always prints:
# "Validation process completed."

try:
    password = input("enter the password: ")
    if len(password) < 6:
        raise Exception("password length is must greater than 8")
    if len(password) > 8:
        print("Login success")
except Exception as e:
    print(e)
finally:
   print("Validation process completed") 


# 15. Mini Project: Online Payment System

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

# ---

class OnlinePaymentSystem(Exception):
    pass
class Invalidcarderror(Exception):
    pass
class Insuffient(Exception):
    pass
balance = 10000
try:
    card_number = input("Enter your card number: ")
    if card_number == 16:
        raise Invalidcarderror("invalid card number")
    amount = int(input("Enter your amount: "))
    if amount > balance:
        raise Insuffient("Insuffiecient balance")
except Invalidcarderror as e:
    print(e)
except Insuffient as e:
    print(e)
except ValueError:
    print("enter valid numbers")
else:
    balance-=amount
    print(balance)  
finally:
    print("Transcation Completed")