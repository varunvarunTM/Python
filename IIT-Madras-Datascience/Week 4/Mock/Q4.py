""" Accept two square matrices A and B of dimensions n x n as input and
    compute their sum A + B.

    The first line will contain the integer n. This is followed by 2n lines.
    Each of the first n lines is a sequence of comma-separated integers that
    denotes one row of the matrix A.
    Each of the last n lines is a sequence of comma-separated integers
    that denotes one row of the matrix B.

    Your output should again be a sequence of n lines,
    where each line is a sequence of comma-separated integer that denotes
    a row of the matrix A+B. """


n = int(input())
matrixA = []
matrixB = []
for i in range(n):
        matrixA.append([int(x) for x in input().split(",")])
for i in range(n):
        matrixB.append([int(x) for x in input().split(",")])
for i in range(n):
        for j in range(n):
                matrixA[i][j] += matrixB[i][j]
for i in range(n):
        for j in range(n):
                print(matrixA[i][j], end="")
                if j < n - 1:
                        print(",", end="")
        if i < n - 1:
                print()
                