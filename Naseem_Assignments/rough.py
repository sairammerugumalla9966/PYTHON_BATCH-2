
# number = int(input("Enter a numner"))

# if number % 2 == 0:
#     print(number, "It is an even Number")

# else: print(number, "It is an odd number")

# length = int(input("Enter length of a Rectangle: "))
# breadth = int(input("Enter Breadth of a Rectangle: "))

# Area = length * breadth
# print("Area of Rectangle is: ", Area)

# student_names = ["zeena", "mairah", "aleena", "amio","saya"]

# student_names.append("libe")
# print(student_names)

# student_names.remove("libe")
# print(student_names)

# print("Final list: ", student_names)


# lst = [10, 20, 30, 40, 50, 60, 70]

# print(min(lst))
# print(max(lst))


# 3.Create a tuple with mixed data types and:

#    a)Access elements using indexing

#    b)Explain why tuples are immutable

#    c)Convert a tuple into a list, modify an element, and convert it back into a tuple.

# tup = ("Naseem", 546, 'Hyderabad', 79.9)

# # a
# print(tup[0])
# print(tup[3])

# # b
# # Tuples are immutable because tuples cannot be modified or changed

# # c

# lst = list(tup)
# lst[0] = "Ahammad"
# print(lst)
# tup = tuple(lst)

# print(tup)

# lst = [10,10,20,20,30]

# print("Before removing duplicates",lst)

# sets = set(lst)
# print(sets)



# 5.Create a dictionary with employee details (id, name, salary).
#    Perform:

#    a)Add a new key

#    b)Update salary
    
#    c)Delete a key'

# Employee_Details = {"Id": 1, "Name": "Zeena", "Salary": "23,000/-"}

# # a 
# Employee_Details["City"] =  "Hyderabd"
# print(Employee_Details)

# # b 
# Employee_Details.update({"Salary": "32000/-"})
# print(Employee_Details)


# # c 
# Employee_Details.pop("Salary")
# print(Employee_Details)

# a = {1, 2, 3}
# b = {3, 4, 5}


# print(a.union(b))

# print(a.intersection(b))

# print(a.difference(b))


# num1 = int(input("Enter 1st value:"))
# num2 = int(input("Enter 2nd Value:"))
# num3 = int(input("Enter 3rd Value:"))

# if num1 > num2 and num1 > num3:
#     print("largest value:", num1)

# elif num2 > num1 and num1 > num3:
#     print("Largest number", num2)

# else:
#     print("Largest Number: ",num3)


# year = int(input("Enter a year to check whether it is a leap year or not:"))

# if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
#     print(year, "It is a Leap Year")
# else:
#     print(year, "It is not a leap year")
    

# person_age = int(input("Enter age of a Candidarte:"))

# if person_age >= 18:
#     print("He is Eligible for Voting", person_age)

# else:
#     print("Candidate is not Eligible for Voting", person_age)


# student_marks = int(input("Enter Student Marks:"))

# if student_marks >= 90 :
#     print(student_marks, "Grade A")
    
# elif student_marks >= 75 and student_marks <=90:
#     print(student_marks, "Grade B")

# elif student_marks >= 60 and student_marks <=90 and student_marks <= 75:
#     print(student_marks, "Grade C")

# else:
#     print(student_marks, "Grade D")

# char = input("Enrter a Character:")

# vowel = ["A","E", "I", "O", "U" , "a", "e", "i"," o", "u"]

# if char in vowel:
#     print(char, "It is a Vowel")

# else:
#     print(char, "It is a Consonant")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Choose operation:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# operation = int(input("Enter your choice (1-4): "))

# if operation == 1:
#     print("Result:", a + b)
# elif operation == 2:
#     print("Result:", a - b)
# elif operation == 3:
#     print("Result:", a * b)
# elif operation == 4:
#     if b != 0:
#         print("Result:", a / b)
#     else:
#         print("Error: Division by zero not allowed")
# else:
#     print("Invalid choice")



# number = input("Enter a Number :")

# if len(number) == 3:
#     print(number, "It is a 3 digit number")
# else:
#     print(number, "It is not a 3 digit number")


# num = int(input("Enter a number: "))
# count = 0

# for i in range(1, num+1):
#     if num % i == 0:
#         count += 1
# if count == 2:
#     print("It is a prime number", num)
# else: 
#     print("It is not a prime number")

# num = int(input("Enter a number:"))
# fac = 0
# i = 1
# while i <= num:
#     fac =fac + i
#     i = i + 1

# print("Number", num, "Factorial: ", fac)


# num = int(input("Enter a number to reverse: "))
# rev  = 0 
# while num > 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
# print(rev)


# num = int(input("Enter a number:"))
# fac = 1
# i = 1
# while i <= num:
#     fac = fac * i
#     i += 1
# print(fac)

# def samplefunction():
#     a = 100
#     b = 200
#     c = 300
#     return c 
# samplefunction

# n = 5
# for i in range(1, n+1):
#     for spaces in range(n - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(n-1,0,-1):
#     for spaces in range(n - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()





# 8.Write a python program to display this table using nested loops.

# 1 2 3 4 5 
# 6 7 8 9 10 
# 11 12 13 14 15
# 16 17 18 19 

# n= 4
# num = 1
# for i in range(1, n+1):
#     for j in range(1,6):
#         print(num, end=" ")
#         num += 1
#     print()        


# n = 5 
# for i in range(1, n+1):
#     for spaces in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end =" ")
#     print()

# for i in range(n-1, 0, -1):
#     for spaces in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end =" ")
#     print()



# # 1.
# def Message():
#     print("Hi, How are you ....?")

# Message()

# # 2. 
# def Sum(a,b):
#     sum = a + b
#     return("Sum of two numbers: ", sum )
# print(Sum(2,5))

# # 3. 
# def ConcatinationOfStrings(name1, name2):
#     Concat = name1 + name2
#     return("Concatination of two Names: ", Concat)
# print(ConcatinationOfStrings("Nas", "eem"))


# # 4. 
# num1 = 8
# num2 = 10 
# def Mul(num1, num2):
#     mul = num1 * num2
#     return("Multiplication of two numbers: ", mul)
# print(Mul(num1, num2))

# # 5. 
# def numbers():
#     for i in range(1,6):
#         print(i)
# numbers()

# # 6. 
# def Student_Details(name, age):
#     print("Name:", name)
#     print("Age:", age)
# Student_Details(age=21, name="Naseem")

# # 7. 
# def Factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * Factorial(n-1)
# print(Factorial(5))

# # 8. 
# x = 10

# def show():
#     y = 5
#     print(" Function:", x + y)
# show()

# # 9. 
# def Bike(name, model):
#     print("Brand: ", name, "~" ,"Model: ", model)

# Bike("Royal Enfield", "Himalayan")

# # 10.
# def info(name, age=18, city="Hyd"):
#     print(name,age,city)

# info("Naseem")
# info("Zeena", 22)
# info("Mairah", 27, "Mumbai")



# 2. User-Defined Max, Min, Sum (Without Built-ins)
# **Question:**
# Write your own functions to calculate:

# * Maximum
# * Minimum
# * Sum

# Do NOT use max(), min(), sum().

# lst = list(map(int, input("Enter elements separated by space: ").split()))
# print("List: ", lst)

# def Max(lst):
#     max = lst[0]
#     for i in lst:
#         if i > max:
#             max = i
#     return max
# print("Maximum: ", Max(lst))

# def Min(lst):
#     min = lst[0]
#     for i in lst:
#         if i < min:
#             min = i
#     return min
# print("Minimum: ", Min(lst))

# def Sum(lst):
#     sum = 0
#     for i in lst:
#         sum+= i
#     return sum
# print("Sum : ", Sum(lst))

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

# def greet(Name):
    
#     msg = "Hello" " "+ Name + "!" +" " "Welcome to Python Class"
#     return msg
# print(greet("Sairam"))


# def calculate_total(price, quantity):
#     total = price * quantity
#     return total
# print(calculate_total(100, 3))

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

# def create_account(name, role='user'):
#     msg = "Account Created For " + name + " " + "With Role " + role
#     return msg
# print(create_account("Rahul"))
# print(create_account("AdminUser", "Admin"))

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

# def square_ret(num):
#     square = num * num
#     return(square)
# print(square_ret(5))

# result = square_ret(5)
# print(result * 10)

# def add(a, b):
#     sum = a + b 
#     return sum
# print(add(2,3))

# def mul(a, b):
#     mul = a * b 
#     return mul
# print(mul(add(2,3), 4))

# num = list(map(int,input("Enter a list : ").split(",")))

# def count(num):
#     eve_count = 0 
#     odd_count = 0
#     for i in num:
#         if i % 2 == 0:
#             eve_count += 1
#         else:
#             odd_count += 1

#     return "Even Count: " + str(eve_count) + "\nOdd Count: " + str(odd_count)
        
# print(count(num))

# def Palindrome(Name):
#     if Name == Name[::-1]:
#         return True
#     else:
#         return False

# print(Palindrome("Naseem"))
# print(Palindrome("madam"))

# def Factorial(num):
#     fac = 1
#     i = 1
#     while i <= num:
#         fac = fac * i
#         i += 1
#     return i

# print(Factorial(5))


# def Factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return  num * Factorial(num - 1)

# print(Factorial(5))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Enter n: "))

# for i in range(n):
#     print(fibonacci(i), end=" ")


# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + sum_of_digits(n//10)
# print(sum_of_digits(2345))

# def reverse(name):
#     if len(name) == 0:
#         return name
#     else:
#         return reverse(name[1:]) + name[0]
# print(reverse("Python"))

# """s[0]   → "p"        (first character)
# s[1:]  → "ython"    (everything except first character)
# """



class Student:

    school_name = "ABC School"   # Class Variable

    def __init__(self, name, marks):
        self.name = name         # Instance Variable
        self.marks = marks

    
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    
    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

    
    @staticmethod
    def is_pass(marks):
        return marks >= 35
    
s1 = Student("Naseem", 80)

s1.display()   

Student.change_school("Oxford")   
print(Student.school_name)

print(Student.is_pass(80))   