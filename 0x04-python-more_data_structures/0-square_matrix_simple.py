#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_pow = [i[:] for i in matrix]
    for i in range(0, len(matrix)):    
        for j in range(0, len(matrix[i])):
            matrix_pow[i][j] = matrix[i][j] ** 2
    return matrix_pow
