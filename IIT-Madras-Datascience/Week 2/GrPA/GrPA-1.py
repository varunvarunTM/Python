""" Accept three positive integers as input and check if they form the sides of a right triangle.
    Print YES if they form one, and NO if they do not. The input will have three lines, with one integer on each line.
    The output should be a single line containing one of these two strings: YES or NO. """


a , b , c = int(input()) , int(input()) , int(input())
if ( a + b ) > c and ( a + c ) > b and ( b + c ) > a:
    print("YES")
else:
    print("NO")