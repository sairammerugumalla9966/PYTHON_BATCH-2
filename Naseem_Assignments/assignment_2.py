# Assignment- 2 (Methods Of Data Types)

# 1. List (append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort)
# 2. Tuple (indexing, index, count)
# 3. Set (add, update, remove, discard, pop, copy, clear, union, intersection, difference, symmetric difference)
# 4. Dict (keys, values, items, get, update, pop, popitem, clear, copy, setdefault, fromkeys)

# --------------------------------------------------------------------------------------------------------------------------


# List


l = [100, 200, 300, 400, 500, 600]

l.append(60)
print(l)


c = l.copy()
print(c)

l.count(400)
print(l)

l.index(400)
print(l)

l.insert(1, 1000)
print(l)

l.pop()
print(l)


l.reverse()
print(l)

l.sort()
print(l)


l.clear()
print(l)

# - ----------------------------------------------------------------------------------------------------

# Tuple


t = (10, 20, 30, 20)

print(t.count(20))


print(t.index(30))  


print(len(t))   


print(max(t))   


print(min(t))   


print(sum(t))   


print(sorted(t))  


# - ----------------------------------------------------------------------------------------------------

# Set

s = {10, 20, 30, 20}

s.add(40)
print(s)


s.update([50, 60])
print(s)

s.remove(20) # Error if not found
print(s)

s.discard(100) # No Error if not found
print(s)

s.pop()
print(s)


c = s.copy()
print(c)

s.clear()
print(s)


a = {1, 2, 3}
b = {3, 4, 5}


print(a.union(b))

print(a.intersection(b))

print(a.difference(b))

print(a.symmetric_difference(b))


# - ----------------------------------------------------------------------------------------------------

# Dictionary

Student_Details = {"Name":"Naseem Ahammad", "Age": 21, "Class": "10th", "Roll_No": 546, "Country": "India",}

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


print(Student_Details.keys())

print(Student_Details.values())

print(Student_Details.items())

print(Student_Details.get("Roll_No"))   

Student_Details.update({"city": "Hyderabad"})
print(Student_Details)

Student_Details.pop("Class")
print(Student_Details)

Student_Details.popitem()
print(Student_Details)

c = Student_Details.copy()
print(c)


Student_Details.setdefault("country", "USA")
print(Student_Details)                           

# Student_Details.fromkeys(["a", "b", "c"], 0) ######################### Advanced ########################## FROM KEYS
# print(Student_Details)

Student_Details.clear()
print(Student_Details)