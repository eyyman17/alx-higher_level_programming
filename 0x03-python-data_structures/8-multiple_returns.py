#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        first_char = None
    length = len(sentence)
    first_char = sentence[0]
    return (length, first_char)
