#!/usr/bin/python3


def uppercase(str):
    for cha in str:
        temp = cha
        if ord(cha) >= 97 and ord(cha) <= 122:
            temp = chr(ord(cha) - (ord('a') - ord('A')))
            print("{}".format(temp), end="")
        print()
