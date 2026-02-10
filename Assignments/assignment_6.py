'''
Assignment 5

conditional statements 
Loops

1.Write a program to print numbers from 1 to 10 using a for loop.

2.Write a program to print even numbers between 1 and 50 using a loop.

3.Write a program to calculate the sum of first N natural numbers using a while loop.

4.Write a program to display the multiplication table of a given number using a for loop.

5.Write a program to count the number of digits in a given number using a loop.

6.Write a program to reverse a number using a while loop.

7.Write a program to print the following pattern using nested loops:

*
* *
* * *
* * * *
* * * * *


8.Write a program to check whether a given number is a prime number using loops.

9.Write a program to demonstrate the use of break and continue statements with a loop.

10.Write a program to find the factorial of a given number using a loop.

'''

# 1.Write a program to print numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)

# 2.Write a program to print even numbers between 1 and 50 using a loop.

for i in range(1, 50):
    if i % 2 == 0:
        print("Even numbers from 1 to 50: ", i)

# 3.Write a program to calculate the sum of first N natural numbers using a while loop.

num = int(input("Enter a number:"))
sum = 0
i = 1
while i <= num:
    sum =sum + i
    i = i + 1

print("Number", num, "Sum of numbers: ", sum)


# 4.Write a program to display the multiplication table of a given number using a for loop.

num = int(input("Enter a number: "))

for i in range(1,11):
    mul = num * i
    print("Number = ", num, "*", i , "=", mul)

# 5.Write a program to count the number of digits in a given number using a loop.


num = list(input("Enter amount: "))
count = 0
for i in num:
    count+=1   
print(count)

# 6.Write a program to reverse a number using a while loop.

num = int(input("Enter a number to reverse: ")) # doubt

# 7.Write a program to print the following pattern using nested loops:

# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6): 
    for j in range(i): 
        print("*",end="")
    print()
print()


