#!/usr/bin/python3

""" BASE CLASS MODULE """


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

    @classmethod
    def save_to_file_cvs(cls, list_objs):
        """ save to file cvs """
        dict_list = []
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", encoding='utf-8') as f:
            if list_objs is None or len(list_objs) == 0:
                return
            write = cvs.writer(f)
            write.wrtierow(list(vars(list_objs[0]).keys()))
            for obj in list_objs:
                write.writerow(list(obj.to_dictionary().values()))

    @classmethod
    def load_from_file_csv(cls):
        """ load from file csv """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
