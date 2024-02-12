#!/usr/bin/python3

""" My list Module """


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        """ print_sorted function """
        a = sorted(self)
        print(a)
