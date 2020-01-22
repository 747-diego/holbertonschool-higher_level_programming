#!/usr/bin/python3
"""TASK 8 Create object from a JSON file."""
import json


def load_from_json_file(filename):
    """Write a function that creates an Object from a “JSON file”."""
    if filename == "":
        pass
    with open(filename, "r") as file:
        SavedFile = json.load(file)
        return SavedFile
