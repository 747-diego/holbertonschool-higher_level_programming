#!/usr/bin/python3
class Square:
    # Creating Private instance attribute: size
    def __init__(self, size=0):
        # Instantiation with size = 0
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must ne >= 0")
