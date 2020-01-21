#!/usr/bin/python3
class Square:
    # Creating Private instance attribute: size
    def __init__(self, size=0):
        # Instantiation with size = 0
        self.__size = size
        if type(size) is not int:
            # if instance(size, int) is False = if both dont match then raise an error
            # instance comapares a variable and a data type if they match
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
