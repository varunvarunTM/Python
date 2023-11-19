""" Accept two strings as input and form a new string by removing all characters from the
    second string which are present in the first string. Print this new string as output.
    You can assume that all input strings will be in lower case. """

# my response

a = input()
b = input()
for i in a:
    if i in b:
        b = b.replace(i,"")
print(b)


# solution code