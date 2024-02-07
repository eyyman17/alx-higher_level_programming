#!/usr/bin/python3

"""
Writing to a file module
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)"""
    with open(filename, 'w+', encoding='utf-8') as f:
        f.write(text)

    return (len(text))
