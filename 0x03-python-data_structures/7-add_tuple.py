#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tempsum = [0, 0]
    for j in range(2):
        if j < len(tuple_a):
            tempsum[j] += tuple_a[j]
        if j < len(tuple_b):
            tempsum[j] += tuple_b[j]
    return tuple(tempsum)
