#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list == []:
        return None
    big = my_list[0]
    for a in range(1, len(my_list)):
        if my_list[a] > big:
            big = my_list[a]
    return big
