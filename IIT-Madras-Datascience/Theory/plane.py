x = float(input())
y = float(input())
if x == 0 and y == 0:
    print("origin")
if x == 0 and (y > 0 or y < 0):
    print("y-axis")
if (x > 0 or x < 0) and y == 0:
    print("x-axis")
if x > 0 and y > 0:
    print("first")
if x < 0 and y > 0:
    print("second")
if x < 0 and y < 0:
    print("third")
if x > 0 and y < 0:
    print("fourth")