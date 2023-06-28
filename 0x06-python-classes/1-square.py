#!/usr/bin/python3

"""
    Subtopic on OOP, task 2 where the requirements are defining
    a square that defines itself using private instance attributes and 
    instatiation with size
"""


class Square:
    """ A Square class """
    def __init__(self, size):
        """ Initialize square with size
        Args:
            __size: size of the square
        """
        self.__size = size
