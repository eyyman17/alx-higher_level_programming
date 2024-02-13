#!/usr/bin/python3

""" And now, the Square! """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ The Square Class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        Rectangle.width.fset(self, value)
        Rectangle.height.fset(self, value)

    def __str__(self):
        """ The Square _str method """
        str_return = (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
        return str_return

    def update(self, *args, **kwargs):
        """ Update Function """
        attributes = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key in list(kwargs.keys()):
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "size"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
