""" Accept two integers a and b as input and print the absolute difference of both the
    numbers. For example, if a=9,b=8, then the absolute difference is 9-8=1. So, your output
    should be 1. You should be able to solve this problem using the concepts covered in this
    week. """

# my response
a = int(input())
b = int(input())
print(abs(a-b))

# solution code
a = int(input())
b = int(input())

square = (b - a) ** 2
root = square ** 0.5

diff = int(root)
print(diff)