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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string representation of dictionaries """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string representation to a file """
        json_file = "{}.json".format(cls.__name__)
        if list_objs is None:
            new_dict = []
        else:
            new_dict = [item.to_dictionary() for item in list_objs]
        with open(json_file, 'w', encoding='utf-8') as json_file:
            json_file.write(cls.to_json_string(new_dict))