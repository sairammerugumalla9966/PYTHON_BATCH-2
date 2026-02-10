'''
Docstring for Day4.variables


# Variables in Python

# What is a Variable?
# A variable is a container used to store data in memory.(general defintion )


# Python variables:

# In python : A variable is a name bound to an object in memory.
# Variable does NOT store value
# It refers to an object
# They are created automatically
# They do not require type declaration
# They can change type at runtime


# Variable Declaration

x = 10
name = "Python"
price = 99.99

age=int(input("enter your age : "))
print(age)

# where x → reference , 10 → object

# Types of Variables

#Local Variables
#Global Variables
#Instance Variables
#Class Variables              (We’ll go deep into these in OOPs)

#Variable Assignment Types

# Single Assignment

x = 10
b=555
c=-25
name="sumanth"

# Multiple Assignment

a,b,c=1,2,3

# Same Value Assignment

x = y = z = 100

# Examples of Variables

# User Login System (Used in authentication)

username = "sairam"
password = "admin123"


# ATM Withdrawal (Used in banking systems)

balance = 20000
withdraw = 5000
balance = balance - withdraw
print("total_balance : ",balance)


# Online Shopping Cart (Used in e-commerce)

item_price = 1500
quantity = 2
total = item_price * quantity
print("total_price : ",total)


# Student Result System (Used in education systems)

marks = 85
result = "Pass" if marks >= 40 else "Fail"


# Salary Calculation (Used in payroll systems)

basic_salary = 30000
hra = 5000
total_salary = basic_salary + hra
print("total_salary : ",total_salary)


'''


x = 10
name = "Python"
price = 99.99

print(x+price)



#age=int(input("enter your age : ")) # input 
#print("my age is : ",age)        #output 

#print(10+3)


a,b,c=1,2,3
print(a)
print(b)
print(c)

username1, username2 ,username3 = "sairam", "manasa","rajesh"
print(username1)
print(username2)
print(username3)

x=12
x = y = z = 100

print(x)
print(y)
print(z)