#!/usr/bin/python3
"""Class Square with size, method of area and getters & setters"""


class Square:

    """class that defines a square by size"""
    def __init__(self, size=0):
        """constructor for the square object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """returns the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size value of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
