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
        str_return = (f"[Square] ({self.id}) {self.__x}/{self.__y} - \
{self.__size}")
        return str_return
