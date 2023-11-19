""" Accept a string as input and print PALINDROME if it is a palindrome,
    and NOT PALINDROME otherwise. """

# my response

x = input()
y = (x[::-1])
if x == y:
    print("PALINDROME")
else:
    print("NOT PALINDROME")


# solution code