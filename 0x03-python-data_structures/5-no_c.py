#!/usr/bin/python3


def no_c(my_string):
    string = list(my_string)
    new_str = ''
    for a in range(len(string)):
        if string[a].upper() == 'C':
            string[a] = ''
        new_str += string[a]
    return new_str
