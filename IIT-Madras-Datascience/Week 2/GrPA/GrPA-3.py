""" Accept a string as input and print the vowels present in the string in alphabetical order.
    If the string doesn't contain any vowels, then print the string "none" as output.
    Each vowel that appears in the input string — irrespective of its case — should appear
    just once in lower case in the output. """



s = input()
s = s.lower()
l = ""
if (s.find("a")) >= 0:
    l = l + "a"
if (s.find("e")) >= 0:
    l = l + "e"
if (s.find("i")) >= 0:
    l = l + "i"
if (s.find("o")) >= 0:
    l = l + "o"
if (s.find("u")) >= 0:
    l = l + "u"
if len(l) == 0:
    print("none")
else:
    print(l)