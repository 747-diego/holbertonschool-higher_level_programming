#!/usr/bin/python3

"""

Write a function that prints a square with the character #.

Prototype: def print_square(size)

"""


def print_square(size):
    """

    Size is the size length of the square.

    size must be an integer, otherwise raise a TypeError

    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    hashtags = 0
    while hashtags < size:
        print("#" * size)
        hashtags += 1
