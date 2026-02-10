'''
Docstring for Day6.Operators

operators are symbols used to perform some operations between
variables , values 

types of operators 

#Arithmetic
+ , - ,* ,/(division) ,// (floor division) ,% (modulas),**(power)

# // foor division ?? always give quotient 
# / division --- always gives the quotient and gives only float value as output 
# % modulus --- always gives the remainder as an output 



# comparison 
compares two variables or values 
== , != , >,< , <= ,>=


# Assignment
=, += ,-=,*=, /=

# Logical
 AND 
if both the conditions are true then it returns true
 
 OR 
 if atleast one conditions is true then it returns true

 NOT
  returns true if false
  returns false if true  


# identity 
is --- returns true if it finds the value 

is not ---- returns true  if it doesn't find the value 



lst=[10, 20, 30 ,40]
is = 20 ?? 

# bit wise
5+3


# membership 
 in ---- returns true if the value is present in  the sequence 
 not ----returns true , if the value is not present 


for i in range():

'''
'''
print(10/5) # 2.0 (Q)
print()
print(10//5)# 2 (Q)
print()
print(10%5)# 0 (R)

print(10**3)

a=5
#a=a+1 #0+1=1
a+=1
print(a)
a*=2 #a=a*2
print(a)

b=12

# legal age 21 
# leagl for voting 18 
# AND


# operator precedence 

brackects ()
**

* , / ,// ,%
+ , -
<< , >>
& ---> bit wisw AND 
^ ---> Bitwisw XOR
| --->bitwise OR
== , != ,< , <= ,>,>=,is , is not


'''

#bit wise operators ---> deals with 0's and 1's

# Bit wise AND(&) : sets each bit to 1 , if both are 1 
# Bit wise OR(|) : sets each bit to 1 , if atlease one of the bit is 1 
# Bit wise XOR(^) : sets each bit to 1 , if only one of the bits is 1

#bit wise NOT (~) : changes 1---> 0 , 0---> 1  


a =10 
print(~a)

#bitwise left shift (<<) :left shifts by specified positions 
#bitwise right shift (>>) :right shifts by specified positions 


a =10 
print(a>>1)

print(bin(a))

a =10
print(a<<1)


a = 5
print(bin(a))
b = 3
print(bin(b))
print(a ^ b) # XOR same values --> 0 


a = 5
b = 3
print(a & b) # AND both of them should be 1 , then 1 

a = 5
b = 3
print(a | b) # OR atleast one is 1 , then 1



