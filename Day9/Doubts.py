
# count the frequency of each element using dictionary 


numbers = [1,2,2,2,3,3,3,1,3,4,2,4,5]
f={}

for num in numbers:
    if num in f:
        f[num]+=1
    else:
        f[num]=1
print(f)



# Find the largest and smallest numbers in a list 

numbers=[10,5,30,45,87,99,1]

L=numbers[0] # 99
S=numbers[0] # 1

for num in numbers:
    if num>L:
        L=num

    if num<S:
        S=num
    
print("Largest : ", L)
print("Smallest : ", S)

