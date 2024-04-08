#!/usr/bin/python3
"""class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attributes:
        size: size of a square.
    """
    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size: size of the square.
        """
        self.__size = size

    def area(self):
        return self.__size ** 2

    @propert
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
