"""
    L is a list of real numbers that is already given to you.
    You have to sort this list in descending order and store the sorted
    list in a variable called sorted_L.
"""


L = [1.1, 2.2, 3.3]  # Given list

def solution(L):
    sorted_L = sorted(L, reverse=True)
    return sorted_L

print(solution(L))