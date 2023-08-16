#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''Function that computes the square va
    lues of all integers in a matrix. Return
    new matrix of same size.
    '''
    if not matrix:
        return None

    x = len(matrix)
    y = len(matrix[0])

    # copy of matrix
    new_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for row in range(x):
        for column in range(y):
            new_matrix[row][column] = matrix[row][column] ** 2

    return new_matrix
