#Topic: variable assigning

name= "Sumanth"
_name = "Sumanth"
name_1 = "Sumanth"
#1name = "Sumanth" #not possible variable name doesn't start with number
age = 10
Age = 10 #both are different because variable names are case sensitives
#from  = "Sumanth" #keywords doesn't valid to put a variable name

#============


#Topic: inbuilt data types

a = 10 #integer
b = "Sumanth" #string
c = 12.55 #float
d = True #boolean
e = 1 + 2j #complex -> it consists of imaginary numbers.
list1 = [1, 2, 3]    #assigning the list
tuple1 = (1, 2, 3)   #assigning the tuple
s = {1, 2, 2, 3}     #assigning the set
student = {"name": "Leo", "age": 22}  #assigning the dictionary


#=============
#Topic : Input # Take a input from the user

name = input() #this is normal input format. In python everything taken as a string on input format
name = input ("Enter your name: ")
age = int(input("enter your age")) #so you can change the integer format using int infront of input()

#======
#output format

#print("you can add information in double quotes", or directly print the input)

#==================
#Examples-------

#single variable assignments

x = 10
name = "Leo"
price = 99.5

print(x) #ouput: 10
print(name) #output : Leo
print(price) #output: 99.5

#Multiple variable assignments

a, b, c = 1, 2, 3

print(a) #output: 1
print(b) #output: 2
print(c) #output: 3

#python allows same value to multiple variables:

a = b = c = 10
#print(a) #output: 10

#example of user taken from the input

username = input("Enter your user name: ")
print(username) #Terminal : Enter your user name: Sumanth -> output: Sumanth

#=====================
#swapping the values using assigning multiple assignments

a = 5
b = 10

a, b = b, a
print(a, b) #working : a = b and b = a #output 10 5

#sum of two numbers

a = int(input("enter the number1: "))
b = int(input("enter the number2: "))
sum = a + b
print("sum of two numbers is :", sum)

#*input : 10 10
#*output: sum of two numbers is: 20

#adding integer plus Float

a = 10
b = 10.5
print(a + b) #output : 10 + 10.5 = 20.5

#adding int plus string

a = 10
b = "Sumanth"

print(a + b) 

#*output : Error-> unsupported operand because int is a numeric data and string is a text data

#adding string plus string

a = "Full stack"
b = "python"

result = a + " " + b  #adding two strings comes under string concatenation
print(result)

#*output: 
#Full stack python

#=======List example

contacts = ["Mom", "Dad", "Brother"] #input
#(or)
contacts = list(input("Enter contacts Here : ").split())

print(contacts[0])

#output: 
#['Mom']

#=======tuple example -> 

days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") #input
#(or)
days = tuple(input("Enter days separated by space: ").split())

print(days)

#output: 

#('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

#=======set example

emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}

print(emails)

#output:
#{'a@gmail.com','b@gmail.com'} #duplicates are removed because set takes only unique inputs

#====== Dict example

# student = {
#     "name": "sumanth",
#     "roll_no": 03,
#     "marks": 85.5,
#     "passed": True
# }

print(student)

#output:

#{'name': 'sumanth', 'roll_no': 03, 'marks': 85.5, 'passed': True}  #key:value pair