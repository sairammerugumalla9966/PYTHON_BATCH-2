// 1.Write a program to check whether a given number is positive, negative, or zero.


a = int(input("enter a value"))

if a > 0 :
    print(a  , "is a positive Number")
  
elif a < 0:
    print(a , "is a Negative Number")
  

else :
   print(a , "is a Zero")

   enter a value5
5 is a positive Number

enter a value0
0 is a Zero

enter a value-4
-4 is a Negative Number
   

// 2.Write a program to check whether a given number is even or odd using an if-else statement.

a = int(input("enter a value"))

if a%2==0 :
   print(a , "is a even number")
elif  a%2!=0:
   print(a , "is a odd number")

 enter a value4
4 is a even number

enter a value3
3 is a odd number


// 3.Write a program to find the largest of two numbers entered by the user.

a = int(input("first Number :"))
b = int(input("second  number :"))

if a>b:
   print(a , "is largest number")

elif b>a:
   print(b,"is largest number")

enter a number :23
enter a number :34
34 is largest number

first Number :34
second  number :23
34 is largest number

// 4.Write a program to find the largest of three numbers using if-elif-else.

a = int(input("first Number :"))
b = int(input("second  number :"))
c = int(input("Third Number:"))

if a>b and a>c:
   print(a ,"is Largest Number")
elif b>c and b>a:
   print(b,"is Largest Number")

else:
   print(c,"is Largest Number")

   first Number :12
second  number :34
Third Number:9
34 is Largest Number




// 5.Write a program to check whether a given year is a leap year or not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

Enter a year: 2026
2026 is not a Leap Year




// 6.Write a program to check whether a person is eligible to vote based on age input.

age = int(input("enter your age:"))

if age>=18:
   print("Eligible for voting")
else:
   print("Not Eligible for voting")

   enter your age:23
Eligible for voting

enter your age:17
Not Eligible for voting

// 7.Write a program to display student grade based on the following conditions:

//     Marks ≥ 90 → Grade A

//     Marks ≥ 75 → Grade B

//     Marks ≥ 60 → Grade C

//     Marks < 60 → Grade D

marks = int(input("enter your marks:"))

if marks >= 90 :
   print("Grade A")

elif marks >= 75:
   print("Grade B")

elif marks >=60:
   print("Grade C")

elif marks <60:
   print("Grade D")

# enter your marks:85
# Grade B

enter your marks:34
Grade D


// 8.Write a program to check whether a given character is: a vowel or a consonant

character = input("enter a character :")

if character in ('a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U'):
   print(character ,"is a Vowel")
else:
   print(character , "is a consonant")

enter a character :e
e is a Vowel

enter a character :r
r is a consonant


// 9.Write a program to create a simple calculator using if- elif -else
// (addition, subtraction, multiplication, division).

operation = input("enter a operator:")


a = int(input("enter first number"))
b = int(input("enter second number"))

result = 0

if operation == '+':
   print("result =" , a+b)
elif operation == '-':
   print("result =" , a-b)
elif operation == '*':
   print("result = " , a*b)
elif operation == '/':
   print("result = " , a/b)

enter a operator:+
enter first number25
enter second number56
result = 81

enter a operator:-
enter first number85
enter second number50
result = 35

enter a operator:*
enter first number25
enter second number5
result =  125

enter a operator:/
enter first number25
enter second number5
result 5.0

// 10.Write a program to check whether a given number is a three-digit number or not using conditional statements.

number = int(input("enter a number:"))

if number >=100 and number <=999:
   print(number,"is a three digit number")
else:
   print(number,"is a not a three digit number")

enter a number:234
234 is a three digit number

enter a number:2345
2345 is a not a three digit number