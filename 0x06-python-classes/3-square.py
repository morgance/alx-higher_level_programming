#!/usr/bin/python3
"""class with size and method of ares"""
class Square:


    """class that defines square by size"""
    def __init__(self, size=0):
        """ Method to contruct the square object"""
        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        elif size < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """returns the square are of the object"""
        return (self.__size ** 2)
