""" Accept four integers as input and write a program to print these integers in
    non-decreasing order.

    The input will be four integers in four lines.
    The output should be a single line with all the integers separated by a single
    space in non-decreasing order.

Note: There is no space after the fourth integer. """


# My response
l = []
n=4
for i in range(n):
    x = int(input())
    l.append(x)
l.sort()
print(*l)

# Solution code