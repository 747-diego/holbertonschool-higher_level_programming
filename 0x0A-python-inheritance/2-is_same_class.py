#!/usr/bin/python3
"""TASK 2  Exact same object."""


def is_same_class(obj, a_class):
    """Return True if object is exactly an instance; otherwise False."""
    return issubclass(a_class, type(obj))
