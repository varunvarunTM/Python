# First method
n = input()
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])
e = int(n[4])
print(a+b+c+d+e)

# Second method
a = list(map(int,n))
print(sum(a))
# Sum is used to find sum of all int characters of a list