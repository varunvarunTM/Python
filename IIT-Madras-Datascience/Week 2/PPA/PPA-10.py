""" Accept a real number "x" as input and print the greatest integer less than or
    equal to "x" on the first line, followed by the smallest integer greater than
    or equal to x on the second line. """

# Method 1

import math
x = float(input())
print(math.floor(x)) # floor fucntion gives largest integer less than the number given
print(math.ceil(x)) # ceil function gives the smallest integer greater than the number given

# Method 2

x = float(input())
print("{}\n{}".format(int(x),int(x)+1))