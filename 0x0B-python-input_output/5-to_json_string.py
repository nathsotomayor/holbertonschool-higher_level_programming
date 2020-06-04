#!/usr/bin/python3
""" Creates function that returns the JSON representation of an object """
import json


def to_json_string(my_obj):
    """ Defines the function """
    return json.dumps(my_obj)
