#!/usr/bin/bash
""" Creates a Base class that is the base of all other classes """


class Base:
    """ Initializing Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    