# Consider the following image of a chess-board:
# (NORMAL CHESS BOARD )
# Accept two positions as input: start and end. 
# Print YES if a bishop at start can move to end in exactly one move. 
# Print NO otherwise. Note that a bishop can only move along diagonals.

a1 = "ABCDEFGH"
start,end = input(),input()
x1 = start[0]
x2 = int(start[1])
y1 = end[0]
y2 = int(end[1])
if a1.index(x1) - a1.index(y1) == x2 - y2:
    print("YES")
else:
    print("NO")