""" Accept two square matrices A and B of dimensions n x n as input and
    compute their product AB.

    The first line of the input will contain the integer n.
    This is followed by 2n lines.
    Out of these, each of the first n lines is a sequence of
    comma-separated integers that denotes one row of the matrix A.
    Each of the last n lines is a sequence of comma-separated integers that
    denotes one row of the matrix B.

    Your output should again be a sequence of n lines,
    where each line is a sequence of comma-separated integers that
    denotes a row of the matrix AB. """


n = int(input())
A = []
B = []
for i in range(n):
    A.append([int(x) for x in input().split(',')])
for i in range(n):
    B.append([int(x) for x in input().split(',')])
AB = []
for i in range(n):
    AB.append([])
    for j in range(n):
        AB[i].append(0)
        for k in range(n):
            AB[i][j] += A[i][k] * B[k][j]
for i in range(n):
    print(','.join([str(x) for x in AB[i]]))
    