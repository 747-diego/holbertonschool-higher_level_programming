#!/usr/bin/python3
"""TASK 0 Read file."""


def read_file(filename=""):
    """Read function that reads a text file (UTF8) and prints it to stdout."""
    if filename == "":
        pass
    with open(filename, "r") as file:
        text = file.read()
        print(text, end="")
