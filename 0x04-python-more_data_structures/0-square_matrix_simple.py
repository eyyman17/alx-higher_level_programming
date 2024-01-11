#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    k = 0
    l = 0
    for i in matrix:
        for j in i:
            new_matrix[l][k] = j**2
            k += 1
        k = 0
        l += 1
    return new_matrix
