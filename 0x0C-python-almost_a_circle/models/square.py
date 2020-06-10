#!/usr/bin/python3
""" Creates a Square class inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defining Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing constructor """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Gets the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the size attribute """
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - "\
               "{}".format(self.id, self.x, self.y, self.size)
