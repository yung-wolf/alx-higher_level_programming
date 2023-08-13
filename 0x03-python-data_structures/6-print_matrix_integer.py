#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    '''Function to print a matrix of integers
    '''

    try:
        # find len of 1st matrix
        idx = (len(matrix[0]) - 1)

        if idx == -1:
            print()

        for i in matrix:
            count = 0
            for x in i:
                if count != idx:  # check for last element of matrix
                    print("{:d}".format(x), end=" ")
                else:
                    print("{:d}".format(x))
                count += 1
    except TypeError:
        print()
