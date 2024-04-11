#!/usr/bin/python3
"""
This is the "matrix_divided"  module.

This module supplies one function, matrix_divided(),
which divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): Value to divide by.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    row_size = None

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg)

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(msg)

        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(msg)

        if row_size is None:
            row_size = len(i)
        elif row_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]
    return new_matrix
