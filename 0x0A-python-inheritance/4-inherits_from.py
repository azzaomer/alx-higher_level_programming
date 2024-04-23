#!/usr/bin/python3
"""Contains a single function"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.

    Returns:
        True if obj is an instance of a subclass of cls; False otherwise.
    """
    return ((issubclass(type(obj), a_class)) and type(obj) != a_class)
