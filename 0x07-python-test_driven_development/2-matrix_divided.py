#!/usr/bin/python3

"""
1. Divide a matrix


"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix. """

    if not all(isinstance(item, (int, float)) for item in matrix) and not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for item in matrix:
        row = []
        for element in item:
            row.append(round(element\div, 2))
        new_matrix.append(row)
    return new_matrix
