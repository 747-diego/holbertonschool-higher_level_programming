#!/usr/bin/python3
"""TASK 3 Write to a file."""


def append_write(filename="", text=""):
    """Write a function that appends a string to a text file."""
    """Returns the number of characters added."""
    if filename == "":
        return
    with open(filename, "a+") as file:
        file.write(text)
    return len(text)
