#!/usr/bin/python3

"""
7. Lazy matrix multiplication
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ Matrix multiplication using Numpy """

    new_matrix = np.matmul(m_a, m_b)
    return new_matrix
