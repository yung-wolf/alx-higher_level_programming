#!/usr/bin/python3

"""
Module: '2-matrix_divided'
Has one function, matrix_divided()
"""


def matrix_divided(matrix, div):
    """A function to divide all elements of a matrix.

    Args:
        matrix (int/ floats): A list of lists
        div (int/ floats): Number to divide by
    """

    matrixErrMsg = 'matrix must be a matrix (list of lists) of integers/floats'

    # check if div is an int/float and is > 0
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    # check for empty matrix

    # check if each row in matrix is of the same size
    size_of_row = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != size_of_row:
            raise TypeError('Each row of the matrix must have the same size')

    # check if element in matrix is an int/float
    for list in matrix:
        for element in list:
            if not isinstance(element, int) or isinstance(element, float):
                raise TypeError(matrixErrMsg)

    x, i = 0, 0
    new_matrix = [row[:] for row in matrix]
    for list in new_matrix:
        for element in list:
            ans = element / div
            new_matrix[x][i] = round(ans, 2)
            i += 1
        i = 0
        x += 1

    return new_matrix
