#1)Write a program to check whether a given number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num == 0:
    print("zero")
elif num < 0:
    print("negative number")
else:
    print("positive number")

# output:
# Enter a number: 10
# positive

#====

#2)Write a program to check whether a given number is even or odd using an if-else statement.

num = int(input("Enter a number: "))

if num%2==0:
    print("even")
else:
    print("odd")

# output: 
# Enter a number: 12
# even

#===

#3)Write a program to find the largest of two numbers entered by the user.

num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

if num1 > num2:
    print(num1)
else:
    print(num2)

# output: 
# Enter the number1: 10
# Enter the number2: 5
# 10

#===

#4) Write a program to find the largest of three numbers using if-elif-else.

num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))

max = num1

if num1 > num2 and num1 > num3:
    max = num1
elif num2 > num3 and  num2 > num1:
    max = num2
else:
    max = num3

print(max)

# output:
# Enter the number1: 12  
# Enter the number2: 33
# Enter the number3: 4
# 33

#===

#5)Write a program to check whether a given year is a leap year or not.

year = int(input("Enter the year: "))

if (year%4==0) or (year%100!=0) and (year%400==0):
    print("leap year")
else:
    print("not a leap year")

# output: 
# Enter the year: 2024
# leap year

#===

#6)Write a program to check whether a person is eligible to vote based on age input.

age = int(input("Enter the age: "))

if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")

# output: 
# Enter the age: 12
# not eligible to vote

#===

#7).Write a program to display student grade based on the following conditions:

    #Marks ≥ 90 → Grade A

    #Marks ≥ 75 → Grade B

    #Marks ≥ 60 → Grade C

    #Marks < 60 → Grade D

    
marks = int(input("Enter the marks: "))

if marks>=90:
    Grade = 'A' 
elif marks>=75:
    Grade = 'B' 
elif marks>=60:
    Grade = 'C'
else:
    Grade = 'D'
    
print(Grade) 

# output: 
# Enter the marks: 33
# D

#===

#8)Write a program to check whether a given character is: a vowel or a consonant

character = input("Enter a character: ")
vowel = ['A','E','I','O','U','a','e','i','o','u']

if character in vowel:
    print("it is a vowel")
else:
    print('it is a consonant')

# output: 
# Enter a character: e
# it is a vowel

#===

#9)Write a program to create a simple calculator using if- elif -else (addition, subtraction, multiplication, division).

calcular = input("Enter a operator: ")
num1 = int(input("enter the number1: "))
num2 = int(input("enter the number2: "))
result = 0

if calcular == '+':
    result = num1 + num2
elif calcular == '-':
    result = num1 - num2
elif calcular == '*':
    result = num1 * num2
elif calcular == '/':
    if num2 != 0: 
        result = num1 / num2 
else:
    print("invalid operator")

print(result)

# output: 
# Enter a operator: /
# enter the number1: 10
# enter the number2: 2
# 5.0

#

#10)Write a program to check whether a given number is a three-digit number or not using conditional statements.

num = input("Enter the number: ")
n = len(num)

if n==3:
    print("yes it is a three digit number")
else:
    print("not a three digit number")

# output: 
# Enter the number: 89
# not a three digit number