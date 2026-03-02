ASSIGNMENT 8
===================================================================================

# FUNCTIONS & RECURSION 
---------------------------------------------
## SECTION 1: BUILT-IN VS USER-DEFINED FUNCTIONS
===================================================================================

### 1. Built-in Functions Practice

**Question:**
Write a program that takes a list of numbers and uses built-in functions to print:

* Maximum value
* Minimum value
* Sum of elements
* Length of the list

**Test Case 1:**
Input:
[10, 20, 5, 40]

Expected Output:
Maximum: 40
Minimum: 5
Sum: 75
Length: 4

**Test Case 2:**
Input:
[3, 3, 3]

Expected Output:
Maximum: 3
Minimum: 3
Sum: 9
Length: 3


l1 = list(map(int, input("Enter numbers: ").split()))
print(l1)
print("Maximum:",max(l1))
print("Minimum:",min(l1))
print("sum:",sum(l1))
print("Length:",len(l1))

Enter numbers: 10 20 5 40
[10, 20, 5, 40]
Maximum: 40
Minimum: 5
sum: 75
Length: 4

Enter numbers: 3 3 3
[3, 3, 3]
Maximum: 3
Minimum: 3
sum: 9
Length: 3


---
===============================================================================================
### 2. User-Defined Max, Min, Sum (Without Built-ins)

**Question:**
Write your own functions to calculate:

* Maximum
* Minimum
* Sum

Do NOT use max(), min(), sum().

**Test Case 1:**
Input:
[4, 8, 1, 9]

Expected Output:
Maximum: 9
Minimum: 1
Sum: 22

**Test Case 2:**
Input:
[-5, -2, -10]

Expected Output:
Maximum: -2
Minimum: -10
Sum: -17

numbers = list(map(int , input("enter numbers:").split()))
print(numbers)
min = numbers[0]
max = numbers[0]
sum = 0

for i in numbers:
    if i>max:
        max = i

    if i < min:
        min = i

    sum+=i

print("Maximum:" , max)
print("Minimum:" , min)
print("sum:" , sum)


enter numbers:4 8 1 9
[4, 8, 1, 9]
Maximum: 9
Minimum: 1
sum: 22  



enter numbers:-5 -2 -10
[-5, -2, -10]
Maximum: -2
Minimum: -10
sum: -17




=========================================================================================
## SECTION 2: PARAMETERS & ARGUMENTS
=========================================================================================

### 3. greet(name)

**Question:**
Create a function greet(name) that prints a greeting message.

**Test Case 1:**
Input:
greet("Sairam")

Expected Output:
Hello Sairam! Welcome to Python class.

**Test Case 2:**
Input:
greet("Anjali")

Expected Output:
Hello Anjali! Welcome to Python class.

def greet(name):
    return f"Hello {name}! Welcome to Python class"
    
print(greet("Sairam"))
print(greet("Anjali"))

# Hello Sairam! Welcome to Python class
Hello Anjali! Welcome to Python class




========================================================

### 4. calculate_total(price, quantity)

**Question:**
Create a function that returns total amount.

**Test Case 1:**
Input:
calculate_total(100, 3)

Expected Output:
300

**Test Case 2:**
Input:
calculate_total(250, 2)

Expected Output:
500

def calculate_total(price , quantity):
    return price * quantity


print(calculate_total(100 , 3))
print(calculate_total(250 , 2))

300
500

=====================================================================================

### 5. create_account(name, role="User")

**Question:**
Create a function with default role.

**Test Case 1:**
Input:
create_account("Rahul")

Expected Output:
Account created for Rahul with role User

**Test Case 2:**
Input:
create_account("AdminUser", "Admin")

Expected Output:
Account created for AdminUser with role Admin


def create_account(name , role="user"):
    return f"Account created for {name} with role {role}"



print(create_account("rahul"))

Account created for rahul with role user

def create_account(name , role):
    return f"Account created for {name} with role {role}"


print(create_account("AdminUser" , "Admin"))

Account created for AdminUser with role Admin

===========================================================================
## SECTION 3: RETURN VS PRINT
===========================================================================

### 6. Print vs Return (Square)

**Question:**
Create:

* One function that prints square
* One function that returns square

**Test Case 1:**

Input:
square_print(5)

Output:
25



def square(s):
    return s*s

print(square(5))

25

def square(s):
    print(s*s)

square(5)

25


Input:
result = square_return(5)
print(result * 10)

Output:
250

def square_return(x):
    return x * x

result  = square_return(5)
print(result * 10)

250




**Test Case 2:**
Input:
square_print(3)

Output:
9

def square(x):
    return x * x

print(square(3))
9


=========================================================================================

### 7. Function Chaining

**Question:**
Create two functions: add(a, b) and multiply(a, b).
Call multiply using result of add.

**Test Case 1:**
Input:
multiply(add(2,3),4)

Expected Output:
20



def add(a , b):
    return(a + b)

def multiply(a , b):
    return(a*b)

result = multiply(add(2 , 3) , 4)

print(result)

20


**Test Case 2:**
Input:
multiply(add(10,5),2)

Expected Output:
30

def add(a , b):
    return(a + b)

def multiply(a , b):
    return(a*b)

result = multiply(add(10 , 5) , 2)

print(result)

30

==================================================================
## SECTION 4: LOGICAL THINKING WITH FUNCTIONS
===================================================================

### 8. Even & Odd Counter

**Question:**
Write a function that returns count of even and odd numbers.

**Test Case 1:**
Input:
[1,2,3,4,5]

Expected Output:
Even count: 2
Odd count: 3

numbers = list(map(int , input("enter numbers:").split()))
print(numbers)
count=0
count1 = 0

for i in numbers:
    if i%2==0:
        count+=1
    else:
        count1+=1
print("Even count:" , count)
print("Odd count:" , count1)

enter numbers:1 2 3 4 5
[1, 2, 3, 4, 5]
Even count: 2
Odd count: 3

**Test Case 2:**
Input:
[2,4,6]

Expected Output:
Even count: 3
Odd count: 0

numbers = list(map(int , input("enter numbers:").split()))

count=0
count1=0

for i in numbers:
    if i%2==0:
        count+=1

    else:
        count1+=1

print("Even count:",count)
print("Odd count:" , count1)

enter numbers:2 4 6
Even count: 3
Odd count: 0

=============================================================================

### 9. Palindrome Checker

**Question:**
Create function is_palindrome(word).
Return True if palindrome else False.

**Test Case 1:**
Input:
is_palindrome("madam")

Expected Output:
True

def is_palindrome(x):
    if x == x[::-1]:
        return True

    else:
        return False


print(is_palindrome("madam"))

True

**Test Case 2:**
Input:
is_palindrome("python")

Expected Output:
False

def is_palindrome(x):
    if x == x[::-1]:
        return True

    else:
        return False


print(is_palindrome("python"))

False

==============================================================================
## SECTION 5: RECURSION
==============================================================================

### 10. Factorial Using Recursion

**Question:**
Write a recursive function to find factorial.

**Test Case 1:**
Input:
factorial(5)

Expected Output:
120

def factorial(n):
    if n==0 or n==1:
        return 1

    else:
        return n * factorial(n-1)

print(factorial(5))

120

**Test Case 2:**
Input:
factorial(4)

Expected Output:
24

def factorial(n):
    if n==0 or n==1:
        return 1

    else:
        return n * factorial(n-1)

print(factorial(4))

24

===========================================================================================

### 11. Fibonacci Using Recursion

**Question:**
Print first N Fibonacci numbers.

**Test Case 1:**
Input:
n = 5

Expected Output:
0 1 1 2 3

def fibonacci(n):
    if n==0:
        return 0

    elif n==1:
        return 1

    else:
         return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

n=5
for i in range(n):
    print(fibonacci(i) , end=" ")

5
0 1 1 2 3 




**Test Case 2:**
Input:
n = 7

Expected Output:
0 1 1 2 3 5 8

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

n=7
for i in range(n):
    print(fibonacci(i),end=" ")

13
0 1 1 2 3 5 8 

======================================================================================

### 12. Sum of Digits (Recursion)

**Question:**
Return sum of digits using recursion.

**Test Case 1:**
Input:
1234

Expected Output:
10


def sum(n):
    if n==0:
        return 0
    else:
        return (n % 10) + sum(n // 10)

print(sum(1234))

10





    


**Test Case 2:**
Input:
567

Expected Output:
18

def sum(n):
    if n==0:
        return 0

    else:
        return (n%10) + sum(n//10)

print(sum(567))

18

===============================================================================

### 13. Reverse String (Recursion)

**Question:**
Reverse string using recursion.

**Test Case 1:**
Input:
"python"

Expected Output:
"nohtyp"

def reverse(a):
    if a==None:
        return 0
    else:
        return a[::-1]

print(reverse("python"))

nohtyp

**Test Case 2:**
Input:
"madam"

Expected Output:
"madam"

def reverse(a):
    if a== None:
        return 0

    else:
        return a[::-1]


print(reverse("madam"))

madam

=================================================================================

### 14. Countdown Using Recursion

**Question:**
Print countdown using recursion.

**Test Case 1:**
Input:
countdown(3)

Expected Output:
3
2
1
Done!

def countdown(n):
    if n==0:
        print("!Done")

    else:
         print(n)    
         countdown(n-1)

countdown(3)

3
2
1
!Done
**Test Case 2:**
Input:
countdown(5)

Expected Output:
5
4
3
2
1
Done!

def countdown(n):
    if n==0:
        print("!Done")

    else:
        print(n)
        countdown(n-1)

countdown(5)

5
4
3
2
1
!Done

=================================================================================

### 15. Power Function Using Recursion

**Question:**
Find power without using ** operator.

**Test Case 1:**
Input:
power(2,3)

Expected Output:
8

def power(a ,b):
    if a == 0 and b==0:
        return 0

    else:
        return a**b

print(power(2 ,3))

8

**Test Case 2:**
Input:
power(5,2)

Expected Output:
25

def power(a , b):
    if a==0 and b==0:
        return 0

    else:
        return a**b

print(power(5 ,2))

25

**Test Case 3:**
Input:
power(3,0)

Expected Output:
1

def power(a,b):
    if a==0 and b==0:
        return 0

    else:
        return a**b

print(power(3 ,0))

1


====================================================================================

