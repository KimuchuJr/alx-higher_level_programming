#!/usr/bin/python3


def uppercase(str):
    for sy in str:
        temp = sy
                if ord(sy) >= 97 and ord(sy) <= 122:
                    temp = chr(ord(sy) - (ord('a') - ord('A')))
                print("{}".format(temp), end="")
        print()
