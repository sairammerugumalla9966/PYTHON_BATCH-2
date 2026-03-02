# 1.Write a program to take a string from the user and:

#     a.Convert it to uppercase

#     b.Convert it to lowercase

# name = "My Name Is Manasa Annapureddy"
# print(name.upper())
# print(name.lower())

# MY NAME IS MANASA ANNAPUREDDY
# my name is manasa annapureddy


# 2.Write a program to count the number of vowels in a given string using string methods.

# name = "ManasaAnnapureddy"

# vowelCount = name.count('a') + name.count('e') + name.count('i') + name.count('i') + name.count('o') + name.count('u') + name.count('A') + name.count('E') + name.count('I') + name.count('O') + name.count('U')

# print("vowel count in name is" , vowelCount)

# vowel count in name is 7

# 3.Write a program to check whether a given string starts with a specific word using a string method.

# name = "My Name Is Manasa Annapureddy"
# word = input("enter the word :")

# if name.startswith(word):
#     print("The string starts with" , word)
# else:
#     print("The string does not strat with " , word)

# enter the word :My
# The string starts with My

# enter the word :manasa
# The string does not strat with  manasa



# 4.Write a program to replace all spaces in a string with a hyphen (-).

# name = "My Name Is Manasa Annapureddy"
# newName = name.replace(" ","-")
# print(newName)

# My-Name-Is-Manasa-Annapureddy

# 5.Write a program to find the length of a string without using the len() function
# (Hint: use a string method).


# name = input("enter a name ")
# count = 0
# for ch in name:
#     count+=1

# print("The length of the string is" , count)


# enter a name manasaannapureddy
# The length of the string is 17

# enter a name manasa annapureddy
# The length of the string is 18

# 6.Write a program to check whether a given string is a palindrome using string methods.

# string = input("enter a value :")

# if string == string[::-1]:
#     print("string is a palindrome")
# else:
#     print("string is not a palindrome")

# enter a value :madam
# string is a palindrome

# enter a value :manasa
# string is not a palindrome

# 7.Write a program to count the number of words in a sentence.

# name = "my name is manasa annapureddy"

# count = name.split()

# print("no of words in name is" , len(count))

# no of words in name is 5

# 8.Write a program to find how many times a particular character appears in a string.

# name = "manasa annapureddy"

# char = 'a'

# print("no of " , char, "appears in name is " , name.count(char))

# no of  a appears in name is  5

# 9.Write a program to remove leading and trailing spaces from a string.

# name = " Manasa Annapureddy "
# print(name.strip())

# Manasa Annapureddy

# 10.Write a program to check whether a string contains only digits using string methods.

# string = input("enter a value:")

# if string.isdigit():
#     print("The string contains only digits")
# else:
#     print("The string does not contains only digits")

# enter a value:567
# The string contains only digits

# enter a value:manu567
# The string does not contains only digits