""" Implement the following functions.

        (1) Write a function named get_column that accepts a matrix
        named mat and a non-negative integer named col as arguments.
        It should return the column that is at index col in the matrix
        mat as a list. Zero-based indexing is used here.

        (2) Write a function named get_row that accepts a matrix named
        mat and a non-negative integer named row as arguments.
        It should return the row that is at index row in the matrix
        mat as a list. Zero-based indexing is used here.

    You do not have to accept input from the user or print output to the
    console. You just have to write the definition of both the functions.
    Each test case will correspond to one function call. """




def get_column(mat, col):
    """
    extract a specific column from the matrix

    Arguments:
        mat: list of lists
        col: integer
    Return:
        col_list: list
    """
    column = []
    for row in mat:
        column.append(row[col])
    return column

def get_row(mat, row):
    """
    extract a specific row from the matrix
    
    Arguments:
        mat: list of lists
        row: integer
    Return:
        row_list: list
    """
    return mat[row]