#!/usr/bin/python3
"""TASK 3 Write to a file."""


def write_file(filename="", text=""):
    """Write a function that writes string to a text file."""
    """Returns the number of characters written."""
    if filename == "":
        return
    with open(filename, "w") as file:
        file.write(text)
    return len(text)
