#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = matrix.copy()
    new_matrix = []
    for i in matrix_copy:
        new_max = [
            i[0]*i[0],
            i[1]*i[1],
            i[2]*i[2]
        ]
        new_matrix.append(new_max)

    return new_matrix
