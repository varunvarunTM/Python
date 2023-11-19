""" Accept a five digit number as input and print the sum of its digits as output. """


x = input()
a = list(map(int,x))
print(sum(a))

    # OR

print(sum(list(map(int,input()))))