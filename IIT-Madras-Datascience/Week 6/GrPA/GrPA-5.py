""" You are given a sequence of n points, ( x(i) , y(i) ) , 1 ≤ i ≤ n ,
    in the 2-D plane as input.
    Also, you are given a point P with coordinates ( x , y ).
    Print all points in the sequence that are nearest to P.
    If multiple points have the same least distance from P,
    print the points in the order of their appearance in the sequence.

    The first line of the input is an integer n, representing the number
    of points in the sequence.
    Each of the next n lines contains the co-ordinates of a point
    separated by comma.
    The last line contains the x and y co-ordinates of the point P.
    Assume that all the x and y co-ordinates are integers.

    The distance between two points ( x1 , y1 ) and ( x2 , y2 )
    is whole root of ( ( x1 - x2 ) ^ 2 + ( y1 - y2 ) ^ 2 ).
    You can assume that the maximum distance from P to any point
    will not exceed 1000. """



n = int(input())
points = []
for i in range(n):
    points.append([int(x) for x in input().split(',')])

p = [int(x) for x in input().split(',')]
distances = []
for i in range(n):
    distances.append(((points[i][0] - p[0]) ** 2 + (points[i][1] - p[1]) ** 2) ** 0.5)

min_dist = min(distances)
min_dist_indices = [i for i, dist in enumerate(distances) if dist == min_dist]

for index in min_dist_indices:
    print(f"{points[index][0]},{points[index][1]}")

