# 1. Find Area of Rectangle.

length = int(input("lenght :"))
breadth = int(input("breadth :"))
Area = length*breadth 
print("Area of Rectangle is :", Area)


# 2. Finding the Cgpa of a Student of four subjects.

java = int(input("Enter Java Marks: "))
python = int(input("Enter Python Marks: "))
c_lang = int(input("Enter C_lang Marks: "))
dbms = int(input("Enter Dbms Marks: "))

total = java + python + c_lang + dbms
Cgpa = total / 4

print("CGPA is:", Cgpa)

# 3. Finding speed of the vehicle

distance_km = float(input("Enter distance in kilometers: "))
time_hr = float(input("Enter time in hours: "))

speed = distance_km / time_hr

print("Speed of vehicle:", speed, "km/hr")



# 4. Swapping of two numbers
x = 10
y = 5

print("Before swap")
print("x:", x)
print("y:", y)

x, y = y, x   # swap

print("After swap")
print("x:", x)
print("y:", y)

# 5. What is type of name, age, height

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print("Name:", name)
print("Age:", age)
print("Height:", height)

print(type(name))
print(type(age))
print(type(height))



# 6. Calculate the multiplication and sum of two numbers?


a = int(input("a="))
b = int(input("b="))
sum = a + b
print("sum=", sum)

multiply = a * b
print("multiply=", multiply)


# 7. Create a string made of the first, middle and last character?



first = input("first=")
middle = input("second=")
last = input("last= ")
fullname = first + middle + " " + last
print("fullname =", fullname)


# 8.  Finding half of the number

a = int(input("a="))
half_of_a = a // 2
print("one half of a is:", half_of_a)




# 9. Type these numbers after the equals sign for your myTotal variable:
#    myTotal = 4 + 2 * 8 - 6
#    answer is 14 explain.


a = 4
b = 2
c = 8
d = 6
my_total = a + b * c - d
print("Mytotal=", my_total)



# 10. Highest among the Numbers

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

max = max(x,y,z)

print("Highest Number Is:" , max)
