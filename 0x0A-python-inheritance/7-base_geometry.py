#!/usr/bin/python3
""" Creates a class BaseGeometry """


class BaseGeometry:
    """ Defining the class """
    def area(self):
        """ Defines area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Defines method that validate an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
