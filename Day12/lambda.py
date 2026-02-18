# user defined functions 
# which are created or defined by the user 


# built in functions 
# functions which are already pre defined 
# print( , len() , input() , type(), int() , float(), list(),set()

# Lambda function 
# it is a special function where we can declare the whole function in a single line.

# Syntax : 

# lambda parameters : expression  ----> declaration 

# how to call ?? 

# (lambda parameters : expression)(arguments) ---> declaration + calling 


# even or odd 

def isEven(num):
    if num%2==0:
        print("Even")
    else:
        print("odd")

isEven(22)


(lambda num : print("Even") if num%2==0 else print("odd"))(22)


# Recursive function : a function calling itself  

# base condition : stops recursion , prevents infinite loop 
# recursive call : function calling itself 

'''
# syntax 

def recursion_func():
    if base_condition:
        return result 
    else:
        return recursion_func(smaller_problem)

'''

# 5! = 5*4*3*2*1

def factorial(n):

    if n==1 :
        return 1
    
    else :
        return n * factorial(n-1)
    
print(factorial(5))





