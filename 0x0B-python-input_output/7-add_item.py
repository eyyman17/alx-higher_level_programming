#!/usr/bin/python3
import json

"""
Load, add, save module
"""


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON """
    with open(filename, 'w+') as f:
        f.write(json.dumps(my_obj))


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename, 'r') as f:
        return json.loads(f.read())


def main():
    """ The main function """
    path = Path("./add_item.json")
    if path.is_file():
        p_list = load_from_json_file("add_item.json")
        if type(p_list) is not list:
            save_to_json_file([], "add_item.json")
            p_list = load_from_json_file("add_item.json")
    else:
        save_to_json_file([], "add_item.json")
    p_list = load_from_json_file("add_item.json")
    for i in range(1, len(sys.argv)):
        p_list.append(sys.argv[i])
        save_to_json_file(p_list, "add_item.json")


main()
