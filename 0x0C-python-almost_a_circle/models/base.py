#!/usr/bin/python3

""" BASE CLASS MODULE """

import json
import csv


class Base:
    """ the Base Class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string representation """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ From JSON string """
        if json_string is None or len(json_string) == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ CREATE """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                created = cls(1, 1)
            else:
                created = cls(1)
            created.update(**dictionary)
            return created
    @classmethod
    def save_to_file(cls, list_objs):
        """ Save list object to JSON """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON  string.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to file cvs """
        dict_list = []
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", encoding='utf-8') as f:
            if list_objs is None or len(list_objs) == 0:
                return
            write = csv.writer(f)
            write.writerow(list(vars(list_objs[0]).keys()))
            for obj in list_objs:
                write.writerow(list(obj.to_dictionary().values()))

    @classmethod
    def load_from_file_csv(cls):
        """ this """
        from pathlib import Path
        l_instance = []
        filename = cls.__name__ + ".csv"
        path = Path(filename)
        if not path.is_file():
            return l_instance
        else:
            with open(filename, encoding='utf-8', newline='') as f:
                reader = csv.reader(f)
                header = next(reader)
                rows = []
                for row in reader:
                    dict_rep = {key: value for key, value in zip(header, row)}
                    obj = cls.create(**dict_rep)
                    l_instance.append(obj)
        return l_instance
