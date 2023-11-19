""" Two integers are co-prime if the only common divisor between the two integers is one.
   Accept two positive integers as input in two different lines.
   Print Coprime if the two integers are co-prime, else print Not Coprime.
   Assume that both the integers are greater than two. """

# my response

import math
a = int(input())
b = int(input())
gcd = math.gcd(a,b)
if gcd == 1:
   print("Coprime")
else:
   print("Not Coprime")


# solution code