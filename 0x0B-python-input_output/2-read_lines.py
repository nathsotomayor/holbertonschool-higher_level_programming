#!/usr/bin/python3
""" Creates that prints n lines of a text file """


def read_lines(filename="", nb_lines=0):
    """ Defines the function """
    with open(filename, 'r', encoding='utf-8') as file_n:
        list_lines = file_n.readlines()
        num_lines = len(list_lines)
        for i, lines in enumerate(list_lines):
            if nb_lines <= 0 or nb_lines >= num_lines:
                print(lines, end="")
            elif i < nb_lines:
                print(lines, end="")
