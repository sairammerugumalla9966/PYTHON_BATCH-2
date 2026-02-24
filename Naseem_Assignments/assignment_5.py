'''
Assignment 4 :
====================================

1.Write a program to check whether a given number is positive, negative, or zero.

2.Write a program to check whether a given number is even or odd using an if-else statement.

3.Write a program to find the largest of two numbers entered by the user.

4.Write a program to find the largest of three numbers using if-elif-else.

5.Write a program to check whether a given year is a leap year or not.

6.Write a program to check whether a person is eligible to vote based on age input.

7.Write a program to display student grade based on the following conditions:

    Marks ≥ 90 → Grade A

    Marks ≥ 75 → Grade B

    Marks ≥ 60 → Grade C

    Marks < 60 → Grade D

8.Write a program to check whether a given character is: a vowel or a consonant

9.Write a program to create a simple calculator using if- elif -else
(addition, subtraction, multiplication, division).

10.Write a program to check whether a given number is a three-digit number or not using conditional statements.

=============================================================================================
'''

# 1.Write a program to check whether a given number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num == 0:
    print(num, "It is Zero")

elif num > 0:
    print(num, "It is a Positive Number")

else:
    print(num, "It is a Negative Number")


# 2.Write a program to check whether a given number is even or odd using an if-else statement.

num = int(input("Enter a number: "))

if num%2 == 0:
    print(num, "It is a Positive Number")
else:
    print(num, "It is a Negative Number")


# 3.Write a program to find the largest of two numbers entered by the user.

num1 = int(input("Enter 1st value:"))
num2 = int(input("Enter 2nd Value:"))

if num1 > num2:
    print("largest value:", num1)
else :
    print(" largest value:", num2)


# 4.Write a program to find the largest of three numbers using if-elif-else.

num1 = int(input("Enter 1st value:"))
num2 = int(input("Enter 2nd Value:"))
num3 = int(input("Enter 3rd Value:"))

if num1 > num2 and num1 > num3:
    print("largest value:", num1)

elif num2 > num1 and num1 > num3:
    print("Largest number", num2)

else:
    print("Largest Number: ",num3)

# 5.Write a program to check whether a given year is a leap year or not.

year = int(input("Enter a year to check whether it is a leap year or not:"))

if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
    print(year, "It is a Leap Year")
else:
    print(year, "It is not a leap year")


# 6.Write a program to check whether a person is eligible to vote based on age input.

person_age = int(input("Enter age of a Candidarte:"))

if person_age >= 18:
    print("He is Eligible for Voting", person_age)

else:
    print("Candidate is not Eligible for Voting", person_age)


# 7.Write a program to display student grade based on the following conditions:

#    Marks ≥ 90 → Grade A

#    Marks ≥ 75 → Grade B

#    Marks ≥ 60 → Grade C

#    Marks < 60 → Grade D

student_marks = int(input("Enter Student Marks:"))

if student_marks >= 90 :
    print(student_marks, "Grade A")
    
elif student_marks >= 75 and student_marks <=90:
    print(student_marks, "Grade B")

elif student_marks >= 60 and student_marks <=90 and student_marks <= 75:
    print(student_marks, "Grade C")

else:
    print(student_marks, "Grade D")


# 8.Write a program to check whether a given character is: a vowel or a consonant

char = int(input("Enrter a Character:"))

vowel = ["A","E", "I", "O", "U" , "a", "e", "i"," o", "u"]

if char in vowel:
    print(char, "It is a Vowel")

else:
    print(char, "It is a Consonant")


# 9.Write a program to create a simple calculator using if- elif -else (addition, subtraction, multiplication, division).

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero not allowed")
else:
    print("Invalid choice")

# 10.Write a program to check whether a given number is a three-digit number or not using conditional statements.

number = input("Enter a Number :")

if len(number) == 3:
    print(number, "It is a 3 digit number")
else:
    print(number, "It is not a 3 digit number")