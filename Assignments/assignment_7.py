'''

Assignment 6
============================================

1.Write a program to print numbers from 1 to N using a loop.
(N is given by the user)

2.Write a program to find the sum of all even numbers between 1 and N using a loop.

3.Write a program to reverse a given number using a loop.
Example: Input → 1234, Output → 4321

4.Write a program to count the number of digits in a given number using a loop.

5.Write a program to generate the multiplication table of a given number up to 10.
expected output : 
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
.
.
.
5 * 10 = 50

6.Write a program to print a square pattern of stars of size N:

****
****       
****
****

and 

* * * *
* * * *       
* * * *
* * * *

7.Write a python program to print a complete diamond shape using stars (*) with nested loops.

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

8.Write a python program to display this table using nested loops.


1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15
16 17 18 19 20

'''

# 1.Write a program to print numbers from 1 to N using a loop.
# (N is given by the user)

N = int(input("enter a number:"))

for i in range(1 , N+1):
    print(i)

# 2.Write a program to find the sum of all even numbers between 1 and N using a loop.

n = int(input("Enter the value of N: "))
sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i

print("Sum of even numbers:", sum)



# 3.Write a program to reverse a given number using a loop.
# Example: Input → 1234, Output → 4321

n = input("Enter a number: ")
rev = ""

for i in n:
    rev = i + rev

print("Reversed number:", rev)

# 4.Write a program to count the number of digits in a given number using a loop.

num = list(input("Enter number : "))
count = 0
for i in num:
    count+=1   
print("No. of digits: ",count)

# 5.Write a program to generate the multiplication table of a given number up to 10.

num = int(input("Enter a number: "))

for i in range(1,11):
    mul = num * i
    print("Number = ", num, "*", i , "=", mul)

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

for i in range(1 , 5):
    for j in range(1 , 5):
        print("*",end="")
    print()


for i in range(1 , 5):
    for j in range(1 , 5):
        print("*",end=" ")
    print()

# 7.Write a python program to print a complete diamond shape using stars (*) with nested loops.

#    *
#   ***
#  *****
# *******
#*********
# *******
#  *****
#   ***
#    *

# n = 5  

# for i in range(1, n + 1):
#     for space in range(n - i):
#         print(" ", end="")
#     for star in range(2 * i - 1):
#         print("*", end="")
#     print()

# for i in range(n - 1, 0, -1):
#     for space in range(n - i):
#         print(" ", end="")
#     for star in range(2 * i - 1):
#         print("*", end="")
#     print()
