""" Write a function insert that accepts a sorted list L of integers
    and an integer x as input.
    The function should return a sorted list with the element x
    inserted at the right place in the input list.
    The original list should not be disturbed in the process.

         (1) The only built-in methods you are allowed to use are append
         and remove. You should not use any other method provided for lists.

         (2) You do not have to accept input from the user or print output
         to the console. You just have to write the function definition. """




def insert(L, x):
    """
    insert an element x into a sorted list L

    Arguments:
        L: list
        x: integers
    Return:
        sorted_L: list
    """
    result = L[:]  # Create a copy of the original list to avoid modifying it
    index = 0

    # Find the correct index to insert x
    while index < len(result) and result[index] < x:
        index += 1

    # Insert x at the correct index
    result.insert(index, x)

    return result