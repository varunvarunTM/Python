# A sequence of five words is called magical if the "i" th word is a 
# substring of the "(i+1)" th word for every i in the range 1≤i<5 . 
# Accept a sequence of five words as input, one word on each line. 
# Print magical if the sequence is magical and non-magical otherwise.
# Note that str_1 is a substring of str_2 if and only if str_1 is 
# present as a sequence of consecutive characters in str_2.

str_1 = input()
str_2 = input()
str_3 = input()
str_4 = input()
str_5 = input()
a = str_1 in str_2
b = str_2 in str_2
c = str_3 in str_4
d = str_4 in str_5
if a and b and c and d == True:
    print("magical")
else:
    print("non-magical")