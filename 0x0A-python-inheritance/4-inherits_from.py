#!/usr/bin/python3
""" Creates a function that verify if an object is
instance of class or class that inherited from """


def inherits_from(obj, a_class):
    """ Defining the function """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
