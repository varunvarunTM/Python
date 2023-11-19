""" A data entry operator has a faulty keyboard.
    The keys 0 and 1 are very unreliable.
    Sometimes they work, sometimes they don't.
    While entering phone numbers into a database, the operator uses the letter
    'l' as a replacement for 1 and 'o' as a replacement for 0 whenever these
    binary digits let him down. Both 'l' and 'o' are in lower case.
    'l' is the first letter of the word 'land', and not capital 'i'.

    Accept a ten-digit number as input.
    Find the number of places where the numbers 0 and 1 have been replaced
    by letters. If there are no such replacements,
    print the string No mistakes.
    If not, print the number of mistakes (replacements) and in the next line,
    print the correct phone number. """


n = input()
l = n.count("l")
o = n.count("o")
if l > 0 or o > 0:
    print(l + o , "mistakes")
    print(n.replace("l", "1").replace("o", "0"))
else:
    print("No mistakes")

