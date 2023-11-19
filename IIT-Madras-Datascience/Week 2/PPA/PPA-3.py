""" Accept an integer as input and print the time of the day.
    Use the following table for reference
    
        Input           |      Output
        T < 0           |     INVALID 
        0 <= T <= 5     |     NIGHT
        6 <= T <= 11    |     MORNING
        12 <= T <= 17   |     AFTERNOON
        18 <= T <= 23   |     EVENING
        24 <= T         |     INVALID

    The input will be a single line containing and integer.
    The output should be one of these strings: NIGHT, MORNING, AFTERNOON, EVENING, INVALID """


T = int(input())
if T < 0:
    print("INVALID")
if 0 <= T <= 5:
    print("NIGHT")
if 6 <= T <= 11:
    print("MORNING")
if 12 <= T <= 17:
    print("AFTERNOON")
if 18 <= T <= 23:
    print("EVENING")
if 24 <= T:
    print("INVALID")

    