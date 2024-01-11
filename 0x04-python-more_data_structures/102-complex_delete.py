#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    dic = dict(a_dictionary)
    for key in dic:
        if dic[key] == value:
            a_dictionary.pop(key)
    return a_dictionary
