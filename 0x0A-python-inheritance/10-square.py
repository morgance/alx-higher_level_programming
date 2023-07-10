#!/usr/bin/python3
"""  class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines a Square from Rectangle class """
    def __init__(self, size):
        """ initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """returns a string with the area """
        return super().area()
