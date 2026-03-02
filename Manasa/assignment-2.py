1.Methods in List
=================

l1 = [10 , 20 , 30 , 40 , 50]

print(l1)        //[10, 20, 30, 40, 50]
print(type(l1))  //<class 'list'>

Indexing in List
==================

print(l1[0])  //10
print(l1[1])  //20
print(l1[2])  //30
print(l1[3])  //40
print(l1[4])  //50

Finding methods in List
=========================

print(dir(l1))

[ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']  


append()
==========

l1.append(60)
print(l1)      //[10, 20, 30, 40, 50, 60]


remove()
==========

l1.remove(20)
print(l1)      //[10, 30, 40, 50, 60]

insert()
==========

l1.insert(1,20)
print(l1)       //[10, 20, 30, 40, 50, 60]


clear()
===========

l1.clear()
print(l1)   //[]


l2 = [45 , 67 , 34 , 78 , 19 , 93 , 43]
print(l2)      //[45, 67, 34, 78, 19, 93, 43]

sort()
========

l2.sort()
print(l2)      //[19, 34, 43, 45, 67, 78, 93]

reverse()
===========

l2.reverse()
print(l2)      //[93, 78, 67, 45, 43, 34, 19]

extend()
===========

l1.extend(l2)
print(l1)       //[10, 20, 30, 40, 50, 93, 78, 67, 45, 43, 34, 19]

l3 = [10 , 20 , 40 ,  20 , 50 , 40 , 50 ]
print(l3)        //[10, 20, 40, 20, 50, 40, 50]

count()
========

count = l3.count(20)
print(count)     //2

copy()
=========

l4 = l3.copy()
print(l4)        //[10, 20, 40, 20, 50, 40, 50]


==============================================================================


2.Methods in tuples:
======================

t1 = (45 , 56 , 23 , 12 , 89 , 43 , 90 )

print(t1)          //(45, 56, 23, 12, 89, 43, 90)
print(type(t1))    //<class 'tuple'>

Indexing
===========

print(t1[0])   //45
print(t1[1])   //56
print(t1[2])   //23
print(t1[3])   //12
print(t1[4])   //89
print(t1[5])   //43
print(t1[6])   //90

Finding methods in tuple
==========================

print(dir(t1))

['count', 'index']

index()
=========

print(t1.index(56))  //1
print(t1.index(89))  //4
print(t1.index(23))  //2


t2 = (10 , 20 , 30 , 20 , 10 , 20)
print(t2)    //(10, 20, 30, 20, 10, 20)

count()
=========

print(t2.count(20))  //3


============================================================================

3.Methods in Set
==================

s = {1 , 12 , 34 , 17 , 12 , 1 , 9 , 34 , 1 , 12}

print(s)          //{1, 34, 17, 9, 12}
print(type(s))    //<class 'set'>

Finding methods
=================

print(dir(s))

['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

Indexing
===============
print(s[0])

add()
=========

s.add(7)
print(s)       //{1, 34, 17, 7, 9, 12}

remove()
============

s.remove(34)   //{1, 17, 7, 9, 12}
print(s)

pop()
=========

s.pop()
print(s)       //{17, 7, 9, 12}

copy()
==========

s1 = s.copy()
print(s1)      //{17, 12, 9, 7}

discard()
==============

s1.discard(9)
print(s1)      //{17, 12, 7}


a = {1 , 2 , 2 , 3 , 3 , 3 , 4 , 4 , 7 , 8}
print(a)   //{1, 2, 3, 4, 7, 8}

b = {1 , 1 , 2 , 2 , 2 , 2 , 5 , 6}
print(b)   //{1, 2, 5, 6}

union()
=========

print(a.union(b))    //{1, 2, 3, 4, 5, 6, 7, 8}

intersection()
===================

print(a.intersection(b))   //{1, 2}

difference()
===============

print(a.difference(b))    {8, 3, 4, 7}


difference_update()
======================

a.difference_update(b)
print(a)                //{3, 4, 7, 8}


symmetric_difference()
========================

print(a.symmetric_difference(b))  //{1, 2, 3, 4, 5, 6, 7, 8}

symmetric_difference_update()
================================

a.symmetric_difference_update(b)
print(a)                           //{1, 2, 3, 4, 5, 6, 7, 8}

intersection_update()
==========================

a.intersection_update(b)
print(a)                  //{1, 2}

isdisjoint()
==============

print(a.isdisjoint(b))    //False

issubset()
=============

print(a.issubset(b))    //True

issuperset()
================

print(a.issuperset(b))   //False

clear()
=========

a.clear()
print(a)       //set()


======================================================================

4.Methods in dict
===================

employee = {"id" : 1 , "name" : "Manasa" , "mail" : "manasa@gmail.com" , "role" : "full stack developer"}

print(employee)    //{'id': 1, 'name': 'Manasa', 'mail': 'manasa@gmail.com', 'role': 'full stack developer'}

print(type(employee))  //<class 'dict'>

Finding Methods
===================

print(dir(employee))

 ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

keys()
========

print(employee.keys())   //dict_keys(['id', 'name', 'mail', 'role'])

values()
============

print(employee.values()) //dict_values([1, 'Manasa', 'manasa@gmail.com', 'full stack developer']) 

copy()
=========

employee1 = employee.copy()
print(employee1)             //{'id': 1, 'name': 'Manasa', 'mail': 'manasa@gmail.com', 'role': 'full stack                                           
                                     developer'}


get()
======

print(employee.get('mail'))    //manasa@gmail.com

items()
==========

print(employee.items())

//dict_items([('id', 1), ('name', 'Manasa'), ('mail', 'manasa@gmail.com'), ('role', 'full stack developer')])

update()
==========

employee.update({"salary" : 30000 , "mobileno" : 1234567890})
print(employee)

////{'id': 1, 'name': 'Manasa', 'mail': 'manasa@gmail.com', 'role': 'full stack developer', 'salary': 30000, 'mobileno': 1234567890}


pop()
=======

d = employee.pop('mobileno')
print(d)                        //1234567890

popitem()
==========

print(employee.popitem())  //('role', 'full stack developer')

setdefault()
=============

employee.setdefault("mobileno" , 1234567890)
print(employee)          //{'id': 1, 'name': 'Manasa', 'mail': 'manasa@gmail.com', 'mobileno': 1234567890}


clear()
==========

employee.clear()
print(employee)      //{}



============================================================================================================
                                       OPERATORS  ============================================================================================================


operators
===========

1.Arithmetic operators(+ , - , * , / , % , ** , // , += , -= , *= , /= )
=========================================================================

p = int(input("enter p"))
print(p)  36
q = int(input("enter q"))
print(q)  6

OUTPUT:
=========

enter p 36
36
enter q 6
6

Addition
==========

addition = p + q
print(addition) 

OUTPUT:
========
 42

subtraction
=============

subtraction = p - q
print(subtraction)  

OUTPUT:
=========
30

Multiplication
================

multiplication = p * q
print(multiplication) 

OUTPUT:
=========
 216

Division
============

division = p / q
print(division)

OUTPUT:
=========
  6.0

Modulus
==========

modules = p % q
print(modules)

OUTPUT:
=========
  0

Floor Division
================

floor_division = p // q
print(floor_division) 

OUTPUT:
========
 6

Power
=========

a = 6
print(a ** 2)

OUTPUT:
=========
 36

a += 3
print(a) 

OUTPUT:
========
 9

a -= 4
print(a)

OUTPUT:
========
  5

a *= 9
print(a)

OUTPUT:
=========
 45

a /= 5
print(a) 

OUTPUT:
=========
 9.0


====================================================================

2.comparsion(== , != , > , >= , < , <=)
==========================================

m = 10
n = 10

print(m==n) 

OUTPUT:
========
True

print(m!=n)

OUTPUT:
=========
 False

age = 23
voting_age = 18

print(age>=voting_age) 

OUTPUT:
=========
True

marks = 75
pass_marks = 35

print(marks<=pass_marks)

OUTPUT:
=========
 False

a = 25
b = 10

print(a>b) 

OUTPUT:
=========
 True

print(a<b)

OUTPUT:
=========
  False

=====================================================================

3.logical(and , or , not)

marks = 75

print(marks >= 35 and marks <= 100)  

OUTPUT:
=========
True

print(marks >= 35 or marks <= 60)

OUTPUT:
=========
True

a = True
print(not a)  

OUTPUT:
=========
False

raining_outside = False
print(not raining_outside) 

OUTPUT:
=========
 True

=======================================================================

4.identity(is , is not)
==========================

l1 = [10 , 20 , 30]
l2 = [10 , 20 , 30]

print(l1 is l2)  

OUTPUT:
=========
#False

print(l1 is not l2)

OUTPUT:
=========
 True

l1 = [10 , 20 , 30]
l2 = l1

print(l1 is l2)

OUTPUT:
=========
 True

print(l1 is not l2)

OUTPUT:
=========
 False

========================================================================

5.membership(in , not)
========================

names = ["manu" , "jyoshu" , "rami reddy" , "pravathi"]

print("rami reddy" in names) 

OUTPUT:
=========
True

print("pandu" not in names) 

OUTPUT:
=========
True

fruits = ["grapes" , "mango" , "banana" , "apple"]

print("mango" not in fruits )

OUTPUT:
=========
 False

print("sapota" in fruits) 

OUTPUT:
=========
False

