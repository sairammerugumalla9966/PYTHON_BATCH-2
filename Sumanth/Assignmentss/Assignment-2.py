

#collection data types
#list -> ordered, mutable and it allows duplicates
#tuple -> ordered, im-mutable and it allows duplicates
#set -> unordered, mutable and it doesn't allow duplicates
#Dictionary -> key–value pairs, mutable, keys unique

#==============================assigning and methods of list==========================================

numbers = [10, 20, 30, 40]
print(numbers)
print(type(numbers))

# output:
# [10,20,30,40]
# <class 'list'>

#METHODS OF LIST

#append -> is adds the element at the end of the index

numbers.append(50)

print(numbers)

#o/p: [10,20,30,40,50]

#insert -> adds the element at whatever index you want

numbers.insert(1,15)   #1-> index number, 15-> value of that index

print(numbers)

#o/p : [10,15,20,30,40,50]

#remove -> it can remove the value of list

numbers.remove(15)

print(numbers)

#o/p: [10,20,30,40,50]

#Pop -> it removes last item 

numbers.pop()

print(numbers)

#o/p: [10,20,30,40]

#sort -> it sorts the list by default ascending order

numbers.sort()

print(numbers)

#o/p: [10,20,30,40]

#reverse -> it reverses the list like ascending to descending

numbers.reverse()

#o/p: [40,30,20,10]

#extend -> it adds multiple items at the list

numbers. extend([50,60])

print(numbers)

#o/p: [10,20,30,40,50,60]

#index -> it finds the index of the element

numbers.index(20)

print(numbers)

#o/p: 1

#count -> it counts the how many times the value will be repeated

print(numbers.count(20))

#o/p : 1

#copy -> it creates the shallow copy like duplicate list

new_list = numbers.copy()

print(new_list)

#o/p: [10,20,30,40,50,60]

#clear -> it clears all the elements on the list

numbers.clear()

print(numbers)

#o/p: [] -->empty

#========================================Tuple methods==================================

marks = (85, 90, 78, 90)
print(marks)
print(type(marks))

# output: 
# (85,90,78,90)
# <class 'tuple'>


#count -> it counts the occurences of the element

marks.count(90)

print(marks)

output: 2


#index -> it finds the index of the element

marks.index(78)

output: 2


#================================set assigning & methods================================

nums = {1, 2, 3, 3, 4}
print(nums)
print(type(nums))

# output:
# {1,2,3,4}
# <class 'set'>


#add() – it adds the element on the set

nums.add(50)

print(nums)

# o/p : {1,2,3,4,50}

#update() – It adds multiple elements on the set

nums.update([60,70])

print(nums)

# o/p : {1,2,3,4,50,60,70}

#remove() – remove element (error if not found)

nums.remove(2)
print(nums)

# o/p: {1,3,4,50,60,70}

nums.remove(100)

print(nums)

# output: Error if not found

#discard() – it removes element (no error)

nums.discard(100)

print(nums)

#o/p : {1,3,4,50,60,70} --> using discard it ignores the errors comparing to remove

#pop() – it removes random element on the set because set is a unordered

nums.pop()

print(nums)

# o/p:
# {1,4,50,60,70}

# ***reseting the sets

A = {10, 20, 30, 40}
B = {30, 40, 50}

#union() –> it combines both the sets

print(A.union(B))

#/p: {10, 20, 30, 40, 50}


#intersection() – common elements on both the sets

print(A.intersection(B))

# o/p:
# {30, 40}

#difference() – check the elements in A not in B

print(A.difference(B))

#o/p: {10, 20}

#symmetric_difference() – checks the elements are not common on both the sets

print(A.symmetric_difference(B))

#o/p: {10, 20, 50}

#intersection_update() – update A with common elements

A.intersection_update(B)

print(A)

#o/p: {30, 40}

#difference_update() – update A by removing common elements

A.difference_update(B)
print(A) 

#o/p: {10, 20}

#issubset() – check subsets wheather set values matching or not'

C = {10, 20}

print(C.issubset(A))

#o/p: True

#issuperset() – check superset

print(A.issuperset(C))

#o/p: True

#isdisjoint() – check no common elements

D = {100, 200}

print(A.isdisjoint(D))

#o/p: True


#=========================Dictionary assigning and methods==================

student = {
    "name": "Leo",
    "age": 21,
    "course": "Python"
}

print(student)
print(type(student))

# output : 
# {"name" : "leo" ,"age" : 22, "course" : "python" }
# {class 'dict'>

#get() – get values using key

print(student.get("name"))

#o/p : Leo

#keys() – get all keys

print(student.keys())

#0/p:

#dict_keys(['name', 'age', 'course'])

#values() – get all values

print(student.values())

#o/p: 

#dict_values(['Leo', 21, 'Python'])

#items() – get key-value pairs

print(student.items())

# o/p: 

# dict_items([('name', 'Leo'), ('age', 21), ('course', 'Python')])


#update() – update / add key-value pairs

student.update({"age": 22})

print(student)

# o/p:
# {'name': 'Leo', 'age': 22, 'course': 'Python'}

#pop() – remove key and return value

student.pop("course")

print(student)

# o/p: {'name': 'Leo', 'age': 22, 'marks': 90}

#popitem() – remove last inserted item

student.popitem()
print(student)

# o/p: 
# ('marks', 90)
# {'name': 'Leo', 'age': 22}


#fromkeys() – create dictionary from keys

keys = ("id", "name", "marks")
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

# o/p: 
# {'id': 0, 'name': 0, 'marks': 0}