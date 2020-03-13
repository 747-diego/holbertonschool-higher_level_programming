#!/usr/bin/python3
"""TASK 7 Improved Geometry Module."""


class BaseGeometry:
    """Raise an implenmentation error: Area Exception."""

    def area(self):
        """Public instance."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance that validates value."""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
