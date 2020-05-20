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

    def area(self):
        """ Return the square area """
        return self.__size ** 2

    @property
    def size(self):
        """ Return square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Update size attribute """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Prints the square with '#' """
        fig = self.__size
        if fig is 0:
            print()
        for i in range(fig):
            for j in range(fig):
                print("#", end="")
            print()
