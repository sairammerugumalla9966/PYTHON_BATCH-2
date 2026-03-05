# inheritance ??
# the ability to use methods , attributes in a newly created class from an existing class 

# types :
# single inheritance
# child class can access all the methods and attributes of parent class but parent class can not access the child's class  
'''
class parent:
    def method1(self):
        print("iam a parent")

class child(parent):
    def method2(self):
        print("iam a child")

child=child()
child.method2()
child.method1()

parent=parent()
parent.method1()
'''
# multiple inheritance 
# child class is created using two or more  parent classes .

class parent1:
    def method1(self):
        print("iam a parent1")

class parent2:
    def method1(self):
        print("iam a parent2")

class child(parent2,parent1):
    def method3(self):
        print("iam a child")

child=child()
#child.method2()
child.method1()
#child.method3()


#parent1=parent1()
#parent1.method1()


# multi level inheritance 

class grandparent:
    def method1(self):
        print("iam a grand parent")

class parent(grandparent):
    def method2(self):
        print("iam a parent")

class child(parent):
    def method3(self):
        print("iam a child")

child=child()
child.method2()
child.method1()
child.method3()


parent=parent()
parent.method1()
parent.method2()

grandparent=grandparent()
grandparent.method1()

# hierarical inheritance 
# child classes created from the parent class can access all the methods and attributes of the parent.

class parent:
    def method1(self):
        print("iam a parent")

class child1(parent):
    def method2(self):
        print("iam a child1")

class child2(parent):
    def method3(self):
        print("iam a child2")


# hybrid inheritance 
# combination of more than one type of inheritances 
