#!/usr/bin/python3
""" checks an instance of a class"""

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.
    Returns:
        True if obj is exactly an instance of cls; False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is a_class
