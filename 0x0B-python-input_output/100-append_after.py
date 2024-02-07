#!/usr/bin/python3

"""
Append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after a specific string function
    """
    with open(filename, "r", encoding='utf-8') as f:
        all_lines = f.readlines()
        new_lines = []
        for line in all_lines:
            if line.find(search_string) != -1:
                new_lines.append(line)
                new_lines.append(new_string)
            else:
                new_lines.append(line)
    with open(filename, "w", encoding='utf-8') as f:
        f.writelines(new_lines)
