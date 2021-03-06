#!/usr/bin/python3
""" Creates a class Rectangle based on BaseGeometry """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Defining the class """
    def __init__(self, size):
        """ Define constructor """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Defines area method that calc the area with size attribute """
        return (self.__size * self.__size)

    def __str__(self):
        """ Prints rectangle description """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
