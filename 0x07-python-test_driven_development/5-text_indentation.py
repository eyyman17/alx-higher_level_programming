#!/usr/bin/python3

"""
4. Text indentation


"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    limit = len(text)
    i = 0
    if text[len(text) - 1] == ' ':
        limit -= 1
    if text[0] == ' ':
        i += 1
    while i < limit:
        if text[i] in ['.', '?', ':']:
            print(f"{text[i]}\n")
            if text[i + 1] == ' ':
                    i += 1
        else:
            print(text[i], end="")
        i += 1
