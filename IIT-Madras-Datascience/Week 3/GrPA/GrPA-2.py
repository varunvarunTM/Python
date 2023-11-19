""" Accept a positive integer n , with n > 1 , as input from the user
    and print all the prime factors of n in ascending order. """


import math
n = int(input())
for i in range(2, n):
    if n % i == 0:
        print(i)
        while n % i == 0:
            n //= i
if n > 1:
    print(n)