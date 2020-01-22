#!/usr/bin/python3
"""TASK 10 Class to JSON."""


def class_to_json(obj):
    """Write a function that returns the dictionary description."""
    """With data structure (list, dictionary, string, integer and boolean)."""
    """For JSON serialization of an object."""
    return vars(obj)
