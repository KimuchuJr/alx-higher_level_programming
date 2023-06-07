#!/usr/bin/python3

for b in range(122, 96, -1):
    ch = chr(b)
        if (b % 2 == 1):
            ch = chr(b - (ord('a') - ord('A')))
        print("{}".format(ch), end="")
