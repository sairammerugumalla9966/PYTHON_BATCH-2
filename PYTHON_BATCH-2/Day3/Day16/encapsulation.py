# Encapsulation : binding data and methods together and restrict direct access 

class bankAccount:

    def __init__(self):
        self.balance = 0

    
    def deposit(self,amount):
        self.balance += amount

b=bankAccount()
b.deposit(5000)
print(b.balance)

b.deposit(5000)
print(b.balance)


# access specifiers :

# public 
# private 
# protected 

class bankAccount:

    def __init__(self):
        self.__balance = 5000

    def display(self):
        print(self.__balance)

b=bankAccount()
b.display()



