#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        sentence = None
    len_tup = len(sentence)
    char_tup = sentence[0]
    return len_tup, char_tup
