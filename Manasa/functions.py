# def multiplication(m , n):
#     a = m * n
#     return a

# print(multiplication(5 , 7))
# print(multiplication(8 , 15))
# print(multiplication(15 , 7))
# print(multiplication(12 , 6))

# 35
# 120
# 105
# 72


# def operators(a , b):
#     c = a > b
#     return c

# print(operators(5 , 9))
# print(operators(34, 56))
# print(operators(56 , 92))
# print(operators(25 , 12))

# False
# False
# False
# True

# def division(x , y):
#     z = x/y
#     return z

# print(division(25 , 5))
# print(division(125 , 25))

# 5.0
# 5.0

# def membership():
#     names = ["manu" , "jyoshu" , "rami reddy" , "pravathi"]
#     print("rami reddy" in names)
#     print("pandu" not in names) 

# membership()

# True
# True


# def evenNumber(i):
#     if i%2==0:
#          print(i,"is a even number")
   
#     else:
#          print(i,"is a odd number")

# evenNumber(32)
# evenNumber(79)
# evenNumber(233)

# 32 is a even number
# 79 is a odd number
# 233 is a odd number

# def table_Division(a):
#     for i in range(1 , 11):
#         print(a , "X" , i , "=" , a * i )

# table_Division(24)
# table_Division(36)

# 24 X 1 = 24
# 24 X 2 = 48
# 24 X 3 = 72
# 24 X 4 = 96
# 24 X 5 = 120
# 24 X 6 = 144
# 24 X 7 = 168
# 24 X 8 = 192
# 24 X 9 = 216
# 24 X 10 = 240
# 36 X 1 = 36
# 36 X 2 = 72
# 36 X 3 = 108
# 36 X 4 = 144
# 36 X 5 = 180
# 36 X 6 = 216
# 36 X 7 = 252
# 36 X 8 = 288
# 36 X 9 = 324
# 36 X 10 = 360


# def eligibility(a):
#     if a>=18:
#         print("Eligible for voting")

#     else:
#         print("Not eligible for voting")

# eligibility(23)
# eligibility(14)
# eligibility(18)


# Eligible for voting
# Not eligible for voting
# Eligible for voting

# def list():
#     l1 = [10 , 50 , 20 , 5 , 2 , 30]
#     l1.sort()
#     print(l1)

# list()

# [2, 5, 10, 20, 30, 50]

# def dict():
#     student = {
                 
#                  "roleno" : 567,
#                  "name" : "Manasa Annapureddy",
#                  "dept" : "CSE"
#     }

#     print(student)
#     print(student.keys())
#     print(student.values())

# dict()

# {'roleno': 567, 'name': 'Manasa Annapureddy', 'dept': 'CSE'}
# dict_keys(['roleno', 'name', 'dept'])
# dict_values([567, 'Manasa Annapureddy', 'CSE'])


# def set():
#     a = {1 , 2 , 5 , 7 , 9 , 12 , 14}
#     b = {2 , 4 , 6 , 8 , 10 , 12}

#     print(a.union(b))
#     print(a.intersection(b))

# set()

# {1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 14}
# {2, 12}