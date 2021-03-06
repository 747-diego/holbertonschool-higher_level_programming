#!/usr/bin/python3
"""TASK 13 Student to disk and reload."""


class Student:
    """Write a class Student that defines a student by."""

    """Public instance attribute."""
    def __init__(self, first_name, last_name, age):
        """Instantiate Method."""
        """Currently Initializing First and Last name along with Age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation."""
        """"Of a Student instance."""
        ListOfAttrs = {}
        if attrs is None:
            return self.__dict__
        ListOfAttrs = {}
        for names in attrs:
            name = hasattr(self, names)
            if name:
                nameGrabbed = getattr(self, names)
                ListOfAttrs[names] = nameGrabbed
        return ListOfAttrs

    def reload_from_json(self, json):
        """Replace all attributes of the Student Instance."""
        for key, value in json.items():
            ReplacedAttr = self.__dict__.update(json)
