#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integer and/or float values.

    Args:
        a (int): First value
        b (int, optional): Second value. Defaults to 98.

    Raises:
        TypeError: If a and b are not integers or floats.

    Returns:
        int: Sum of a and b.
    """
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a+b
