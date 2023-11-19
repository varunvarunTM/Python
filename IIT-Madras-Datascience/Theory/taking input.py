
# Python program showing how to
# without split
x,y = int(input("enter a number : ")),int(input("enter a number : "))
print(x+y)

# Python program showing how to
# multiple input using split
 
# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
 
# taking two inputs at a time
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))
 
# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)

# taking input as string without spaces and converting into list of characters
x = input("enter 12345") #eg = 12345
a = list(map(int,x))
print(a)

# taking input as string without spaces and converting into list of characters
# using list comprehension
s = input("enter 12345") #eg = 12345
a = [int(i) for i in s]
print(a)

# taking input as string without spaces and converting into list of characters
# using REGEX
import re
a = input("enter 12345")
a = re.findall(r"\d",a)
print(a)

# taking input and printing at the same time
print(int(input("enter first number : ")) + int(input("enter second number : ")))