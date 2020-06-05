#!/usr/bin/python3
""" Creates a function that prints a square with the character '#' """


def print_square(size):
    """ Defines the function """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for x in range(size):
        for x in range(size):
            print("#", end='')
        print()
