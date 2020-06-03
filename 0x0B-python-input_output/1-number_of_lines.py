#!/usr/bin/python3
""" Creates that returns the number of lines of a text file """


def number_of_lines(filename=""):
    """ Defines the function """
    lines = 0
    f = open('my_file_0.txt', 'r', encoding='utf-8')
    with open('my_file_0.txt', 'r', encoding='utf-8') as file_n:
        lines = len(f.readlines())
    return lines

