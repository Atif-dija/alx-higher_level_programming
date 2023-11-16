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
        return self.__width

    @width.setter
    def width(self, value):
        """Private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """primeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """print the rectangle with the character #"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for i in range(self.__height))
        return string

    def __repr__(self):
        """return a string representation of the rectangle """
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
