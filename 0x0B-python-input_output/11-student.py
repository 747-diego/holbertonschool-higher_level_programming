#!/usr/bin/python3
"""TASK 11 Student to JSON."""


class Student:
    """Write a class Student that defines a student by."""

    """Public instance attribute."""
    def __init__(self, first_name, last_name, age):
        """Instantiate Method."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retrieves a dictionary representation."""
        """"Of a Student instance."""
        return vars(self)
