""" Consider two non-empty strings a and b of lengths n(1) and n(2) respectively,
    which contain only numbers as their characters. Both the strings are in ascending order,
    that is a[i] ≤ a[j] for 0 ≤ i < j < n(1). The same holds true for b.
    You need to merge both the strings into one string of length n(1) + n(2) such that all
    the characters of this combined string are also in ascending order.

    Accept a and b as input and print this merged string as output. """

# my response

a = input()
b = input()
c = a + b
c = sorted(c)
print("".join(c))



# solution code