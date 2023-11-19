""" L is a list of runs scored by a batsman.
Each entry corresponds to the batsman's score in a match.
A score is termed a century if it is greater than or equal to 100.
A streak is a sequence of consecutive centuries.
Write a function named longest-streak that accepts a list L of
non-negative integer as argument. It should return the length of the
longest streak in the list. You can assume that L will have at least
one element that is greater than or equal to 100. So, the value you
should return should be greater than or equal to 1 """


x = [100, 200, 340, 400, 35, 67, 107, 8, 900]
def longest_streak(x):
    y = 0
    z = 0
    for i in x:
        if i >= 100:
            y += 1
        else:
            if y > z:
                z = y
            y = 0
    return z

print(longest_streak(x))
