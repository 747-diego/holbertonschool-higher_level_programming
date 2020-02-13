#!/usr/bin/python3
"""TASK 12 Student to JSON with Filter."""


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
        if type(attrs) is list:
            for index in range(len(attrs)):
                if type(attrs[index]) is not str:
                    return vars(self)
        else:
            for attribute, value in vars(self).items():
                if type(attrs) is list:
                    for index in attrs:
                        if index is attribute:
                            ListOfAttrs[attribute] = value
        return vars(self)
