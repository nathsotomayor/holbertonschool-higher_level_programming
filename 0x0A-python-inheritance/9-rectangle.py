#!/usr/bin/python3
""" Creates a class Rectangle based on BaseGeometry """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Defining the class """
    def __init__(self, width, height):
        """ Define constructor """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Defines area method that calc the area of a rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ Prints rectangle description """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
