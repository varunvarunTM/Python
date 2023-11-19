""" A sequence of integers of even length is said to be left-heavy if the
    sum of the terms in the left-half of the sequence is greater than the
    sum of the terms in the right half.
    It is termed right-heavy if the sum of the second half is greater than
    the first half.
    It is said to be balanced if both the sums are equal.

    Accept a sequence of comma-separated integers as input.
    Determine if the sequence is left-heavy, right-heavy or balanced and
    print this as the output. """

n = input().split(",")
l = len(n)
i = 0
sum1 = 0
while i < l//2:
    sum1 = sum1 + int(n[i])
    i+=1
j = l//2
sum2 = 0
while j < l:
    sum2 = sum2 + int(n[j])
    j+=1
if sum1 > sum2:
    print("left-heavy")
elif sum1 < sum2:
    print("right-heavy")
else:
    print("balanced")
