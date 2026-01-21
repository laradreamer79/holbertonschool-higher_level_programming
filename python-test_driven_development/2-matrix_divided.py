#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div."""

    # Validate matrix
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = None
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if (not isinstance(element, (int, float))
                    or isinstance(element, bool)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Validate div
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = round(element / div, 2)
            if result == 0:
                result = 0.0
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
