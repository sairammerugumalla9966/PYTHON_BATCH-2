# nested functions
# Higher order function 
# basics of OOPS 



# Difference between print() and return 

# print() :
# Display the output , used for showing the results 
# does not send any values to any function
# once print() is run , then value is gone 
# you can not reuse the printed output 


# Return :
# Sends a value back to the caller
# ends function excecution
# returned value can be stored 
# returned values can be reused 


# Nested functions 
# function inside  another function 

'''
def outer():

    def inner():
        return 
    inner()

outer()

'''

def login(username,password):

    def validate():
        return username=="Rocky" and password=="Rocky@123"
    
    if validate():
        return "Login successful"
    else:
        return "Invalid details"
    
print(login("Rocky","Rocky@123"))

#print(login("pk","pk@123"))

#print(login("Nani","Nani@123"))



def bank_acc(balc):

    def withdraw(amount):
        if amount<=balc:
            return balc-amount
        else:
            return "Insufficient balance"
        
    return withdraw(500)

print(bank_acc(499))



# Higher order functions 

# takes one or more functions as arguments 
# Return a function as a result 

#uses :
# reduces code repetition
# clean and shorter code 
# apply same login to different operations 



def operation(a,b,func):

    return func(a,b)

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

print(operation(10,5,add))
print(operation(10,5,sub))
print(operation(10,5,multiply))


# Built-in functions in higher order functions 

# map() --> 

numbers=[1,2,3,4]

def square(x):
    return x * x

result=list(map(square,numbers))
print(result)


#filter() ---> filters elements based on condition

numbers=[1,2,3,4,5,6,7,8,9,10]

def is_even(y):
    return y%2==0

result=list(filter(is_even,numbers))
print(result)


#reduce() ---> applies a function cumulatively  

from functools import reduce

numbers=[1,2,3,4,5,6,7,8,9,10]

def add(x,y):
    return x+y

result=reduce(add,numbers)
print(result)
























