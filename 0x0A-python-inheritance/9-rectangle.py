#!/usr//bin/python3
"""TASK 9 Full Rectangle."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry:(7-base_geometry.py)."""

    def __init__(self, width, height):
        """Instantiate with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        """Width and height must be private. No getter or setter."""
        """Width and height must be positive integers."""
        """Validated by integer_validator."""
        self.__width = width
        self.__height = height

    def area(self):
        """Methods to find area of a rectangle."""
        width = self.__width
        height = self.__height
        return height * width

    def __str__(self):
        """Methods to describe a rectangle and its dimensions."""
        width = self.__width
        height = self.__height
        return "[Rectangle] {:d}/{:d}".format(width, height)
