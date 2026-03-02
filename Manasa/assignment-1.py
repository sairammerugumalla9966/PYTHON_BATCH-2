1.Area of a square

side = int(input("enter any value:"))

area = side * side

print("area of a square is" , area)


OUTPUT:

enter any value:5
area of a square is 25


=====================================================


2.Greatest of among 3 Numbers

a = int(input("Enter value1:"))

b = int(input("Enter value2:"))

c = int(input("Enter value3:"))

max = max(a , b , c)

print("Max Number among the given 3 Numbers is" , max)


OUTPUT:

Enter value1:20
Enter value2:15
Enter value3:40
Max Number among the given 3 Numbers is 40


========================================================


3.Swapping of 2 Numbers

c1 = 2

c2 = 7

c1 , c2 = c2,c1

print(c1 , c2)


OUTPUT:

7 2

========================================================


4.Area of a Rectangle

length =int(input("enter an value"))
breadth = int(input("enter an value"))

area = length * breadth
print("Area of a Rectangle:" , area)

OUTPUT:

enter an value15
enter an value5
Area of a Rectangle: 75

=======================================================

5.Finding the greatest among the given 2 Numbers

k = 4

l = 6

print(k>l)

OUTPUT:

False

=======================================================

6.Smallest of among given Numbers

a1 = int(input("Enter value1:"))

b1 = int(input("Enter value2:"))

c1 = int(input("Enter value3:"))

min = min(a1 , b1 , c1)

print("Min Number among the given 3 numbers is" , min)

OUTPUT:

Enter value1:23
Enter value2:45
Enter value3:2
Min Number among the given 3 numbers is 2

===================================================================

7.Accessing the elements and Printing Ṣum of elements in a list

list = [10 , 20 , 30 , 40 , 50]

print(list)

print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

print("The sum of the values in a list is",sum(list))

OUTPUT:

[10, 20, 30, 40, 50]
10
20
30
40
50
The sum of the values in a list is 150

=====================================================================

8.Finding Cube of a given Number


x = int(input("Enter a value :"))

cube = x * x * x

print("The cube of a given Number is" , cube)

OUTPUT:

Enter a value :4
The cube of a given Number is 64

=====================================================================

9.Finding Simple Interest on Savings

P = 50000 
T = 2      
R = 5    

SI = (P * T * R) / 100
print("Simple Interest is", SI)

total_amount = P + SI
print("Total amount is", total_amount)

OUTPUT:

Simple Interest is 5000.0
Total amount is 55000.0

=====================================================================

10.Finding Final balance after deposit and withdraw

balance = 20000
deposit = 7000
withdraw = 3000

balance = balance + deposit
balance = balance - withdraw

print("Final balance is", balance)


OUTPUT:

Final balance is 24000

====================================================================

11.Finding the data type of a variable

name = "Manasa"
print(name)
print(type(name))

OUTPUT:

Manasa
<class 'str'>


