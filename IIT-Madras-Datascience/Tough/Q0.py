# Print the following pattern. 
# There is exactly one space between any two consecutive numbers on any line. 
# There are no spaces at the end of any line.
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1


x = int(input())
a = x
t = ""
for n in range(2,6):
    b = n
    while a <= n:
        t = t + (str(a) + " ") 
        a = a + 1
    while n-1 > 1:
        t = t + (str(n-1) + " ")
        n = n - 1
    t = t + "1\n"    
    a = x
print(t)