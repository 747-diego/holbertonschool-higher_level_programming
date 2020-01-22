#!/usr/bin/python3
"""TASK 1 Number of Lines."""


def number_of_lines(filename=""):
    """Line Number function that returns the number of lines of a text file."""
    if filename is "":
        pass
    NumberOfLines = 0
    with open(filename, "r") as file:
        for Lines in file:
            NumberOfLines += 1
    return NumberOfLines
