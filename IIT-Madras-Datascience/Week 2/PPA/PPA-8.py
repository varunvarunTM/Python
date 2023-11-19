""" Consider the following image of a chess-board: Credits
         
    Accept two positions as input: start and end.
    Print YES if a bishop at start can move to end in exactly one move.
    Print NO otherwise.
    Note that a bishop can only move along diagonals. """



a1 = "ABCDEFGH"
a2 = "12345678"
start,end = input(),input()
if a1.index(start[0]) - a1.index(end[0]) == a2.index(start[1]) - a2.index(end[1]):
    print("YES")
else:
    print("NO")