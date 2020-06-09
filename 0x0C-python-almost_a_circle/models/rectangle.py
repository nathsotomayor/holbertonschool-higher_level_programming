#!/usr/bin/python3
""" Creates a Rectangle class inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ Defines Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing constructor """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Rectangle width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set value to rectangle width """
        self.__width = value

    @property
    def height(self):
        """ Rectangle height """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ Set value to rectangle height """
        self.__height = value

    @property
    def x(self):
        """ Rectangle 'x' attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set value to rectangle 'x' """
        self.__x = value
    
    @property
    def y(self):
        """ Rectangle 'y' attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set value to rectangle 'y' """
        self.__y = value
