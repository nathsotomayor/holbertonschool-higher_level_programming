#!/usr/bin/python3
""" Creates a function that prints a text with two lines """


def text_indentation(text):
    """ Defines the function """
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = True
    for msg in text:
        if (line):
            if (msg == " "):
                continue
            else:
                line = False
        print(msg, end="")
        if msg in [".", ":", "?"]:
            print("", end="\n\n")
            line = True
