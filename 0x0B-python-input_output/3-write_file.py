#!/usr/bin/python3
""" Creates function to write to a file """


def write_file(filename="", text=""):
    """ Defines the function """
    with open(filename, mode='w', encoding='utf-8') as file_n:
        file_n = file_n.write(text)
        return file_n
