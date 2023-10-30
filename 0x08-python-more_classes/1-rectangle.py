#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Private instance attribute width"""
        return self.width

    @width.setter
    def width(self, value):
        """Private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width mush be >=0")
        self.__width = value

    @property
    def height(self):
        """Private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height mush be >=0")
        self.__height = value
