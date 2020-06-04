#!/usr/bin/python3
""" Creates function that appends a string to a file """


def append_write(filename="", text=""):
    """ Defines the function """
    with open(filename, mode='a', encoding='utf-8') as file_n:
        file_n = file_n.write(text)
        return file_n
