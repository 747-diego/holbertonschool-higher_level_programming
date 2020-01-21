#!/usr//bin/python3
"""TASK 8 Rectangle."""


BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


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
