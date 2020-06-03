#!/usr/bin/python3
""" Creates a function that verify if an object is equal to class """


def is_same_class(obj, a_class):
    """ Defining the function """
    if type(obj) == a_class:
        return True
    else:
        return False
