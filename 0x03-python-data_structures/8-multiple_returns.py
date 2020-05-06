#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence[0] = None
    len_tup = len(sentence)
    char_tup = sentence[0]
    return len_tup, char_tup;
