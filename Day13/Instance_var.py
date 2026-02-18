# Instance varibales 

# defined using self.variable
# used in constructor 

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



# class varibale 

# accessed by all the objects in the class 
# defined inside the class but outside the methods.
 
class Store:
    name="Rocky_Bhai"
    age=29

s=Store()
s1=Store()
 
s.name="Rocky"
print(s.name)

