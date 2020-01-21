#!/usr/bin/python3
"""TASK 4 Only sub class of."""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class.

    Inherited (directly or indirectly) from the specified class.

    otherwise return False.
    """
    return a_class is not type(obj) and isinstance(obj, a_class)
