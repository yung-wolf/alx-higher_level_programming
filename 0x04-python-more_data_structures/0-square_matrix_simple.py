#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''Function that computes the square va
    lues of all integers in a matrix. Return
    new matrix of same size.
    '''

    # if empty matrix
    if not matrix:
        return None

    x = [0, 1, 2]

    # copy of matrix
    new_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for row in x:
        for column in x:
           new_matrix[row][column] = matrix[row][column] **2

    return new_matrix 
