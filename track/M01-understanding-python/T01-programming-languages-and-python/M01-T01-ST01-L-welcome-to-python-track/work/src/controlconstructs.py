#controls all type of programs:

#Program 1: Check whether a number is positive.
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")

#Program 2:Check if a person is eligible to donate blood (Age >= 18)
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to donate blood")
else:
    print("Not eligible to donate blood")
    
#Program:3: Check if the temperature is above 30°C and print "Hot Day"
temperature = float(input("Enter temperature: "))

if temperature > 30:
    print("Hot Day")
    
#Program 4:Check whether a student has attended at least 75% of classes
attendance = float(input("Enter attendance percentage: "))

if attendance >= 75:
    print("Eligible to attend exam")
else:
    print("Not eligible to attend exam")

#Program 5:Check whether a number is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#Program 6:Check whether a person is eligible to apply for a driving license
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to apply for driving license")
else:
    print("Not eligible to apply for driving license")
    
#Program 7: Check whether a given year is a leap year.
year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
    
#Program 8: Compare two numbers and print the greater number.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    print("Greater number")
else:
    print("Not greater number")

#Program 9: Assign grades based on marks.
#90-100 → Grade A
#80-89 → Grade B
#70-79 → Grade C
#60-69 → Grade D
#Below 60 → Fail
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")

#Program 10: Categorize electricity usage.
#Above 500 → High 
#301-500 → Medium
#101-300 → Low
#0-100 → Very Low
units = int(input("Enter electricity units: "))

if units > 500:
    print("High")
elif units >= 301:
    print("Medium")
elif units >= 101:
    print("Low")
elif units >= 0:
    print("Very Low")
else:
    print("Invalid units")

#Program 11: scholarship Eligibility
#Marks >= 85
#Family Income < 3,00,000
marks = int(input("Enter your marks: "))
income = int(input("Enter your income: "))

if marks >= 85 and income < 300000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")

#Program 12: User Login
#Username is correct
#Password is correct
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "admin":
    print("Login successful")
else:
    print("Invalid username or password")

#Program 13: Display weekday using numbers (1-7)
day = int(input("Enter a number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")

#Program 14: Display season based on month.
#Dec, Jan, Feb → Winter case 12 | 1 | 2
#Mar, Apr, May → Summer case 3 | 4 | 5
#Jun, Jul, Aug, Sep - Rainy case 6 | 7 | 8 | 9
#Oct, Nov → Autumn case 10 | 11
month = int(input("Enter a month (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    print("Summer")
elif month == 6 or month == 7 or month == 8 or month == 9:
    print("Rainy")
elif month == 10 or month == 11:
    print("Autumn")
else:
    print("Invalid month")

#For Loop
#Program 15: Print numbers from 1 to 20.
for i in range(1, 21):
    print(i)

#Program 16: Print multiplication table of a given number.
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num * i)

#While Loop
#Program 17: Print numbers from 10 to 1.
i = 10
while i >= 1:
    print(i)
    i -= 1
#Program 18: Find factorial of a number.
num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(factorial)

#Break Statement
#Program 19: Print numbers from 1 to 20 but stop at 15.
for i in range(1, 21):
    if i == 15:
        break
    print(i)
#Program 20: Search for a number in a list using break.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input("Enter a number to search: "))

for number in numbers:
    if number == num:
        print("Number found")
        break
else:
    print("Number not found")

#Continue Statement
#Program 21: Print numbers from 1 to 20, skipping multiples of 3.
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)
#Program 22: Print odd numbers from 1 to 50.
for i in range(1, 51):
    if i % 2 == 0:
        continue
    print(i)

#Part 4 - Functions & Pass Statement 
#Functions
#Program 23: Find the cube of a number.
def cube(num):
    return num * num * num
print(cube(3))
#Program 24: Find the maximum of two numbers.
def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print(maximum(10, 20))

#Pass Statement
#Program 25: Create an empty function named display().
def display():
    pass
display()
#Program 26: Create an empty class named Student.
class Student:
    pass
s = Student()
print(s)
