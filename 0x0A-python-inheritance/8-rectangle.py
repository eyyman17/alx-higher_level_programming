#!/usr/bin/python3

""" Improve Geometry module """


class BaseGeometry:
    """ BASE GEOMETRY CLASS """
    def area(self):
        """ area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle Class """

    def __init__(self, width, height):
        """ instantiation function """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
