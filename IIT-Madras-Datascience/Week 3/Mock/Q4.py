""" Accept a string as input, print Integer if the string is an integer,
    print Float if it a float, else print None. """

# my response

x = input()
if x.isdigit():
    print("Integer")
elif x.replace(".","",1).isdigit():
    print("Float")
else:
    print("None")


# solution code