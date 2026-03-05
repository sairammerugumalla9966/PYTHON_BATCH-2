# OOPS  concepts 
# Object Oriented Programming System 

# class ---> a class is a blue print used for creating objects 
# properties --->> variables 
# functinality -->> methods 
# class --->> contains variables and methods 



# object ---> an object is an instance of class 
'''
# syntax:

class Store:
    pass

s=Store()
print(s)

'''
'''
class Store:
    name="Rocky"
    age=29

s=Store()
print(s.name) 
print(s.age) # accessing thenvaribales using object 


class Store:
    name="Rocky"
    age=29

s=Store()
s1=Store()

print(s1.name) 
print(s1.age) 

print(s.name) 
print(s.age) 



class Store:
    name="Rocky_Bhai"
    age=29

    def method1(self):
        print("method1 is accessed")


s=Store()
s1=Store()

# 
print(s.name)

print(s1.name)


# Constructor (__init__)

# is a method used to initialize attributes and methods. 
# __init__ method will automatically execute when an object is created 
# stores the intial atrributes and methods in oject 

# syntax:
def __init__(self , paramter1 , parameter2):
    self.paramter1=paramter1
    self.parameter2=parameter2


# simple constructor 

class ConstructorClass:

    def __init__(self):
        print("executed automatically ")

    def Timepass(self):
        print("timepass successfully done")

obj=ConstructorClass()
obj.Timepass()


# constructor with parameter

class ConstructorClass:

    def __init__(rambo,name):
        rambo.name=name
        print("executed automatically ")

    def Timepass(rambo,age):
        rambo.age=age
        print("timepass successfully done")
        print("My age is : ",age)

obj=ConstructorClass("Rocky")
obj.Timepass(25)
print(obj.name)

'''

# multiple parameters 

class ConstructorClass:
    

    def __init__(rambo,name,branch):
        rambo.name=name
        rambo.branch=branch
        print("executed automatically ")

    def Timepass(rambo,age):
        rambo.age=age
        print("timepass successfully done")
        print("My age is : ",age)

obj=ConstructorClass("Rocky","Python developer")
obj.Timepass(25)
print(obj.name)
print(obj.branch)



