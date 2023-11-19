""" In the first line of input, accept a sequence of space-separated words.
    In the second line of input, accept a single word.
    If this word is not present in the sequence, print NO.
    If this word is present in the sequence,
    then print YES and in the next line of the output,
    print the number of times the word appears in the sequence. """



s = input().split()
w = input()
if w in s:
    print('YES')
    print(s.count(w))
else:
    print('NO')
