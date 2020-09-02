#!/usr/bin/python3


def remove_char_at(str, n):
    copy_str = str
    if n >= 0 and n <= len(str):
        copy_str = str[:n] + str[n + 1:]
    return(copy_str)
