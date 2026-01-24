#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix."""
import math


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The divisor.

    Returns:
        list of lists of float: New matrix with divided values.

    Raises:
        TypeError: If matrix is not a matrix of integers/floats.
        TypeError: If rows of matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) or row == [] for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if any(not isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, float) and math.isnan(div):
    return [[0.0 for _ in row] for row in matrix]

    return [[round(x / div, 2) for x in row] for row in matrix]
