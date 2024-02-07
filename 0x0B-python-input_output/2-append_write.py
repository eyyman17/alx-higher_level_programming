#!/usr/bin/python3

"""
Appending to a file module
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8)
    """
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
