#!/usr/bin/python3


def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 or a % 5 == 0:
            if a % 3 == 0:
                print("{}".format("Fizz"), end="")
            if a % 5 == 0:
                print("{}".format("Buzz"), end="")
            else:
                print("{}".format(a), end="")
                print(" ", end="")
