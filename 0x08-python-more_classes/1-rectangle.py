#!/usr/bin/python3
"""

Simple rectangle.

Write an empty class Rectangle that defines a rectangle:

"""


class Rectangle:
    """Class on Rectangles."""

    def __init__(self, width=0, height=0):
        """Instantiate with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """

        Getter to retrieve width.

        returns as private
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter to set the value of width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        # setting value of width
        self.__width = value

    @property
    def height(self):
        """

        Getter to retrieve height.

        Returns as private
        """
        return self.__height

        @height.setter
        def height(self, value):
            """Property setter to set the value of width."""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
