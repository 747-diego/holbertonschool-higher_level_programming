#!/usr/bin/python3
"""TASK 6 From JSON string to Object."""

import json


def save_to_json_file(my_obj, filename):
    """Write a function that writes an Object to a text file."""
    """Using a JSON representation."""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
