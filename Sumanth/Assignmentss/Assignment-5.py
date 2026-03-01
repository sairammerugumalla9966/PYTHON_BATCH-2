# 1.Write a program to print numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)

# OUTPUT: 
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

# =======

# 2)Write a program to print even numbers between 1 and 50 using a loop.

for i in range(1 , 51):
    if(i%2==0):
        print(i)

# OUTPUT:
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

# ====
# 3)Write a program to calculate the sum of first N natural numbers using a while loop.

num = int(input("Enter a number: "))
sum = 0
i=1

while i<=num:
    sum += i
    i += 1
print("sum of n natural numbers is: ",sum)

# ouput:
# Enter a number: 10
# sum of n natural numbers is: 55

# ====
# 4)Write a program to display the multiplication table of a given number using a for loop.

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

# ===

# 5)Write a program to count the number of digits in a given number using a loop.

num = int(input("enter a number:"))
count = 0

while num != 0:
    num = num // 10
    count += 1

print(count)

# output:
# enter a number:126
# 3

# # ======
# # 6)Write a program to reverse a number using a while loop.

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

# ======
# 7)Write a program to print the following pattern using nested loops:

# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

# output:

# *
# * *
# * * *
# * * * *
# * * * * *

# =====
# 8)Write a program to check whether a given number is a prime number using loops.

num = int(input("enter a number: "))
is_prime = True

if num > 1:
    for i in range(2,num):
        if num%i == 0:
            is_prime=False
            break
    if is_prime:
        print("yes it is a prime number")
    else:
        print("no it's not a prime number")
else:
    print("invalid")

# output:
# enter a number: 5
# yes it is

# ========
# 9)Write a program to demonstrate the use of break and continue statements with a loop.

num= int(input("Enter a number: "))

for i in range(1,num+1):
    if i == 3:
        continue
    if i==5:
        break
    print(i)

# output:
# Enter a number: 10
# 1
# 2
# 4

#=======
#10)Write a program to find the factorial of a given number using a loop.

num = int(input("enter a number: "))

fact = 1
i = 1
while i<=num:
    fact = fact * i
    i+=1
print(f"factorial of {num} is: ",fact)

# output:
# enter a number: 5
# factorial of 5 is: 120

# =======