#!/usr/bin/python3

""" 5. Printing a square """


class Square:
    """ The Square class """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @positon.setter
    def position(self, value):
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x > 0 for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for p1 in range(position[1]):
                print("")
            for p2 in range(position[0]):
                print(" ", end="")
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
