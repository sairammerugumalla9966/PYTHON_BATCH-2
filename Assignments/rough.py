
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

