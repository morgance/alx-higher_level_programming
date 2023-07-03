#!/usr/bin/python3
"""
Defines a rectangle with private instance attributes
width and height and public area and perimeter
"""


class Rectangle:
    """
    private attributes width and height
    Arguments:
        width
        height
        """
    def __init__(self, width=0, height=0):
        """Initializes the instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter, to return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter, to set width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter, to return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter, to set height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ return area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width + self.height) * 2)

    def __str__(self):
        """print the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(("#" * self.width for row in range(self.height)))
