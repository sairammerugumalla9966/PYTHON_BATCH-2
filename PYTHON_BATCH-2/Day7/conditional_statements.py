# conditional statements ??

# if , else , elif , nested if 

# if statement ?? decision making 
# syntax 
'''
if condition :
    statement
    statements
    statment  

statements 
'''
# boolean value as an output 
# if condition is True then execute the if-block code 
# if condition is False get out of the if-block 

age=19

if age>=18:
    print("eligible to vote")
    print("he is a major ")
    print("he is a superman")
    print("he is batman")


password ="super1256"
if len(password) >= 8:
    print("password accepted")
else:
    print("password must be more that 8 characters")

print("if-else completed ")


username="sai"

if username=="Ram":
    print("login success")

elif username== "ram":
    print("login success")

else :
    print("login failed ")


# elif : allows you to check multiple conditions 

signal=input("enter the color : ")

if signal=="red":
    print("stop")

elif signal=="orange":
    print("get ready")

elif signal=="white":
    print("close your eyes")

elif signal=="blue":
    print("open your eyes")

else:
    print("go")


#Nested if : if inside a fi condition 

username="laxman" 
password="ram123"

if username=="laxman" :
    if password=="ram123" : 
        print("permited")


#type conversions
#type casting 
#Bit wise operator 

print(10/5) # 2.0














