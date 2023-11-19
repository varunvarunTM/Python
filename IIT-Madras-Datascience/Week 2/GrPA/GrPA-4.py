""" You are given the dates of birth of two persons, not necessarily from the same family.
    Your task is to find the younger of the two. If both of them share the same date of birth,
    then the younger of the two is assumed to be that person whose name comes first in
    alphabetical order (names will follow Python's capitalize case format).

    The input will have four lines. The first two lines correspond to the first person,
    while the last two lines correspond to the second person.
    For each person, the first line corresponds to the name and the second line
    corresponds to the date of birth in DD-MM-YYYY format.
    Your output should be the name of the younger of the two. """



an , ad , bn , bd = input() , input() , input() , input()
if (ad[6:11]) > (bd[6:11]):
    print(an)
elif (ad[6:11]) < (bd[6:11]):
    print(bn)
else:
    if (ad[3:5]) > (bd[3:5]):
        print(an)
    elif (ad[3:5]) < (bd[3:5]):
        print(bn)
    else:
        if (ad[0:2]) > (bd[0:2]):
            print(an)
        elif (ad[0:2]) < (bd[0:2]):
            print(bn)
        else:
            l = [an,bn]
            l.sort()
            print(l[0])