#!/usr/bin/python3

""" And now, the Square! """


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        super().__init__(x)
        super().__init__(y)
        self.__size = super().__init__(width)
        self.__size = super().__init__(height)

    def __str__:
        """ The Square _str method """
        str_return = (f"[Square] ({self.id}) {self.__x}/{self.__y} - \
{self.__size}")
        return str_return

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, width, height):
        self.setter_valid("size", value)
        self.__size = self.__width
        self.__size = self.__height
