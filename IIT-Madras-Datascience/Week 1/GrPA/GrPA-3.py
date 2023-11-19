""" Accept a sequence of five single digit numbers separated by commas as input.
    Print the product of all five numbers. """

n = input()

# METHODS
d = n.split(",")
print(int(d[0])*int(d[1])*int(d[2])*int(d[3])*int(d[4]))
    # OR
m = list(map(int,(n[::2])))
print(int(m[0])*int(m[1])*int(m[2])*int(m[3])*int(m[4]))