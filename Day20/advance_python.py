# Advance python 

# decorators 
# iterators 
# generators 
# regular expressions 


# database 


# frameworks
# flask 
# Django


# Frontend 
# HTML and CSS basics 


# End to End Project explaination 


#  Real time Project Assignment  



# Decorators 
# is a callable that takes another function and returns modified callable  

# extend behaviour of functions 
# we'll add new features without modifying the original code 
 

def sample_decorator(func):
    def wrapper():
        print("before execution")
        func()
        print("after execution")
    return wrapper
    
@sample_decorator
def sample():
    print("decorator implemented")
    print("im batman")

sample()


def sample_decorator(func):
    def wrapper(args):
        print("before execution")
        func(args)
        print("after execution")
    return wrapper
    
@sample_decorator
def sample(args):
    print("decorator implemented")
    # print("im batman")
    print("msg sent :",args)

sample("not batman , im super man")


# Iterators  : 

# __iter__() : returns iterator 
# __next__() : to fetch next value 


num=[1,2,3,4,5]
it = iter(num)

print(next(it))
print(next(it))
print(next(it))
print(next(it))



# generators :  it is a function that returns an iterator using yeild keyword 


def numbers():
    yield "sai"
    yield 2
    yield 3
    yield 4

for num in numbers():
    print(num)




# regular expressions  # re module 

# pattern matching 
# searching 
# replacing 
# slitting text 


import re 

msg="happy holi to each and everyone"

match=re.search("diwali",msg)

if match:
    print("do festival")

else :
    print("no festival")



# findall()
# match()
# 


# login 

# username  gmail.com / outlook.in
# username should be only 20 characters max 

# sai.@domain@gamil.com # error not in standard format 
# if correct format # correct format 



# password 

# sairam1995@gmail.com 

# [a-z]@/[A-Z]/[0-9] 20 @ [a-z]/[A-Z] . com


# list comprehensions 




































































