#This is popularly called CAESAR CIPHER in cryptography
x = "abcdefghijklmnopqrstuvwxyz"
y = input()
k = 3
n = 0
t = ""
while True:
 t = t + x[(x.index(y[n])+k)%26]
 n = n + 1
 if n == len(y):
  break
print(t)

#solution to CAESAR CIPHER

x = "abcdefghijklmnopqrstuvwxyz"
y = input()
k = 3
n = 0
t = ""
while True:
 t = t + x[(x.index(y[n])-k)%26]
 n = n + 1
 if n == len(y):
  break
print(t)