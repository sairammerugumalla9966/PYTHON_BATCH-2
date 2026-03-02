# Assignment 10
# ===============================================================

# 1. password checker (functions , loops , conditional startements)

# def password_checker(name,password):
#     if name=="Manasa" and password=="Manu@12":
#         print("Login successfull")

#     else:
#         print("Login unsuccessfull")


# password_checker("Manasa","Manu@12")
# password_checker("manasa","manasa@12")

# Login successfull
# Login unsuccessfull


# 2. Log file analyzer (string+list+dictinary+set)

# Sample log lines
# logs = [
#     "INFO User1 Login",
#     "ERROR User2 PaymentFailed",
#     "INFO User1 Logout",
#     "WARNING User3 LowBalance",
#     "ERROR User2 Timeout"
# ]

# log_count = {}
# unique_users = set()

# for line in logs:
#     parts = line.split()      # string → list
#     level = parts[0]
#     user = parts[1]

#     # Count log levels
#     if level in log_count:
#         log_count[level] += 1
#     else:
#         log_count[level] = 1

#     # Add unique users
#     unique_users.add(user)

# print("Log Level Count:", log_count)
# print("Unique Users:", unique_users)

# Log Level Count: {'INFO': 2, 'ERROR': 2, 'WARNING': 1}
# Unique Users: {'User1', 'User2', 'User3'}

# 3. simple payment system (abstraction+overriding)

# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass


# class CreditCard(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Credit Card")


# class UPI(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using UPI")


# p1 = CreditCard()
# p1.pay(500)

# p2 = UPI()
# p2.pay(1000)

# Paid 500 using Credit Card
# Paid 1000 using UPI


# 4. database connection class (inheritance + constructor overriding)
# class Database:
#     def __init__(self, host):
#         self.host = host
#         print("Base Database Connected")

# class MySQL(Database):
#     def __init__(self, host, user):
#         super().__init__(host)
#         self.user = user
#         print("MySQL Connected")

# db = MySQL("localhost", "root")
# Base Database Connected
# MySQL Connected
# 5. using *args and *kwargs for API request builder
# def build_request(endpoint, *args, **kwargs):
#     print("Endpoint:", endpoint)
#     print("Positional Params:", args)
#     print("Keyword Params:", kwargs)

# build_request(
#     "/users",
#     101, 102,
#     method="GET",
#     auth="token123"
# )
# Endpoint: /users
# Positional Params: (101, 102)
# Keyword Params: {'method': 'GET', 'auth': 'token123'}

# 6. product price calculator (functions + default and keywords)
# def calculate_price(price, tax=5, discount=0):
#     final = price + (price * tax / 100) - discount
#     return final

# print(calculate_price(1000))  
# print(calculate_price(1000, tax=10))
# print(calculate_price(1000, discount=50))

# 1050.0
# 1100.0
# 1000.0
# 7. logging frameworks (duck typing + polymorphism)
# class FileLogger:
#     def log(self, message):
#         print("File Log:", message)

# class ConsoleLogger:
#     def log(self, message):
#         print("Console Log:", message)

# def process_log(logger):
#     logger.log("System Started")

# f = FileLogger()
# c = ConsoleLogger()

# process_log(f)
# process_log(c)

# File Log: System Started
# Console Log: System Started





