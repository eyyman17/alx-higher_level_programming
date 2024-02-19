#!/usr/bin/python3

""" 
Exact same object Module
"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance of a class """
    if obj isinstance(a_class):
        return True
    else:
        return False
