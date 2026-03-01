# 1. password checker (functions , loops , conditional startements)

def password_checker():
    passwords = ["sumanth234","Leo@2342"]
    for password in passwords:
        if len(password) >= 8:
            print("strong password")
        else:
            print("weak password")
        
password_checker()

# output:
# -----
# strong password
# strong password

# ==========

# 2) Log file analyzer(string+list+dictinary+set)

#list stores the multiple logs
logs = [
    "2026-02-22 INFO User1 Login Successful",
    "2026-02-22 ERROR User2 Login Failed",
    "2026-02-22 INFO User1 Logout",
    "2026-02-22 ERROR User1 Login Failed",
    "2026-02-22 WARNING User3 Password Attempt"
    ]

Error_count = 0
log_level_count = {}
unique_users = set() 

for line in logs:
    
    lines = line.split()
    log_level = lines[1]
    user = lines[2]
    
    if log_level == "ERROR":
        Error_count+=1
        
    if log_level in log_level_count:
        log_level_count[log_level]+=1
    else:
        log_level_count[log_level]=1
        
    unique_users.add(user) #it stores unique users
    
print("Total Error Logs: ",Error_count)
print("Log_level_count: ",log_level_count)
print("Unique Users:", unique_users)
print("Number of Unique Users:", len(unique_users))

# output:
# -----
# Total Error Logs:  2
# Log_level_count:  {'INFO': 2, 'ERROR': 2, 'WARNING': 1}
# Unique Users: {'User2', 'User3', 'User1'}
# Number of Unique Users: 3

# ==========
# 3)simple payment system (abstraction+overriding)


from abc import ABC,abstractmethod

class payment:
    
    def __init__(self,balance):
        self.balance = balance
    
    @abstractmethod
    def process_amount(self,amount):
        pass

class upi(payment):
    
    def process_amount(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            print("payment sucessful"+" "+"remaining Balance: ",self.balance)
        else:
            print("insufficient balance")
    
phonepe = upi(5000)

phonepe.process_amount(1000)

# output:
# ----
# payment successful remaining amount: 4000

# =========

# 4) database connection class (inheritance + constructor overriding)


class Databaseconnection:
    
    def __init__(self,host,user_name,password,database_name):
        self.host = host
        self.user_name = user_name
        self.password = password
        self.database_name = database_name
        
    def connect(self):
        print("connecting database....")
    
class mysql(Databaseconnection):
    
    def __init__(self,host,user_name,password,database_name,port):
        
        super().__init__(host, user_name, password, database_name)
        self.port = port
        
    def connect(self):
        print(f"connecting to mysql database..{self.host}:{self.port}")
        
obj = mysql("local","sumanth","123sj8","sql",3000)
obj.connect()

# output:
# ----
# connecting to mysql database..local:3000

# ==========

#5. using *args and *kwargs for API request builder

class Apirequestbuilder:
    
    def api(self,*args,**kwargs):
        
        #taking argumernts and urls
        base_url = "https://example.com"
        add_args = "/".join(args)
        full_url = f"{base_url}/{add_args}"
        
        #taking keyword argumens like requests from user
        
        method = kwargs.get("method","GET")
        security = kwargs.get("security",{})
        status = kwargs.get("status",{})
        Details = kwargs.get("Details",{})
        
        #creation of Api
        
        print("URL: ",full_url)
        print("Method: ",method)
        print("Security: ",security)
        print("status: ",status)
        print("Details: ",Details)
        print("-----Api creation successful------")
        
obj = Apirequestbuilder()
obj.api(
    "sumanth", "21N31A7303",
    method="POST",
    security={"autencation": "tokrn123"},
    status = {"active":True},
    Details = {"name": "sumanth","role": "software developer"}
    
)

# output:
# -----
# URL:  https://example.com/sumanth/21N31A7303
# Method:  POST
# Security:  {'autencation': 'tokrn123'}
# status:  {'active': True}
# Details:  {'name': 'sumanth', 'role': 'software developer'}
# -----Api creation successful------

# =============


# 6. product price calculator (functions + default and keywords)

#product = price and quantity and if require taxes, platform fee and delivery fee

class price_calculator:
    
    def product_calculations(self,price,Discount=0,delivery_fee=10):
        
        Discount_amount = price * (Discount/100)
        price_after_discount = price - Discount_amount
        
        total_bill = price_after_discount + delivery_fee
        
        return total_bill
    

obj = price_calculator()

print(obj.product_calculations(price=10000,Discount=20))

# output:
# ---
# 8010.0

# =========
# 7)logging frameworks (duck typing + polymorphism)

class ConsoleLogger:
    def log(self, message):
        print(f"[Console] {message}")


# File Logger
class FileLogger:
    def log(self, message):
        print(f"[File] Writing '{message}' to file...")


# Database Logger
class DatabaseLogger:
    def log(self, message):
        print(f"[Database] Inserting '{message}' into database...")


# Application Service
class Application:
    def __init__(self, logger):
        self.logger = logger   # No type checking!

    def process(self):
        self.logger.log("Application started")


# Using different loggers
app1 = Application(ConsoleLogger())
app1.process()

app2 = Application(FileLogger())
app2.process()

app3 = Application(DatabaseLogger())
app3.process()

# output:
# ----
# [Console] Application started
# [File] Writing 'Application started' to file...
# [Database] Inserting 'Application started' into database...
