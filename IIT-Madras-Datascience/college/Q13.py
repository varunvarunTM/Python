"""
Q13) Write a Program to generate Fibonacci series till 100.


"""

a = 0
b = 1
while a <= 100:
    print(a, end=' ')
    a, b = b, a+b