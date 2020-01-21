#!/usr/bin/python3
"""TASK 13 Can I?."""


def add_attribute(obj=None, key="", value=""):
    """Write a function that adds a new attribute to an object."""
    """If it’s possible."""
    try:
        obj.__setattr__(key, value)
    except Exception:
        raise TypeError("can't add new attribute")
