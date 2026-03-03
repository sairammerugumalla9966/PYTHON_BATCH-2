========================================================================
                assignment-3
========================================================================   


# 1.Write a program to demonstrate all arithmetic operators using two user-defined numbers. 

p = int(input("enter value for p"))
print(p)

q = int(input("enter value for "))
print(q)

addition = p + q
print(addition)  

subtraction = p - q
print(subtraction)  

multiplication = p * q
print(multiplication)  

division = p / q
print(division)  

modules = p % q
print(modules)  


floor_division = p // q
print(floor_division) 

a = 6
print(a ** 2) 

a += 3
print(a)  

a -= 4
print(a) 

a *= 9
print(a) 

a /= 5
print(a) 

# OUTPUT:
# ========
# enter value for p36
# 36
# enter value for 6
# 6
# 42
# 30
# 216
# 6.0
# 0
# 6
# 36
# 9
# 5
# 45
# 9.0

================================================================================

# 2.Write a program to compare two numbers using relational operators and display the result.

m = int(input("enter value for m"))
print(m)

n = int(input("enter value for n"))
print(n)

print(m==n)
print(m!=n)
print(m>n)
print(m>=n)
print(m<n)
print(m<=n)

# OUTPUT:
# ========
# enter value for m25
# 25
# enter value for n5
# 5
# False
# True
# True
# True
# False
# False

=====================================================================

# 3.Explain logical operators (and, or, not) with a truth table and a sample program.

and
====
-->If both conditions are True then it returns True

P   Q   P and Q
0   0      0
0   1      0
1   0      0
1   1      1

ex:
marks=75

if marks >= 35 and marks <= 100:
    print("pass")
else:
    print("fail")

# OUTPUT:
# =======
# pass

  

  or
  ===
  -->If any one condition is True then it returns True


P    Q   P or Q
0    0      0
0    1      1
1    0      1
1    1      1

ex:

marks1 = 30
marks2 = 75
if marks1>=35 or marks2>=75 :
    print("passed atleast one subject")
else:
    print("failed")

# OUTPUT:
# =========
# passed atleast one subject

not
===
-->Reverses the result of the condition
Truth table
============
  P    not P
0      1
1      0

Ex:

is_raining = False
print(not is_raining)

# OUTPUT:
# ========
# True

=========================================================================

4.Write a program to check whether a number lies between 10 and 50 using logical operators.

number = 25

if number>10 and number<50 :
    print("Number lies between 10 and 50")

else:
    print("Number does not lie between 10 and 50")

# OUTPUT:
# ========
# Number lies between 10 and 50

==========================================================================

# 5.Demonstrate the use of assignment operators (=, +=, -=, *=, /=) with examples.

'=' is used to assign a value to the variable 
ex: a = 5

'+=' is used to add a value to the variable and assigns the result.
ex:

a = 5
a+=2
print(a)

# OUTPUT:
# ==========
# 7

# '-=' is used to subtract a value to the variable and assigns the result
# ex:

a = 5
a-=3
print(a)

# OUTPUT:
# =======
# 2

# '*=' is used to multiply a value to the variable and assigns the result
# ex:

a = 3
a*=2
print(a)

# OUTPUT:
# ========
# 6

# '/=' is used to divide a value to the variable and assigns the result
# ex:

a = 25
a/=5
print(a)

# OUTPUT:
# =========
# 5.0

# =============================================================================

# 6.Write a program to check whether a given value exists in a list using membership operators.

vegetables = ["tomato" , "brinjal" , "potato" , "ladiesfinger" ]
print("potato" in vegetables)

# OUTPUT:
# ========
# True

# =================================================================================

# 7.What is the difference between == and is operators?
# Write a program to prove it.

# '==' is used to compare the values of 2 variables .If 2 values  are same it returns True
# ex:

a = [10 , 20 , 30]
b = [10 , 20 , 30]
print(a==b)
print(a is b)

# OUTPUT:
# =========
# True
# False

# 'is' is a identity operator.It is used to compare the memory location of 2 variables.If the memory location of 2 variables are same then it returns True
# ex:
x = [10 , 20 , 30]
y = x
print(x is y)
print(x == y)

# OUTPUT:
# =======
# True
# True

# ==================================================================================

# 8.Write a program to check whether a number is even or odd using operators.

a = 5

if a%2==0 :
    print("a is a even number")
else:
    print("a is odd number")

# OUTPUT:
# ========
# a is odd number

# ============================================================================================

# 9.Write a program to calculate the area of a rectangle using arithmetic operators and user input.

length = int(input("enter a value for length :"))
print(length)

breadth = int(input("enter a value for breadth :"))
print(breadth)

area = length * breadth
print(area)

# OUTPUT:
# ========
# enter a value for length :25
# 25
# enter a value for breadth :7
# 7
# 175

# ===================================================================================================

# 10.Explain operator precedence in Python and write a program showing how precedence affects the result.

# 1.Create a list of 5 student names and:

#     a)Add one more name

#     b)Remove one name

#     c)Display the final list


students = ["manu" , "jyoshu" , "ravi" , "sravani" , "hema"]
print(students)

students.append("pravathi")
students.remove("sravani")

print(students)

# OUTPUT:
# ========
# ['manu', 'jyoshu', 'ravi', 'sravani', 'hema']
# ['manu', 'jyoshu', 'ravi', 'hema', 'pravathi']

# =================================================================

# 2.Write a program to find the largest and smallest elements in a list without using built-in functions.

# ==================================================================

# 3.Create a tuple with mixed data types and:

#     a)Access elements using indexing

#     b)Explain why tuples are immutable

#     c)Convert a tuple into a list, modify an element, and convert it back into a tuple.

a = (5 , 3.5 , "python" , True , None)
print(a)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

# OUTPUT:
# ==========
# (5, 3.5, 'python', True, None)
# 5
# 3.5
# python
# True
# None

# (b)Tuples are immutable because tuple cannot be changed once created
# ex:

a[1] = "java"
print(a)

# OUTPUT:
# ========
# TypeError: 'tuple' object does not support item assignment


# (c)

b = list(a)
b[2] = "java"
a = tuple(b)
print(a)

# OUTPUT:
# ==========
# (5, 3.5, 'java', True, None)

# ======================================================

# 4.Write a program to remove duplicate values from a list using a set.

a = [10 , 20 , 10 , 30 , 40 , 20 , 30 , 50 , 40]
print(a)

my_set = set(a)
print(my_set)

# OUTPUT:
# ==========
# [10, 20, 10, 30, 40, 20, 30, 50, 40]
# {40, 10, 50, 20, 30}

# ===============================================================

# 5.Create a dictionary with employee details (id, name, salary).
# Perform:

#     a)Add a new key

#     b)Update salary
    
#     c)Delete a key

employee = {
              "id" : 567,
              "name" : "manasa",
              "salary" : 50000
           }

print(employee)  

employee["role"] = "developer"
print( employee)

employee["salary"] = 60000
print(employee)

del employee["name"]
print(employee)

# OUTPUT:
# =========
# {'id': 567, 'name': 'manasa', 'salary': 50000}
# {'id': 567, 'name': 'manasa', 'salary': 50000, 'role': 'developer'}
# {'id': 567, 'name': 'manasa', 'salary': 60000, 'role': 'developer'}
# {'id': 567, 'salary': 60000, 'role': 'developer'}

# =========================================================================

# 6.Write a program to iterate through a dictionary and print: Keys, Values ,Key-value pairs.

employee = {
             "id" : 567,
             "name" : "manasa",
             "role" : "developer",
             "salary" : 50000
}

print(employee)

print(employee.keys())
print(employee.values())
print(employee.items())

# OUTPUT:
# ==========
# {'id': 567, 'name': 'manasa', 'role': 'developer', 'salary': 50000}
# dict_keys(['id', 'name', 'role', 'salary'])
# dict_values([567, 'manasa', 'developer', 50000])
# dict_items([('id', 567), ('name', 'manasa'), ('role', 'developer'), ('salary', 50000)])

# =============================================================================

# 7.Declare two sets, perform and display: Union, Intersection, Difference.

a = { 10 , 20 , 12 , 10 , 12 , 30 , 40 , 5 , 6}
print(a)

b = {1 , 2 , 3 ,1 , 12 , 10 , 5 , 6 , 1 , 3}
print(b)

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# OUTPUT:
# ========
# {20, 5, 6, 40, 10, 12, 30}
# {1, 2, 3, 5, 6, 10, 12}
# {1, 2, 3, 5, 6, 40, 10, 12, 20, 30}
# {10, 12, 5, 6}
# {40, 20, 30}

# =========================================================================================

# 8.Write a program to count the frequency of each element in a list using a dictionary.

9.Explain the difference between list, tuple, set, and dictionary with one real-time example each

10.Explain the difference between list, tuple, set, and dictionary with one real-time example each.

====================================================================================================================================
|                  LIST                      |                  TUPLE                  |              DICTIONARY                   |          
====================================================================================================================================
| 1.List is denoted with '[]'                | 1.Tuple is denoted with '()'            | 1.Dictionary is denoted with '{}'         |                             
| 2.List is a ordered collection             | 2.Tuple is a ordered collection         | 2.Data is stored in the key-value pair    |
| 3.List can be mutable                      | 3.Tuple can be immutable                | 3.Dictionary can be mutable               |
| 4.In list,values can be accessed by index  | 4.In tuple,values can be accessed by    | 4.In dictionary,values are accessed by    |
|                                            |     index                               |    using key() and values() method.                    |
====================================================================================================================================
