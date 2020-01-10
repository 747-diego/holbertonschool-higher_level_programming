#!/usr/bin/python3
class Square:
    # Creating Private instance attribute: size
    def __init__(self, size=0):
        # Instantiation with size = 0
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        # Public instance method: that returns the current square area
        return self.__size ** 2

    @property
    def size(self):
        # property to retrieve it
        return self.__size

    @size.setter
    def size(self, value):
        # property setter to set it
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        # Public instance method that prints in stdout the square with the #
        if self.size == 0:
            print()
        SquareSize = self.size
        for index1 in range(SquareSize):
            for index2 in range(SquareSize):
                print('#', end='')
            print()
