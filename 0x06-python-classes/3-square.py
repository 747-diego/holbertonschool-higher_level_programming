#!/usr/bin/python3
class Square:
    # Creating Private instance attribute: size
    def __init__(self, size=0):
        # Instantiation with size = 0
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    # Public instance method: that returns the current square area
     def area(self):
         return self.__size ** 2
