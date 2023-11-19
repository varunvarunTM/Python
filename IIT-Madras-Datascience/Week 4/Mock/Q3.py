""" Accept a square matrix A and an integer s as input and print the
    matrix s ⋅ A as output.
    Multiplying a matrix by an integer s is equivalent to multiplying
    each element of the matrix by s.
    For example: 
    
       2 x | 1  2 | = | 2  4 |
           | 3  4 |   | 6  8 |
    
    The first line of input is a positive integer, n, that denotes the
    dimension of the matrix A.
    Each of the next n lines contains a sequence of space-separated integers.
    The last line of the input contains the integer s.
    Print the matrix s ⋅ A as output.
    Each row of the matrix must be printed as a sequence of space
    separated integers, one row on each line.
    There should not be any space after the last number on each line.
    If the expected output looks exactly like the actual output and
    still you are getting a wrong answer,
    it is because of the space at the end. """


n = int(input())
matrix = []
for i in range(n):
      matrix.append([int(x) for x in input().split()])
s = int(input())
for i in range(n):
      for j in range(n):
            matrix[i][j] *= s
for i in range(n):
      for j in range(n):
            print(matrix[i][j], end="")
            if j < n - 1:
                  print(" ", end="")
      if i < n - 1:
            print()
            