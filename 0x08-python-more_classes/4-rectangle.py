#!/usr/bin/python3
""" Creates A class that defines a Rectangle """


class Rectangle:
    """ Defines a class Rectangle """
    def __init__(self, width=0, height=0):
        """ Defines a init method for class Rectangle """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """ Return rectangle width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set value to rectangle width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Return rectangle height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set value to rectangle height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Public method that return rectangle area """
        width_side = self.__width
        height_side = self.__height
        rect_area = width_side * height_side
        return rect_area

    def perimeter(self):
        """ Public method that return rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            per = 0
        per = (2 * self.__width) + (2 * self.__height)
        return per

    def __str__(self):
        """ Prints rectangle """
        msg = ""
        if self.__width == 0 or self.__height == 0:
            return msg
        for i in range(self.__height):
            for j in range(self.__width):
                msg += "#"
            if i != self.__height - 1:
                msg += "\n"
        return msg

    def __repr__(self):
        """ Representation of the rectangle """
        rep_rect = "Rectangle({}, {})".format(self.__width, self.__height)
        return rep_rect
