#!/usr/bin/python3
"""class Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Instantiation with size
        Args:
        size:  is crucial for a square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
