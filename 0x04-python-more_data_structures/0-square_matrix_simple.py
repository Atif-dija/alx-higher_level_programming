#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = matrix.copy()
    for j in range(len(matrix)):
        matrix1[j] = list(map(lambda x: x**2, matrix[i]))
    return (matrix1)
