#!/usr/bin/python3
""" Creates function that creates an Object from a 'JSON file' """
import json


def load_from_json_file(filename):
    """ Defines the function """
    with open(filename, 'r', encoding='utf-8') as file_n:
        return json.load(file_n)
