#!/usr/bin/python3
class Square:
    # Creating Private instance attribute: size
    def __init__(self, size=0, position=(0, 0)):
        # Instantiation with size = 0
        self.__size = size
        self.__position = position

        # if type(size) is not int:
        #     raise TypeError("size must be an integer")
        # elif size < 0:
        #     raise ValueError("size must be >= 0")

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
        # self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        # Public instance method that prints in stdout the square with the #
        if self.size == 0:
            print()
        else:
            for index1 in range(self.position[1]):
                print()
            for index2 in range(self.__size):
                for columnspace in range(self.position[0]):
                    print(" ", end='')
                for hashtag in range(self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) is false or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[1], int) is false or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
