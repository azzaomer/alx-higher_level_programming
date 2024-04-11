#!/usr/bin/python3
"""Defines a function that prints a square with the character #.

Attributes: print_squer: function that prints my name.
"""
def print_square(size):
    """Print square

    Args:
    size: is the size length of the square "".

    Raises:
        TypeError: If size is not float or not is less than 0
        ValueError: If size is less than 0
        TypeError: If size is not integer
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and (size < 0):
        raise TypeError('size must be an integer')
    
    for i in range(size):
        print("#" * size)
