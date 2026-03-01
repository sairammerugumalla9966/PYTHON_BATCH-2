# operators -> operators is a symbols that tells to perform operations on between variables and values
# There are different type of operators they are:

#==========================Arithmetic Operators=============================

#1) Addition

a = 10
b = 3
print(a + b)   

#o/p:  13


#2) Subtraction

a = 10
b = 3
print(a - b)   

#o/p:  7

#3) Multiplication

a = 10
b = 3
print(a * b)

#o/p : 30

#4) Division

a = 10
b = 5
print(a / b) 

#o/p: 2.0   #by default it takes float division only

#5) Floor division

a = 10
b = 3
print(a // b) #it takes coefficient values

#o/p: 3

#6) Modulus

a = 10
b = 3
print(a % b)

#/p: 1 -> it takes remainder values

7#) power

a = 10
b = 3
print(a ** b)

#o/p : 1000 

#=================Comparison or Relational Operators==================

#it is used to compare two values and it gives the output true or false

#1) Equal to

x = 10
y = 20
print(x == y)   

#o/p : False

#2) Not equal

x = 10
y = 20
print(x != y) 

#o/p: True

#3) Greater than

x = 10
y = 20
print(x > y)   # False

#4) Less than

x = 10
y = 20
print(x < y)

#o/p: True

#5) Greater or equal

x = 10
y = 20
print(x >= y)

#o/p: False

# 6) Less or equal

x = 10
y = 20
print(x <= y)

#o/p: True

#=====================Assignment Operators=============================

#1) Assign -> assigning the values (=)

a = 10
print(a) 

#o/p : 10

#2) Add & assign (+=)

a = 10
a+=5
print(a)

# o/p: 15

# 3) Subtract & assign (-=)

a = 10
a-=5
print(a)

# o/p : 10

#4) Multiply & assign (*=)

a = 10
a*=2

print(a)

#

#5) Divide & assign (/=)

a = 10
a/=2
print(a)

# o/p: 5

#=====================Logical Operators========================

#it is used to combine the both conditions

#1) and -> must be both the conditions True 

a = 10
b = 5
print(a > b and b > 2)  

# o/p: True

#2) or -> atleast one condition will be true

a = 10
b = 5
# print(a>b or b=2)

# o/p: True

#3) not ->it reverse the results 

a = 10
b = 5
#print(a>b not b>2)

# o/p: False

#=====================Membership Operators===================================

#it is used to check the presence on the sequence

#1) in -> it gives True if the value is found in the sequence

list1 = [10, 20, 30]
print(20 in list1) 

#o/p: True

#2) not in -> it gives false if value is not found in the sequence

list1 = [10, 20, 30]
print(50 not in list1) 

#o/p: True

#====================Identity Operators===================

#it is used to check the same memory location like pointing the same objects or not if not it gives false

#1) is -> it returns true if both variable are pointing the same object

a = [10, 20]
c = [10, 20]

print(a is c)   

#o/p: False  -> because pointing the different objects even those values are same but it creates different memory location example id(1),id(2)

a = 10
b = 10
print(a is b)

#o/p: True -> because pointing the same memory location

#2) is not -> checks whether two variables are pointing the same objects if not it returns true

a = [10, 20]
c = [10, 20]

print(a is not c)

# o/p: True

# ===========
# Q(8)
#Write a program to check whether a number is even or odd using operators.

num = int(input("enter a number: "))

if num % 2 == 0:
    print("even")
else:
    print("odd")

# o/p :
# enter a number: 3
# odd

# Q(9)
#write a program to calculate the area of a rectangle using arithmetic operators and user input.

length = int(input("enter a length: "))
width = int(input("enter the width: "))

rec = length * width
print(rec)

# o/p: 
# enter a length: 2
# enter a width: 3
# 6

# Q(10)
# #Explain operator precedence in Python and write a program showing how precedence affects the result.

# Operator precedence decides which operator is evaluated first when multiple operators are used in the same       
# expression.

result = 10 + 5 * 2 #multiply first after addition because it follow the precedence rules
print(result)

# o/p:
# 20

# ==================
# 1) 1.Create a list of 5 student names and:

#     a)Add one more name

#     b)Remove one name

#     c)Display the final list

students = ['sumanth','mahesh','vinay'] 

students.append('Naseem')

students.remove('vinay')

print("final list: " ,students)

# output: 
# final list: ['sumanth','mahesh','Naseem']

# =======
# 2.Write a program to find the largest and smallest elements in a list without using built-in functions.

# =======

# 3.Create a tuple with mixed data types and:

#     a)Access elements using indexing

#     b)Explain why tuples are immutable

#     c)Convert a tuple into a list, modify an element, and convert it back into a tuple.

a = (2 , 3.5 , "sumanth" , True , None)
print(a)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

# OUTPUT:
# (2, 3.5, 'sumanth', True, None)
# 2
# 3.5
# python
# True
# None

# (b)Tuples are immutable because tuple cannot be changed once created
# ex:

a[1] = "Leo"
print(a)

# OUTPUT:
# TypeError: 'tuple' object does not support item assignment


#(c)

b = list(a)
b[2] = "Leo"
a = tuple(b)
print(a)

# OUTPUT:
# (5, 3.5, 'Leo', True, None)

#====

#4.Write a program to remove duplicate values from a list using a set.

a = [10 , 10 , 10 , 20 , 40 , 20 , 30 , 50 , 40]
print(a)

my_set = set(a)
print(my_set)

# OUTPUT:
# [10, 10, 10, 20, 40, 20, 30, 50, 40]
# {30,20,10,40,50}

#=====

# 5.Create a dictionary with employee details (id, name, salary).
# Perform:

#     a)Add a new key

#     b)Update salary
    
#     c)Delete a key

employee = {
              "id" : 3,
              "name" : "Sumanth",
              "salary" : 40000
           }

print(employee)  

employee["role"] = "python developer"   #adding a new key-value
print( employee)

employee["salary"] = 50000    #updating the value
print(employee)

del employee["id"]
print(employee)

# OUTPUT:

# {'id': 03, 'name': 'Sumanth', 'salary': 40000}
# {'id': 03, 'name': 'Sumanth', 'salary': 50000, 'role': 'python developer'}
# {'id': 03, 'name': 'Sumanth', 'salary': 60000, 'role': 'python developer'}
# {'name': 'Sumanth', 'salary': 60000, 'role': 'python developer'}

#====

#6.Write a program to iterate through a dictionary and print: Keys, Values ,Key-value pairs.

Student_Details = {"Name":"sumanth", "Age": 22, "Class": "10th", "Roll_No": 3, "Country": "India",}


print(Student_Details.keys())

print(Student_Details.values())

print(Student_Details.items())

#=========

#7.Declare two sets, perform and display: Union, Intersection, Difference.

a = {10, 20, 30, 40}
print(a)

b = {30, 40, 50, 60}
print(b)

print(a | b)
print(a & b)
print(a - b)

# OUTPUT:

# {10, 20, 30, 40}
# {30, 40, 50, 60}
# {10, 20, 30, 40, 50, 60}
# {40, 30}
# {10, 20}

#====

# 8.Write a program to count the frequency of each element in a list using a dictionary.

ls = [1,2,3,2,1,3,4,4,5]
freq={}
count = 0

for i in list:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

# output:
# {1: 2, 2: 2, 3: 2, 4: 2, 5: 1}
#=========

# 9 & 10.Explain the difference between list, tuple, set, and dictionary with one real-time ex.

# ------------|------------|-------------------|------------------------|--------------------
# Feature	    |    List	 |         Tuple     |	             Set      |	      Dictionary
# ------------|------------|-------------------|------------------------|--------------------
# Order	    |    Yes	 |          Yes	     |                No      |	        Yes
# Mutable	    |    Yes	 |          No	     |                Yes     |	        Yes
# Duplicates  |	 Yes	 |          Yes	     |                No      |	        Keys 
# Indexing    |	 Yes	 |          Yes	     |                No      |	        By key
# Syntax	    |     []	 |          ()	     |                {}      |	        {key: value}
# ---------------------------------------------------------------------------------------------

# # real-time examples of list: 
# Shopping cart items (items can be added/removed, order matters)
# bash : cart = ["Mobile", "Charger", "Mobile"]

# real-time examples of tuple:
# Days of the week (fixed, should not change)
# bash: days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# real-time examples of set:
# Unique email IDs (duplicates not allowed)
# bash: emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}

# real-time examples of dictionary:
# Employee details
# employee = {"id": 03, "name": "Sumanth", "salary": 50000}
