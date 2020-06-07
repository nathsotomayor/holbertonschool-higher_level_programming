#!/usr/bin/python3
""" Creates class MyInt inherits from int that inverts == and != operators """


class MyInt(int):
    """ Defines class MyInt inherits from int """
    def __eq__(self, other):
        """ Invert the equal operator """
        return False

    def __ne__(self, other):
        """ Invert the negation operator """
        return True
