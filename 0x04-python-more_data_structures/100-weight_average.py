#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == []:
        return 0
    num = den = 0
    for tpl in my_list:
        a, b = tpl
        num += (a * b)
        den += b
    return num / den
