#!/usr/bin/python3
"""class that defines a Rectangle"""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance

        Arguments:
            width: rectangle width
            height: rectangle height
            """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns the value of the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width

        Argument:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
            """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height

        Returns:
            rectangle height


        """

        return self.__height

    @height.setter
    def height(self, value):
        """defines the height

        Argument:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
            """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates the Rectangle area"""

        return self.width * self.height

    def perimeter(self):
        """ calculates the Rectangle perimeter"""

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ Method that returns the Rectangle #"""

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """returns the string represantion of the instance"""

        return "Rectangle({:d}, {:d})".format(self.width, self.height)
