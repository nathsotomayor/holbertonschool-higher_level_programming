#!/usr/bin/python3
""" Creates a class Square """


class Square:
    """ Defining a Square class and one instance """
    def __init__(self, size=0):
        """ Initialize instance size of square class """
        if size is not int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
