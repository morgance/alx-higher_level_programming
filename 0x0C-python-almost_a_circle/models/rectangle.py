#!/usr/bin/python3
"""class rectangle, iheritance form class Base"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initalization of an instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super()__init__(id)

    @property
    def width(self):
        """width seeter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise TypeError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise TypeError("y must be > 0")
        self.__y = value 

    def area(self):
        """that returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ str special method """
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh

     def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returs a dictionary with properties """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
