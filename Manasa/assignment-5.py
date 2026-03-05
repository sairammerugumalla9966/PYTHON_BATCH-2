# 1.Write a program to print numbers from 1 to 10 using a for loop.

 for i in range(1 , 11):
    print(i)

# OUTPUT:
# ==========
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

# ====================================================================

# 2.Write a program to print even numbers between 1 and 50 using a loop.

for i in range(1 , 51):
    if(i%2==0):
        print(i)

# OUTPUT:
# ==========
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
# 22
# 24
# 26
# 28
# 30
# 32
# 34
# 36
# 38
# 40
# 42
# 44
# 46
# 48
# 50

# ===============================================================

# 3.Write a program to calculate the sum of first N natural numbers using a while loop.

n = int(input("Enter a number: "))
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i+=1

print("Sum of first", n, "natural numbers is:", sum)

# OUTPUT:
# ==========
# Enter a number: 10
# Sum of first 10 natural numbers is: 55

# =====================================================================

# 4.Write a program to display the multiplication table of a given number using a for loop.

num = int(input("enter a number:"))

for i in range(1 , 11):
    print(num , "X" , i , "=" , num * i)

# OUTPUT:
# ==========
# enter a number:3
# 3 X 1 = 3
# 3 X 2 = 6
# 3 X 3 = 9
# 3 X 4 = 12
# 3 X 5 = 15
# 3 X 6 = 18
# 3 X 7 = 21
# 3 X 8 = 24
# 3 X 9 = 27
# 3 X 10 = 30

# =====================================================================

# 5.Write a program to count the number of digits in a given number using a loop.


num = int(input("enter a number:"))

count = 0


while num != 0:
    num = num // 10
    count += 1

print("Number of digits:", count)

# OUTPUT:
# ==========
# enter a number:1234
# Number of digits: 4

# ===========================================================

# 6.Write a program to reverse a number using a while loop.

num = int(input("enter a number:"))

reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num// 10

print("Reversed number:", reverse)

# OUTPUT:
# ==========
# enter a number:2345
# Reversed number: 5432

# =============================================================

# 7.Write a program to print the following pattern using nested loops:

# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1 , 6):
    for j in range(i):
        print("* ",end="")
    print()

# OUTPUT:
# ==========
# * 
# * * 
# * * *
# * * * *
# * * * * *

# ======================================================================

# 8.Write a program to check whether a given number is a prime number using loops.

num=int(input("enter any number : "))
count=0

for i in range(1,num+1):
    if num%i==0:
        count+=1

if count==2:
    print(num, "is a prime number")
else:
    print(num, "is a not prime number")

# OUTPUT:
# ==========
# enter any number : 43
# 43 is a prime number

# ===================================================================

# 9.Write a program to demonstrate the use of break and continue statements with a loop.

# ========================================================================

# 10.Write a program to find the factorial of a given number using a loop.

num = int(input("enter a number:"))

factorial = 1

for i in range(1 , num+1):
    factorial = factorial * i
print("factorial of num is",factorial)

# OUTPUT:
# ==========
# enter a number:5
# factorial of num is 120

# ====================================================================

# 6.Write a program to print a square pattern of stars of size N:

# ****
# ****       
# ****
# ****

for i in range(4):
    for j in range(4):
        print("*",end="")
    print()

# OUTPUT:
# ==========
# ****
# ****
# ****
# ****

# and 

# * * * *
# * * * *       
# * * * *
# * * * *


for i in range(4):
    for j in range(4):
        print("* ",end="")
    print()

# OUTPUT:
# ==========
# * * * *
# * * * *
# * * * *
# * * * *


for i in range(3):
    for j in range(3):
        print("*",end="")

    print("")


Star problems 

rows = 4

for i in range(rows, 0, -1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(i):
        print("* ", end="")
    print()

* * * * 
 * * * 
  * *
   *

rows = 5

for i in range(rows):
    for space in range(rows - i):
        print(" ",end="")

    for star in range(i):
        print("* ",end="")

    print()

         
    * 
   * * 
  * * * 
 * * * * 



for i in range(3): # 3 times 
    for j in range(3): # 3 times 
        print(i)


for i in range(3): # 3 times 
    for j in range(3): # 3 times 
        print(i,j)
    print()



for i in range(4): # 4 times 
    for j in range(4): # 4 times 
        print("*",end=" ")
    print()


# Right angle triangle 

for i in range(1,5): # 4 times 
    for j in range(i): # 4 times 
        print("*",end=" ")
    print()
print()



# Inverted right angle triangle 

for i in range(5,0,-1): # 4 times 
    for j in range(i): # 4 times 
        print(" * ",end=" ")
    print()


for i in range(5):
    for j in range()


n=4
for i in range(1,n+1): 
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("* ",end=" ")
    print()

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


num = int(input("enter a number:"))

for i in range(1 , 11):
    print(num , "X" , i , "=" , num * i)

# OUTPUT:
# ==========
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


for i in range(1 , 6):
    for j in range(i):
        print("* ",end="")
    print()

* 
* * 
* * *
* * * *
* * * * *