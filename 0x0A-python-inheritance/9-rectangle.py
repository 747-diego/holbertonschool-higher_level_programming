#!/usr//bin/python3
"""TASK 9 Rectangle."""


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
        """Area of Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Print String Representation."""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
