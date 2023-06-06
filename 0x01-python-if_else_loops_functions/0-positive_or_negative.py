#!/usr/bin/python3
import random

number = random.randint(1, 100)

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

