#!/usr/bin/python3
""" Creates a class Square """


class Square:
    """ Defining a Square class and one instance """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize instances of square class """
        if size is not int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """ Return square position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Update size attribute """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Prints the square with '#' """
        fig = self.__size
        spaces = self.__position
        if fig is 0:
            print()
        for unders in range(spaces[1]):
            print()
        for i in range(fig):
            for space in range(spaces[0]):
                print(" ", end="")
            for square in range(fig):
                print("#", end="")
            print()
