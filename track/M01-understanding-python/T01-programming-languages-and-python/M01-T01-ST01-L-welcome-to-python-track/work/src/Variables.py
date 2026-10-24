name= "Gayathri"
age = 23 
print(name)
print(id(name))
print(type(name))

print("Hello Python", end=" - ")
print("Thank you Python")

print("Hello Python \nThank you Python")

# My name is Gayathri and age is 23 str + str
print(" My name is " + name + " age is " , age)
print(" My name is " + name + " age is " + str(age))

#String Formating ()f strings
print(f"My name is {name} and age is {age}")

# Single - line comments
""" Multi - line comments
Hello 
Hi 
thank you 
"""

a = 10
b = 20 
c = 30 
# a, b, c=10, 20, 30
# print(a + b + c)
a = b = c = 10
print(a + b + c)

a, b, c = "Abhi", "Ram", "Sai"
print(b)
print(a + b + c)

x, y, z = 30, 4, 8
print(x + z) # = 38
print(a + str(x)) # = Abhi30
print(b + c) # = RamSai
print(a, x) # = Abhi30
