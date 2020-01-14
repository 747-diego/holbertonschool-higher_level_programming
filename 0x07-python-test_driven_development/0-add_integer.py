#!/usr/bin/python3

"""

Integers addition.

Write a function that adds 2 integers

Returns an integer: the addition of a and b

"""


def add_integer(a, b=98):
    """

    Variables A and B must be integers or floats, otherwise raise a TypeError.

    exception with the message a must be an integer or b must be an integer

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
