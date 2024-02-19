#!/usr/bin/python3

""" MyInt Module"""


class MyInt(int):
    """ MyInt class """

    def __eq__(self, value):
        """ Overriding == opeartor with != """
        return self.real != value

    def __ne__(self, value):
        """ Overriding != operator with == """
        return self.real == value
