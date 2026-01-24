#!/usr/bin/python3
"""Module that defines matrix_divided function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div and return a new matrix."""
    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) for row in matrix) or
            any(row == [] for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Handle NaN
    if isinstance(div, float) and div != div:
        return [[0.0 for _ in row] for row in matrix]

    # Handle +inf and -inf
    if isinstance(div, float) and div in (float("inf"), float("-inf")):
        return [[0.0 for _ in row] for row in matrix]

    new = []
    for row in matrix:
        new_row = []
        for x in row:
            value = round(x / div, 2)
            if value == 0:
                value = 0.0
            new_row.append(value)
        new.append(new_row)

    return new
