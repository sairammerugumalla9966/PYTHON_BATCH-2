'''
# loops 

# for loop 
 # a for loops is used for iteration over a sequence . (range , list , tuple , string)

# when we know the range (how many times)

#for varibale in sequence:
    #statements 
    #statements 

employees=["sathwik", "sumanth","Naseem", "manasa","sairam"]

for emp in employees:
    print(emp, "is a super man ")

print("come out of dreams")


# strings 

name=input("enter any name")

for x in name:
    print(x)


for i in range(1,11):
    print(i)


'''
# while loop 
# when you dont know the range 
# it excecutes untill the condition is true 

# while condition :
    #statements 
    #statements 
'''
i=1
while i<=5:
    print(i)
    i+=1

'''
# prime number 
# number which is divisible by 1 and itself 

# nested loops 
#loop control statements --- pass , break , continue 
'''

# is prime number or not 

num=int(input("enter any number : "))
count=0

for i in range(1,num+1):
    if num%i==0:
        count+=1

if count==2:
    print(num, "is a prime number")
else:
    print(num, "is a not prime number")




# prime number or not using while loop 

num=int(input("enter any number : "))
count=0
i=1
while i<=num:
    if num%i==0:
        count+=1
    i+=1

if count==2:
    print(num, "is a prime number")
else:
    print(num, "is a not prime number")

'''
# first 10 prime numbers program 

# 2,3,5,7,11,13,17,.......

num=2
count=0
while count<10:
    i=1
    factor=0
    while i<=num:
        if num%i==0:
            factor+=1
        i+=1

    if factor==2:
        print(num)
        count+=1
    num+=1




