# Encapsulation : binding data and methods together and restrict direct access 
'''
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
'''
class bankAccount:

    def __init__(self):
        self.__balance = 5000

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance :
            self.__balance -= amount

    def display(self):
        print(self.__balance)

b=bankAccount()
b.deposit(2000)
b.display() # 7000
b.withdraw(1000)
b.display() # 6000

# Abstraction  : hiding implemention details and only show essintial details 


from abc import ABC , abstractmethod

class payment(ABC) : 

    @abstractmethod
    def pay(self , amount):
        pass

class UPI(payment):
    def pay(self , amount):
        print("payment is successful", amount)

obj=UPI()
obj.pay(500)










