#!/usr/bin/python3

import sys

def main():
    length = len(sys.argv) - 1
    print("{} argument".format(length), end="")
    if length == 0:
        print("s.")
    else:
        if length > 1:
            print("s", end="")
        print(":")
        for i in range(1, length + 1):
            print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()
