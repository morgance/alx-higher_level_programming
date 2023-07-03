#!/usr/bin/python3
"""class that defines a Rectangle"""


class Rectangle:
    """ Class that defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializes the instance"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the value of the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """defines the width

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
        """ returns the value of the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """ defines the height

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
        """calculates the Rectangle area"""

        return self.width * self.height

    def perimeter(self):
        """calculates the Rectangle perimeter"""

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ returns the Rectangle #"""

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += (str(self.print_symbol) * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """returns the string represantion of the instance"""

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ prints a message when the instance is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger Rectangle

        Arguments:
            rect_1: Rectangle 1
            rect_2: Rectangle 2

        Raises:
            TypeError: when some argument passed is not
            an instance of the Rectangle class

        Returns:
            The bigger Rectangle
            """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new instance of Rectangle class

        Arguments:
            cls: rectangle class
            size: rectangle width and rectangle height

        Returns:
            a new instance of Rectangle class
            """

        return cls(size, size)
