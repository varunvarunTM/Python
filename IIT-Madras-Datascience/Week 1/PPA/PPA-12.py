""" You are given a string and two non-negative integers as input.
   The two integers specify the start and end indices of a substring in the given string.
   Create a new string by replicating the substring a minimum number of times so that the resulting string is longer than the input string.
   The input parameters are the string, start index of the substring and the end index of substring (endpoints inclusive) each on a
   different line. """



string = input()
int1 = int(input())
int2 = int(input()) + 1
y = string[int1:int2]
x = ""
while len(string) >= len(x):
   x = x + y
   if len(x) > len(string):
      print(x)