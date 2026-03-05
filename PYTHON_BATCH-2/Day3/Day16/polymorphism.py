# polymorphism : ploy -->> many , morphs --->> forms 
# an ability to do more than one task 


# operator overloading :

# + (addition operator) 5+6
# " im "  +  " fine "

# *args---> multiple arguments    * --> multiplication 

# / ---> division , /n ---> next line  


# polymorphism in function : method overloading 

print("sairam" + "is a don")

print(45 + 67)
# static polymorphism or compile time polymorphism 
# combination of methhod overloading and operator overloading 



# method overridding 
# run time ploymorphism or dynamic polymorphism 

class parent:
    def method1(self):
        print("this is parent method")


class child(parent):
    def method1(self):
        print("this is child method")


obj=child()
obj.method1()
# obj.method()


