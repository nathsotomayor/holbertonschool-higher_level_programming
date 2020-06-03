#!/usr/bin/python3
""" Creates a class BaseGeometry """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Defining the class """
    def __init__(self, width, height):
        """ Define constructor """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
