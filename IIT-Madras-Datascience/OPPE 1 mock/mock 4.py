""" Write a function named identical that accepts a dictionary P and an
integer val as arguments. Both the keys and values of P are integers.
The function should return -1 if val is not a value corresponding to
any key in dictionary. If val is one of the values then function should
return the difference between the maximum and minimum keys that have a
value of val. If there is only one key corresponding to val,
it represents both the maximum & minimum.
 """

x = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
y = 4
z = []
for i in x:
    if x[i] == y:
        z.append(i)
if len(z) == 0:
    print(-1)
elif len(z) == 1:
    print(z[0])
else:
    print(max(z) - min(z))
