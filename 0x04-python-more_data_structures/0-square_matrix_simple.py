#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = matrix.copy()
    for j in range(len(matrix)):
        matrix1[j] = list(map(lambda a: a**2, matrix[j]))
    return (matrix1)
