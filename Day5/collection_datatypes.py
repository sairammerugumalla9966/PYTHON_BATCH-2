'''
Docstring for Day5.collection_datatypes

list 
tuple 
set 
dictionary 

indexing is for accessing the data 
type() - knowing the datatype 


'''
'''
# list
name="manasa"
print(type(name))


bad=[10,20,30,40,"sai",90.99]
print(bad[0])
print(bad[3])

print(bad[-1])
print(bad[-4])

nums=[78,96,40,56,67]
#append()
#insert()
#remove()
#pop()

nums.append(100)
nums.insert(1,88)
nums.remove(40)
nums.pop()
nums.sort() #asc order
nums.reverse() 
print(nums)

# print(dir(nums)) # methods of the datatype 


#tuple 

t=(10,20,20,20,30,30,30,30,30)
print(t[0]) # data is given based on index value

print(t.count(20))

print(t.index(20)) # getting the index value based on that particular data 

#print(dir(t))



#set 

s={1,2,2,3,78,56,4,4,4,}

r={77,88,99,111}

#print(dir(s))

s.add(99)
s.add(100)
s.add(67)
'''
#print(s[0]) # subcriptable : no indexing 

#print(s)

# we also have union , intersection in sets 

p={1,2,2,3,78,56,4,4,4,}
r={77,88,99,111,4}
print(p.union(r))
print()
print(r.intersection(p))


#rint(type(p))

# Dictionary 

d={"id":1,"name":"Ram"}
print(d)
print(type(d))

print(d.keys())
print(d.values())

'''
# range()
# sequence datatype 

#range(0 to n-1)
range(start, end, step)

start: starting value 
default start value =0

stop : ending value 
default stop value = n-1

step : iteration 
default value = 1
 

i=i+1 


range(1,6)

'''

# Assingment 
# practice all the methods of collection datatypes 

# today 
# colletion datatypes 
#methods of collection datatypes 
# indexing 

