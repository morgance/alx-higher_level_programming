#!/usr/bin/python3
"""Create class with size"""

class Square:
    """class that defines square by size"""
    def __init__(self, size=0):
        """ Method to construct the square object"""
        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        elif size < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = int(size)
