#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, diff, prod, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, diff(a, b)))
    print("{} * {} = {}".format(a, b, prod(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
