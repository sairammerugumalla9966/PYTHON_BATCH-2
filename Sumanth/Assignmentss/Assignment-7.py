# 1)Write a program to take a string from the user and:
# a.Convert it to uppercase b.Convert it to lowercase

s = input("Enter your name: ")

print(s.lower()) #it converts the name into lowercases
print(s.upper()) #it converts the name into uppercases

# output:
# Enter your name: sumantH
# sumanth
# SUMANTH

# ========
# 2)Write a program to count the number of vowels in a given string using string methods.

# 1st approach: 

s = "sumAnth"
vowels = "aeiou"
count=0
for i in s.lower():
    if i in vowels:
        count+=1
    
print(count)

# output:
# 2

# 2nd approach: 

s = "sumAnth"
s = s.lower()
vowels = "aeiou"
count=0
for i in vowels:
    count += s.count(i)
print(count)

# output:
# 2

# ==============
# 3)Write a program to check whether a given string starts with a specific word using a string method.

s = "sumanth"

print(s.startswith('s'))

# output:
# --
# True

# =========
# 4)Write a program to replace all spaces in a string with a hyphen (-).

s = "Arisinapalli sumanth"

print(s.replace(" ","-"))

# output:
# --
# Arisinapalli-sumanth

# ==========
# 5)Write a program to find the length of a string without using the len() function (Hint: use a string method).

s = "sumanth"

print(s.__len__())  #we cannot use len(), we can use the string’s internal method __len__() 

# output:
# 7

# ==========
# 6)Write a program to check whether a given string is a palindrome using string methods

s = "sss"
rev = "".join(reversed(s))

if s==rev:
    print("yes")
else:
    print("No")

# output:
# yes

# =======
# 7)Write a program to count the number of words in a sentence.

sen = "full stack developer"
words = sen.split(' ')
count = 0

for i in words:
    count+=1
print(count)  

# output:
# 3

# ======
# 8)Write a program to find how many times a particular character appears in a string.

s = "sumanntth"
freq = {}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)

# output:
# {'s': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 2, 't': 2, 'h': 1}

# =====
# 9)Write a program to remove leading and trailing spaces from a string.

def remspa():
    
    s= "     sumanth "
    new_s = s.strip()
    return new_s

print(remspa()) #calling the function

# output:
# sumanth
# sumanth 
#    sumanth 

# =======
# 10)Write a program to check whether a string contains only digits using string methods.

def stdigit():
    s = "123"
    result = s.isdigit()
    return result

print(stdigit())

# output:
# True
