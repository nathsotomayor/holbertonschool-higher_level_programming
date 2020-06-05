#!/usr/bin/python3
""" Creates function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Defines function that divides elements of a matrix """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i, row in enumerate(matrix):
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not all([isinstance(j, (int, float)) for j in row]):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
    return [[round(i / div, 2) for i in row] for row in matrix]
