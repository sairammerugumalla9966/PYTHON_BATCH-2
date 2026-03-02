# Operators:


num1 = int(input("Enter 1st value:"))
num2 = int(input("Enter 2nd Value:"))

# Arithmetic Operator(+, -, *, /, //, %, **, +=, -=, *=, /=)

add = num1 + num2
print("Addition:", add)

sub = num1 - num2
print("Substraction:", sub)

mul = num1 * num2
print("Multiplication:", mul)

div = num1 / num2
print("Division(Quotient):", div)

floor_div = num1 // num2
print("Floor Divison(Quotient):", floor_div)

pow = num1 ** num2
print("Power:", pow)

mod = num1 % num2
print("Modulus(Remainder):", mod)

k = 2

k += 3 
print("k = k + 3 = ", k) 

k -= 3
print("k = k - 3 = ", k)

k *= 3
print("k = k * 3 = ", k)

k /= 3
print("k = k / 3 = ", k)

# -------------------------------------------------------------------------------

# Comparison Operators/ Relational Operators (==, !=, >, <, >=, <=)

a = 10
b = 3

print("a is equal to b :", a == b)
print("a is not equal to b :", a != b)
print("a is greater than  b :", a > b)
print("a is less than b :", a < b)
print("a is greater than or equal to b :", a >= b)
print("a is less than or equal to b :", a <= b)

# ---------------------------------------------------------------------------------

# Assignment Operator (=)

a = 10  # a is equal(=) to 10

# ---------------------------------------------------------------------------------

# Logical Operators (and, or, not)

a = 10 
b = 5

print(a > 5 and b < 10) # True , True so ---> True

print(a > 20 or b < 10) # False , True so ---> True

print(not(a > 5))       # True so ---> False

# -----------------------------------------------------------------------------------

# Membership Operators (in, not in)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print (2 in numbers)

print(12 not in numbers)


Royal_Enfield = ["Himalayan", "Classic", "Gt650"]

print("Interceptor" in Royal_Enfield)
print("Classic" not in Royal_Enfield)


# -----------------------------------------------------------------------------------

# Identity Operators (is, is not)

p = 5 
q = 5 

print(p is q)
print(p is not q)



