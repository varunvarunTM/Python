#  (Q) You are given a string and two non-negative integers as input. 
#  The two integers specify the start and end indices of a substring
#  in the given string.Create a new string by replicating the substringa minimum
#  number of times so that the resulting string is longer than the input string.
#  The input parameters are the string, start index of the substring and the end
#  index of substring (endpoints inclusive) each on a different line.

#First Method

string = input()
int1 = int(input())
int2 = int(input()) + 1
m = (len(string[int1:int2]))
n = m
while len(string) > n:
   n = n + m
   if n > len(string):
      a = n//m
      print(string[int1:int2]*a)
   if n == len(string):
      a = n//m + 1
      print(string[int1:int2]*a)


#Second Method

string = input()
int1 = int(input())
int2 = int(input()) + 1
y = string[int1:int2]
x = ""
while len(string) >= len(x):
   x = x + y
   if len(x) > len(string):
      print(x)


