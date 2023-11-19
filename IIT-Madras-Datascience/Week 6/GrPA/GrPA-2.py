""" You are given a list marks that has the marks scored by a class of
    students in a Mathematics test.
    Find the median marks and store it in a float variable named median.
    You can assume that marks is a list of float values.

    Procedure to find the median

        (1) Sort the marks in ascending order.
        Do not try to use built-in methods.
        Look at the lecture 4.5 of week-4 to get a better idea.

        (2) If the number of students is odd,
        then the median is the middle value in the sorted sequence.
        If the number of students is even, then the median is the
        arithmetic mean of the two middle values in the sorted sequence.

    You do not have to accept input from the console as it has already
    been provided to you.
    You do not have to print the output to the console.
    Input-Output is the responsibility of the autograder for this problem.
    Refer to PPA-11 if you are not sure how this works. """



n = len(marks)
for i in range(n):
    for j in range(n - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

# Calculate the median
median = 0.0
if n % 2 == 0:
    mid1 = n // 2
    mid2 = mid1 - 1
    median = (marks[mid1] + marks[mid2]) / 2
else:
    mid = n // 2
    median = marks[mid]

