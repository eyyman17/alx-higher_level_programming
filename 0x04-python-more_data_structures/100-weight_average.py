#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = 0
    denominator = 0
    for value in my_list:
        numerator += value[0] * value[1]
        denominator += value[1]
    result = numerator / denominator
    return result
