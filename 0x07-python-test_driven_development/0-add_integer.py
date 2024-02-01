#!/usr/bin/python3

"""
0. Integers addition


"""


def add_integer(a, b=98):
    """
    a function that adds 2 integers.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
