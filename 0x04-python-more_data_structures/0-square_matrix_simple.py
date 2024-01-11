#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    k = 0
    t = 0
    for i in matrix:
        for j in i:
            new_matrix[t][k] = j**2
            k += 1
        k = 0
        t += 1
    return new_matrix
