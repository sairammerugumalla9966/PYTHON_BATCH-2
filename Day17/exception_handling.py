# Exception_handling

# Exception ?? 
# is also an error which occurs during the execution
# to handle the program crash we declare exceptions 

# Error ??
# program will stop executing 

# exception handling blocks 

# try 
# except 
# else 
# finally 


try:
    num = float("87")

except ValueError:
    print("error in conversion")

else:
    print("conversion is successful", num)
    print(type(num))

finally:
    print("exception completed")

'''
# custom exceptions 

class LoginError(Exception):
    pass

try :
    username = "admin"
    if username != "rocky":
        raise LoginError("invlaid username")
    
except LoginError :
    print(LoginError)

'''


class WeakPasswordError(Exception):
   pass

try:
    password ="sai"
    if len(password) < 8:
        print("password is weak")
    
except WeakPasswordError:
    print("strong password")






