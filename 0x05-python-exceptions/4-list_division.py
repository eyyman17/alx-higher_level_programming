#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(list_length):
        try:
            r = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            r = 0
            print("division by 0")
        except TypeError:
            r = 0
            print("wrong type")
        except IndexError:
            r = 0
            print("out of range")
        finally:
            list.append(r)
    return list
