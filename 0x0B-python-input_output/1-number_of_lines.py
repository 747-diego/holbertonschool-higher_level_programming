#!/usr/bin/python3
"""TASK 1 Number of Lines."""


def read_file(filename=""):
    """Read function that reads a text file (UTF8) and prints it to stdout."""
    if filename == "":
        pass
    NumberOfLines = 0
    with open(filename, "r") as file:
        for NumberOfLines in file:
            NumberOfLines += 1
    return NumberOfLines
