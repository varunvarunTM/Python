"""
Q12) Write a Program to computer factorial of a given number 

"""

x = int(input("Enter a number: "))
fact = 1
for i in range(1, x+1):
    fact = fact * i
print(fact)


# shortened

import math
x = int(input("Enter a number: "))
fact = math.factorial(x)
print(fact)

