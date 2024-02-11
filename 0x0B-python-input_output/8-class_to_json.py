#!/usr/bin/python3

""" Class to JSON Module """


def class_to_json(obj):
    """ function that returns the dict description with data for JSON """
    return obj.__dict__
