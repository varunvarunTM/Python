"""
Q14) Write a Program to print a multiplication table of a given number

"""

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    