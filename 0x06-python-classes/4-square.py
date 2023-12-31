#!/usr/bin/python3
"""class Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Instantiation with size
        Args:
        size:  is crucial for a square
        """
        self.size = size

    @property
    def size(self):
        """ Private instance attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
