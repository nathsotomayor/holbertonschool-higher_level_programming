#!/usr/bin/python3
""" Creates function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """ Defines the function """
    obj = json.loads(my_str)
    return obj
