'''
Assignment 3 :
===================================

1.Write a program to demonstrate all arithmetic operators using two user-defined numbers.

2.Write a program to compare two numbers using relational operators and display the result.

3.Explain logical operators (and, or, not) with a truth table and a sample program.

4.Write a program to check whether a number lies between 10 and 50 using logical operators.

5.Demonstrate the use of assignment operators (=, +=, -=, *=, /=) with examples.

6.Write a program to check whether a given value exists in a list using membership operators.

7.What is the difference between == and is operators?
Write a program to prove it.

8.Write a program to check whether a number is even or odd using operators.

9.Write a program to calculate the area of a rectangle using arithmetic operators and user input.

10.Explain operator precedence in Python and write a program showing how precedence affects the result.   ()()Doubt()()

=========================================================================================================

'''

# 1.Write a program to demonstrate all arithmetic operators using two user-defined numbers.

num1 = int(input("Enter 1st value:"))
num2 = int(input("Enter 2nd Value:"))

# Arithmetic Operator(+, -, *, /, //, %, **, +=, -=, *=, /=)

add = num1 + num2
print("Addition:", add)

sub = num1 - num2
print("Substraction:", sub)

mul = num1 * num2
print("Multiplication:", mul)

div = num1 / num2
print("Division(Quotient):", div)

floor_div = num1 // num2
print("Floor Divison(Quotient):", floor_div)

pow = num1 ** num2
print("Power:", pow)



# 2.Write a program to compare two numbers using relational operators and display the result.

a = 10
b = 3

print("a is equal to b :", a == b)
print("a is not equal to b :", a != b)
print("a is greater than  b :", a > b)
print("a is less than b :", a < b)
print("a is greater than or equal to b :", a >= b)
print("a is less than or equal to b :", a <= b)


# 3. Explain logical operators (and, or, not) with a truth table and a sample program.

a = 10 
b = 5

print(a > 5 and b < 10) # True , True so ---> True

print(a > 20 or b < 10) # False , True so ---> True

print(not(a > 5))       # True so ---> False


# 4. Write a program to check whether a number lies between 10 and 50 using logical operators.

number = int(input("Enter a Number: "))

if number >= 10 and number <= 50:
    print(number)

else: print("Invalid Number") 


# 5.Demonstrate the use of assignment operators (=, +=, -=, *=, /=) with examples.

k = 2

k += 3 
print("k = k + 3 = ", k) 

k -= 3
print("k = k - 3 = ", k)

k *= 3
print("k = k * 3 = ", k)

k /= 3
print("k = k / 3 = ", k)


# 6. Write a program to check whether a given value exists in a list using membership operators.

value = int(input("Enter a value: "))
lst = [10, 20, 30, 40, 50, 61, 71, 81, 91, 100]

print(value in lst)


# 7. What is the difference between == and is operators? Write a program to prove it.

student_names = ["zeena", "mairah", "aleena", "amio"]
emp_names = ["zeena", "mairah", "aleena", "amio"]

print(student_names == emp_names)   # True (same values)
print(student_names is emp_names)   # False (different memory)



# 8.Write a program to check whether a number is even or odd using operators.


number = int(input("Enter a numner"))

if number % 2 == 0:
    print(number, "It is an even Number")

else: print(number, "It is an odd number")


# 9. Write a program to calculate the area of a rectangle using arithmetic operators and user input.

length = int(input("Enter length of a Rectangle: "))
breadth = int(input("Enter Breadth of a Rectangle: "))

Area = length * breadth
print("Area of Rectangle is: ", Area)

'''
=========================================================================================================

1.Create a list of 5 student names and:

    a)Add one more name

    b)Remove one name

    c)Display the final list

2.Write a program to find the largest and smallest elements in a list without using built-in functions.

3.Create a tuple with mixed data types and:

    a)Access elements using indexing

    b)Explain why tuples are immutable

    c)Convert a tuple into a list, modify an element, and convert it back into a tuple.

4.Write a program to remove duplicate values from a list using a set.

5.Create a dictionary with employee details (id, name, salary).
Perform:

    a)Add a new key

    b)Update salary
    
    c)Delete a key

6.Write a program to iterate through a dictionary and print: Keys, Values ,Key-value pairs.

7.Declare two sets, perform and display: Union, Intersection, Difference.

8.Write a program to count the frequency of each element in a list using a dictionary.

9.Explain the difference between list, tuple, set, and dictionary with one real-time example each

10.Explain the difference between list, tuple, set, and dictionary with one real-time example each.

===================================================================================================

'''


# 1.Create a list of 5 student names and:

#    a)Add one more name

#    b)Remove one name

#    c)Display the final list


student_names = ["zeena", "mairah", "aleena", "amio","saya"]

student_names.append("libe")
print(student_names)

student_names.remove("libe")
print(student_names)

print("Final list: ", student_names)


# 2.Write a program to find the largest and smallest elements in a list without using built-in functions.

lst = [10, 20, 30, 40, 50, 60, 70]

print(min(lst))
print(max(lst)) ## DDOOUUBBTT  ##


# 3.Create a tuple with mixed data types and:

#    a)Access elements using indexing

#    b)Explain why tuples are immutable

#    c)Convert a tuple into a list, modify an element, and convert it back into a tuple.

tup = ("Naseem", 546, 'Hyderabad', 79.9)

# a
print(tup[0])
print(tup[3])

# b
# Tuples are immutable because tuples cannot be modified or changed

# c
lst = list(tup)
lst[0] = "Ahammad"
print(lst)
tup = tuple(lst)
print(tup)


# 4.Write a program to remove duplicate values from a list using a set.

lst = [10,10,20,20,30]

print("Before removing duplicates: ",lst)

sets = set(lst)
print("After Removing Duplicates :",sets)


# 5.Create a dictionary with employee details (id, name, salary).
#    Perform:

#    a)Add a new key

#    b)Update salary
    
#    c)Delete a key'

Employee_Details = {"Id": 1, "Name": "Zeena", "Salary": "23,000/-"}

# a 
Employee_Details["City"] =  "Hyderabd"
print(Employee_Details)

# b 
Employee_Details.update({"Salary": "32000/-"})
print(Employee_Details)


# c 
Employee_Details.pop("Salary")
print(Employee_Details)


# 6.Write a program to iterate through a dictionary and print: Keys, Values ,Key-value pairs.

Student_Details = {"Name":"Naseem Ahammad", "Age": 21, "Class": "10th", "Roll_No": 546, "Country": "India",}


print(Student_Details.keys())

print(Student_Details.values())

print(Student_Details.items())



# 7. Declare two sets, perform and display: Union, Intersection, Difference.

a = {1, 2, 3}
b = {3, 4, 5}


print(a.union(b))

print(a.intersection(b))

print(a.difference(b))


# 8.Write a program to count the frequency of each element in a list using a dictionary.   ##DDOOUUBBTT##

# 9.Explain the difference between list, tuple, set, and dictionary with one real-time example each

'''
Type	        Ordered 	Duplicates	   Mutable	          ExampleUse
List	          Yes	        Yes       	 Yes	       Shopping items
Tuple	          Yes	        Yes	          No	        Fixed data
Set   	           No	        No	         Yes	       Unique values
Dictionary	      Yes	    Keys_No        	Yes	           Key-value data

'''