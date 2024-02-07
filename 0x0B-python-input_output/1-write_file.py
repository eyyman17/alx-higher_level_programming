#!/usr/bin/python3

"""
Writing to a file module
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of characters"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
    except FileNotFoundError:
        with open(filename, 'w+', encoding='utf-8') as f:
            pass

    return (len(text))
