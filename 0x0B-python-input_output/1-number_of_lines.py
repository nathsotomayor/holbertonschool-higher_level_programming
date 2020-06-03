#!/usr/bin/python3
""" Creates that returns the number of lines of a text file """


def number_of_lines(filename=""):
    """ Defines the function """
    lines = 0
    with open(filename, 'r', encoding='utf-8') as file_n:
        lines = len(file_n.readlines())
    return lines
