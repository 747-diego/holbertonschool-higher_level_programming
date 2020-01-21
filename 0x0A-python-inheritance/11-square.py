#!/usr/bin/python3
"""TASK 11 Square #2."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from BaseGeometry:(9-rectangle.py)."""

    def __init__(self, size):
        """Size must be private. No getter or setter."""
        """Size must be a positive integer, validated by integer_validator."""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Methods to describe a square and its dimensions."""
        size = self.__size
        return "[Square] {:d}/{:d}".format(size, size)
