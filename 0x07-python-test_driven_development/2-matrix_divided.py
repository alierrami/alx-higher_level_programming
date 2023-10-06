#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (matrix == [] or matrix == [[]] or
        type(matrix) is not list or
            not all(type(row) is list for row in matrix)):
        raise TypeError(error_msg)
    for row in matrix:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
