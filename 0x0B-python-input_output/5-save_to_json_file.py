#!/usr/bin/python3

"""
Save Object to file
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON """
    with open(filename, 'w+') as f:
        f.write(json.dumps(my_obj))
