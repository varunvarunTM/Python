""" This question introduces you to the idea of suffix codes.
    Suffix code is a block of visible code that will be executed after
    whatever code you type. You have to type your code above the suffix code.
    Note that the contents of the suffix code cannot be modified.

    Accept a square matrix as input and store it in a variable named matrix.
    The first line of input will be, n, the number of rows in the matrix.
    Each of the next n lines will have a sequence of n space-separated integers.

    You do not have to print the output to the console as the suffix code
    already does that for you. """



n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
print(matrix) # suffix code
