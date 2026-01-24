#!/usr/bin/python3
"""Module that defines matrix_divided function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div and return a new matrix."""
    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) or row == [] for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(not isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if isinstance(div, float) and div != div:
        return [[0.0 for _ in row] for row in matrix]
    if div == float("inf") or div == float("-inf"):
        return [[0.0 for _ in row] for row in matrix]

    new = []
    for row in matrix:
        new_row = []
        for x in row:
            v = round(x / div, 2)
            if v == 0:
                v = 0.0  # normalize -0.0 to 0.0
            new_row.append(v)
        new.append(new_row)
    return new
