# function ??
# a function is grouping a block of code in a single unit to perform a specific task.
# you group only similar kind of code 


# why ??
# code reuseabilty 
# organise the code 
# write once and use multiple times 

# syntax :

#def SampleFunction():
    #block of code 
    #block of code 
    #block of code 
    #block of code 

#def sample_function():
    #block of code 
    #block of code 
    #block of code 
    #block of code 

# naming conventions ?? 
# CamleCase Naming Convention 
# snake_case Naming convention 

'''
def SampleFunction():
    a=100
    b=200
    c=a+b
    print("sum of a and b is : ",c)
    return c

p=SampleFunction()
print(p)


# function with parameters 


#def sample_function(parameters): # 
    #pass

#sample_function(Arguments) # 



#a=77
#b=50
def sample_function(a,b): # 
    c=a+b
    return c

#print(sample_function(567,876)) # 

#print(sample_function(100,675))

#print(sample_function(10,00))


def sample_function1(a,b): # 
    c=a+b
    return c

#print(sample_function(a,b))
#print(sample_function1(a,b))

print(sample_function(100,675))




# types of arguments :

# postional arguments 
# key word args 
# Default args 
# varibale length args or arbitary args 



# postional arguments 

def sample_function2(a,b): # variables --> parameters
    c=a+b
    print(a)
    print(b)

    return c


print(sample_function2(90,77))

'''
# Default args 

def sample_function2(a,b=77): # variables --> parameters
    c=a+b
    print(a)
    print(b)

    return c


print(sample_function2(90,44))



# key word args 

def sample_function2(a,b): # variables --> parameters
    c=a+b
    print(a)
    print(b)

    return c

print(sample_function2(a=90,b=44))


# varibale length args or arbitary args 

def func(*args):
    return args
print(func(1,3,56,78,90,1001,"sairam"))


def func(**kwargs):
    return kwargs
print(func(name="sairam", age=20))








