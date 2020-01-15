#!/usr/bin/python3
"""Write an empty class Rectangle that defines a rectangle."""


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
        """Property setter to set the value of height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        # setting value of height
        self.__height = value

    def area(self):
        """Public instance method that returns the rectangle perimeter."""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method that returns the rectangle perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """Str() should print the rectangle with the character #."""
        StrRep = ""
        if self.width == 0 or self.height == 0:
            return StrRep
        index1 = 0
        while index1 < self.height:
            StrRep = StrRep + ("#" * self.__width) + "\n"
            index1 += 1
        # return sting representattion of a rectangle
        return StrRep

    def __repr__(self):
        """Return a string representation of the rectangle.

        to recreate a new instance.
        """
        StringWidth = str(self.__width)
        StringHeight = str(self.__height)
        return "Rectangle(" + StringWidth + "," + StringHeight + ")"

    def __del__(self):
        """Return an instance of Rectangle when its deleted."""
        print("Bye rectangle...")
