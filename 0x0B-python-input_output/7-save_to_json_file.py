#!/usr/bin/python3
""" Creates function that writes an Object to a text file, using a JSON
representation """
import json


def save_to_json_file(my_obj, filename):
    """ Defines the function """
    with open(filename, 'w', encoding='utf-8') as file_n:
        return json.dump(my_obj, file_n)
