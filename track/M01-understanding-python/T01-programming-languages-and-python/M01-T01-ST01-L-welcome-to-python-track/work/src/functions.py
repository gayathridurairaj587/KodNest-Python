# add 2 numbers 
def add():
    a = 5
    b = 10
    print(a+b)
add()

# Square of a number
def square():
    a = 5
    print(a*a)
square()

# find the largest number in a list
def largest():
    a = 10
    b = 20
    c = 30
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
largest()

#check if a number is even or odd
def even_odd():
    a = 10
    if a%2 == 0:
        print("Even")
    else:
        print("Odd")
even_odd()

# greet with name
def greet():
    name = "gayathri"
    print("Hello", name)
greet()

# no arguements + no return value
def square():
    a = 5
    print(a*a)
square()

# no arguements + return value
def sqaure():
    a = 5
    return a*a
print(square())

# arguements + no return value
def square(a):
    print(a*a)
square(10)

# arguements + return value
def square(a):
    return a*a
print(square(10))