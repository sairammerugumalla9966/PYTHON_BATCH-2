#============================================================================================================
#                                          ASSIGNMENT - 7
#============================================================================================================


# 1)Write a program to take a string from the user and:
# a.Convert it to uppercase b.Convert it to lowercase

Name = input("Enter your name: ")

print("Name in Lower Case: ", Name.lower()) 
print("Name in upper Case: ",Name.upper()) 

# 2)Write a program to count the number of vowels in a given string using string methods.

Name = "Naseem"
vowels = "aeiou"
count=0
for i in Name.lower():
    if i in vowels:
        count+=1
    
print(count)


# 3)Write a program to check whether a given string starts with a specific word using a string method.

Name = "Naseem"

print(Name.startswith('s'))



# 4)Write a program to replace all spaces in a string with a hyphen (-).

Name = "Aashfaque Naseem Ahammad"

print(Name.replace(" ","-"))


# 5)Write a program to find the length of a string without using the len() function (Hint: use a string method).

Name = "Naseem"

print(Name.__len__())  


# 6)Write a program to check whether a given string is a palindrome using string methods

x  = "sss"
rev = "".join(reversed(x))

if x==rev:
    print("yes")
else:
    print("No")


# 7)Write a program to count the number of words in a sentence.

x = "full stack developer"
words = x.split(' ')
count = 0

for i in words:
    count+=1
print(count)  


# 8)Write a program to find how many times a particular character appears in a string.

x = "Naseeemmmmahhhhammmaaaddd"
freq = {}
for i in x:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)


# 9)Write a program to remove leading and trailing spaces from a string.

def remove():
    x= "   NAseem "
    y = x.strip()
    return y

print(remove()) #calling the function



# 10)Write a program to check whether a string contains only digits using string methods.

def Digits():
    num = "123"
    result = num.isdigit()
    return result
print(Digits())



