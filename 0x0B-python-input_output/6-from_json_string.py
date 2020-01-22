#!/usr/bin/python3
"""TASK 6 From JSON string to Object."""

import json


def from_json_string(my_str):
    """Write a function that returns the JSON representation of an object."""
    """(Python data structure) represented by a JSON string."""
    return json.loads(my_str)
