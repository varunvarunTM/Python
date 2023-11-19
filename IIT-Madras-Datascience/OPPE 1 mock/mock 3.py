""" A number is called well behaved if all the digits are in non-descending
    order when read from left to right.
    Write a function named well-behaved that accept a list of positive
    integers as arguments and return the number
    of well behaved numbers in the list. """


x = [123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
count = 0
for i in x:
        a = str(i)
        if a == "".join(sorted(a)):
                count += 1
print(count)

