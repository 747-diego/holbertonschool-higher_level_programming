#!/usr/bin/python3
"""POP is a function used to delete keys inside this dictionary"""


def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    return a_dictionary
