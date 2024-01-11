#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = []
    j = 0
    for i in my_list:
        if i not in uniq_list:
            uniq_list.append(i)
            j += 1
    s = 0
    for i in uniq_list:
        s += i
    return s
