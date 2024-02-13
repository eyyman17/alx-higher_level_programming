#!/usr/bin/python3

""" First Rectangle Module """


from models.base import Base


class Rectangle(Base):
    """ The Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.setter_valid("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.setter_valid("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.setter_valid("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.setter_valid("y", value)
        self.__y = value

    def area(self):
        """ function that returns area of the triangle """
        return (self.width * self.height)

    @staticmethod
    def setter_valid(attribute, value):
        """ function that checks if attribute in the setter is valid """
        if type(value) is not int:
            raise TypeError(f"{attribute} must be an integer")
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError(f"{attribute} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attribute} must be > 0")
