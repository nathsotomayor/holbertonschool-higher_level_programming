#!/usr/bin/python3
""" Creates function to read a file """


def read_file(filename=""):
    """ Defines the function """
    lines = 0
    with open('my_file_0.txt', 'r', encoding='utf-8') as file_n:
        for lines in file_n:
            print(lines, end="")
