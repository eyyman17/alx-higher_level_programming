#!/usr/bin/python3

"""  2-is_same_class Module """


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance of a class """
    if obj isinstance(a_class):
        return True
    else:
        return False
