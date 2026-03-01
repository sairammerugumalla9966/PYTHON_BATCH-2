# 1) Write a program to print numbers from 1 to N using a loop.

num = int(input("enter a number:"))

for i in range(1 , num+1):
    print(i)

# OUTPUT:
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

# ====
# 2)Write a program to find the sum of all even numbers between 1 and N using a loop.

n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    if i%2==0:
       sum+=i
print(sum)

# output:
# Enter a number: 10
# 30

# ====
# 3)Write a program to reverse a given number using a loop.

num = int(input("enter a number: "))

rev = 0
while num>0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num//10
print("reversed number is: ",rev)

# output:
# enter a number: 123
# reversed number is: 321

# ========
# 4)Write a program to count the number of digits in a given number using a loop.

num = int(input("enter a number:"))
count = 0

while num != 0:
    num = num // 10
    count += 1

print(count)

# output:
# enter a number:126
# 3

# =========
# 5)Write a program to generate the multiplication table of a given number up to 10.

num = int(input("Enter a number: "))

for i in range(1,11):
    print(f"multliplication of {num} * {i}: ",num*i)

# output: 
# Enter a number: 5
# multliplication of 5 * 1:  5
# multliplication of 5 * 2:  10
# multliplication of 5 * 3:  15
# multliplication of 5 * 4:  20
# multliplication of 5 * 5:  25
# multliplication of 5 * 6:  30
# multliplication of 5 * 7:  35
# multliplication of 5 * 8:  40
# multliplication of 5 * 9:  45
# multliplication of 5 * 10:  50

# =====
# 6)Write a program to print a square pattern of stars of size N:

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

# OUTPUT:
# ****
# ****
# ****
# ****

for i in range(1 , 5):
    for j in range(1 , 5):
        print("* ",end=" ")
    print()

# OUTPUT:

# * * * * 
# * * * * 
# * * * *
# * * * *

# =========
# 7)Write a python program to print a complete diamond shape using stars (*) with nested loops.

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()
    
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()

# output:

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# =====
# 8) 8.Write a python program to display this table using nested loops.


# 1 2 3 4 5 
# 6 7 8 9 10 
# 11 12 13 14 15
# 16 17 18 19 20

num = 1
for i in range(1,6):
    for j in range(1,6):
        print(num,end=" ")
        num+=1
    print()

# output:

# 1 2 3 4 5 
# 6 7 8 9 10 
# 11 12 13 14 15
# 16 17 18 19 20
