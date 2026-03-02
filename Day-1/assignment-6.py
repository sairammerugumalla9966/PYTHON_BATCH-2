# Assignment 6
# ============================================

# 1.Write a program to print numbers from 1 to N using a loop.
# (N is given by the user)

# num = int(input("enter a number:"))

# for i in range(1 , num+1):
#     print(i)

# enter a number:10
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 2.Write a program to find the sum of all even numbers between 1 and N using a loop.

# num = int(input("enter a number:"))

# for i in range(1 , num+1):
#     if(i%2==0):
#         print(i)

# enter a number:20
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20


# 3.Write a program to reverse a given number using a loop.
# Example: Input → 1234, Output → 4321

# num = int(input("enter a number:"))
# reverse = 0

# while num != 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num// 10

# print("Reversed number:", reverse)

# enter a number:1234
# Reversed number: 4321

# 4.Write a program to count the number of digits in a given number using a loop.

# num = int(input("enter a number:"))

# count = 0
# while num != 0:
#     num = num // 10
#     count += 1

# print("Number of digits:", count)

# enter a number:34567
# Number of digits: 5

# 5.Write a program to generate the multiplication table of a given number up to 10.
# expected output : 
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# .
# .
# .
# 5 * 10 = 50

# num = int(input("enter a number:"))

# for i in range(1 , 11):
#     print(num , "X" , i , "=" , num * i)

# enter a number:5
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# 5 X 10 = 50


# 6.Write a program to print a square pattern of stars of size N:

# ****
# ****       
# ****
# ****

# and 

# * * * *
# * * * *       
# * * * *
# * * * *

# for i in range(1 , 5):
#     for j in range(1 , 5):
#         print("*",end="")
#     print()

# ****
# ****
# ****
# ****

# for i in range(1 , 5):
#     for j in range(1 , 5):
#         print("* ",end="")
#     print()

# * * * * 
# * * * * 
# * * * *
# * * * *


# 7.Write a python program to print a complete diamond shape using stars (*) with nested loops.

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# 8.Write a python program to display this table using nested loops.


# 1 2 3 4 5 
# 6 7 8 9 10 
# 11 12 13 14 15
# 16 17 18 19 20

# num = 1
# for i in range(1 , 5):
#     for j in range(1 , 6):
#         print(num , end="")
#         num+=1
#     print()

# 12345
# 678910
# 1112131415
# 1617181920




