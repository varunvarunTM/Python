""" A bot starts at the origin — ( 0 , 0 ) — and can make the
    following moves:

        (1) UP
        (2) DOWN
        (3) LEFT
        (4) RIGHT

    Each move has a magnitude of 1 unit.
    Accept the sequence of moves made by the bot as input.
    The first entry in the sequence is always START while the last
    entry in the sequence is always STOP.
    A sample sequence is given below:

        START
        UP
        RIGHT
        LEFT
        LEFT
        DOWN
        UP
        STOP

    Print the Manhattan distance of the bot from the origin.
    If the bot is at the position ( x , y ) , then its
    Manhattan distance from the origin is given by the equation:
            
        D = | x | + | y | """


n = input()
x = 0
y = 0
while n != "STOP":
    if n == "START":
        x = 0
        y = 0
    elif n == "UP":
        y += 1
    elif n == "DOWN":
        y -= 1
    elif n == "LEFT":
        x -= 1
    elif n == "RIGHT":
        x += 1
    n = input()
print(abs(x) + abs(y))
