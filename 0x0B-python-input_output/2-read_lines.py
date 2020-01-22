#!/usr/bin/python3
"""TASK 2 Read n Lines."""


def read_lines(filename="", nb_lines=0):
    """Line Number function that reads n lines of text file."""
    if filename is "":
        pass
    NumberOfLines = 0
    with open(filename, "r") as file:
        for lines in file:
            if nb_lines <= 0:
                print(lines, end="")
                NumberOfLines += 1
            elif NumberOfLines < nb_lines:
                print(lines, end="")
                NumberOfLines += 1
            else:
                pass
