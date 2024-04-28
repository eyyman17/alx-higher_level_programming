#!/usr/bin/python3
""" Find a peak technical interview preparation """


def find_peak(list_of_integers):
    """ Function for finding the peak """

    if len(list_of_integers) == 0 or list_of_integers is None:
        return None
    if len(set(list_of_integers)) == 1:
        return list_of_integers[0]
    low = 0
    high = len(list_of_integers) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if list_of_integers[middle] > list_of_integers[middle - 1] and \
           list_of_integers[middle] > list_of_integers[middle + 1]:
            return list_of_integers[middle]
        elif list_of_integers[middle + 1] > list_of_integers[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return None
