""" Accept two positive integers x and y as input. Print the number of digits in xy.
    You should be able to solve this problem using the concepts covered in week-1. """

x , y = int(input()) , int(input())
z = str(x ** y)
print(len(z))