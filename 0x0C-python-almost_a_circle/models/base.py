#!/usr/bin/python3
""" Creates a Base class that is the base of all other classes """
import json


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

    def to_json_string(list_dictionaries):
        """ JSON string representation of dictionaries """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
