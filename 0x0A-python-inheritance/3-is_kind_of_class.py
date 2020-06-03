#!/usr/bin/python3
""" Creates a function that verify if an object is
instance of class or class that inherited from """


def is_kind_of_class(obj, a_class):
    """ Defining the function """
    if isinstance(obj, a_class):
        return True
    else:
        return False
