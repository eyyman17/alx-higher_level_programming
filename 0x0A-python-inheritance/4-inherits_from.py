#!/usr/bin/python3

""" Only sub class of """


def inherits_from(obj, a_class):
    """ inherits_from function """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
