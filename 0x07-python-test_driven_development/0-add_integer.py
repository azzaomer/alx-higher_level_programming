#!/usr/bin/python3
"""Defines a function add_integer(a, b=98) that adds two integers.

Attributes:
    add_integer: function that adds two integers.
"""

def add_integer(a, b=98):
    """Args: a, b
    Raises: TypeError: If a and b are not integers or floats.
    Returns: int: Sum of a and b."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a+b
