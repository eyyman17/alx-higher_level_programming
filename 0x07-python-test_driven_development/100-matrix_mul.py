#!/usr/bin/python3

""" 6. Matrix multiplication module """


def matrix_mul(m_a, m_b):
    """ This is the matrix multplication function """

    # Raising Errors:

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(x, list) for x in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(x, list) for x in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for item in m_a:
        if not all(isinstance(x, (int, float)) for x in item):
            raise TypeError("m_a should contain only integers or floats")
    for item in m_b:
        if not all(isinstance(x, (int, float)) for x in item):
            raise TypeError("m_b should contain only integers or floats")
    m_a_length = 0
    for item in m_a:
        m_a_length += len(item)
    if m_a_length // len(m_a[0]) != len(m_a):
        raise TypeError("each row of m_a must be of the same size")
    m_b_length = 0
    for item in m_b:
        m_b_length += len(item)
    if m_b_length // len(m_b[0]) != len(m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication:

    new_matrix = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]
    return new_matrix
