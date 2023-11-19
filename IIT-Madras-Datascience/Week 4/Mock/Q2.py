""" An identity matrix is a square matrix which has ones on the main diagonal
    and zeros everywhere else.
    For example, the identity matrix of size 3 x 3 is:

            | 1  0  0 |
            | 0  1  0 |
            | 0  0  1 |
    

    Accept a positive integer n as input and print the identity
    matrix of size n x n.
    Your output should have n lines, where each line is a sequence of n 
    comma-separated integers that corresponds to one row of the matrix. """

n = int(input())
for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end="")
        else:
            print(0, end="")
        if j < n - 1:
            print(",", end="")
    print()
