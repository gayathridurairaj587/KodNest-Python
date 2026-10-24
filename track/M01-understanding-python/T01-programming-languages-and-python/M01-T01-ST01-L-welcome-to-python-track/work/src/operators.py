# Arthemetic operators
print(1+2) # Addition
print(1-2) # Subtraction
print(1*2) # Multiplication
print(1/2) # Division
print(1%2) # Modulus
print(1**2) # Exponentiation
print(1//2) # Floor Division

# comparison operators
print(1==2) # Equal to
print(1!=2) # Not equal to
print(1>2) # Greater than
print(1<2) # Less than
print(1>=2) # Greater than or equal to
print(1<=2) # Less than or equal to

# Assignment operators
a = 10
print(a) # 10
a += 10 # a = a + 10
print(a) # 20
a -= 10 # a = a - 10
print(a) # 10
a *= 10 # a = a * 10
print(a) # 100
a /= 10 # a = a / 10
print(a) # 10.0
a %= 10 # a = a % 10
print(a) # 0.0
a **= 10 # a = a ** 10
print(a) # 0.0                  
a //= 10 # a = a // 10
print(a) # 0.0

#logical operators
a = True 
b = False 
print(a and b) # False
print(a or b) # True
print(not a) # False
print(not b) #True

# Identity operators
a = 10
b = 10 
print(a is b) # True
print(a is not b) # False

# Membership operators
a = [1, 2, 3, 4, 5]
print(3 in a) # True
print(6 in a) # False

# Bitwise operators
a = 2 
b = 3 
print(a & b) # 2
print(a | b) # 3
print(a ^ b) # 1
a = 5 
print(~a) # -5
print(a << b) # 40
print(a >> b) # 0