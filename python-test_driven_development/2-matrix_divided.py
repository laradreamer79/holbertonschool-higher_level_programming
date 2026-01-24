#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.
    
    Args:
        matrix: A list of lists containing integers or floats
        div: A number (integer or float) to divide by
        
    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places
        
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows have different sizes,
                   or if div is not a number
        ZeroDivisionError: If div is equal to 0
    """
    
    # Check if matrix is a list
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    
    # Check if all rows are lists
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
    
    # Check if matrix has at least one row and it's not empty
    if len(matrix) == 0 or (len(matrix) > 0 and len(matrix[0]) == 0):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    
    # Check first row to get expected size
    first_row_length = len(matrix[0])
    
    # Check all rows have same size and elements are numbers
    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError("matrix must have each row with the same size")
        
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create new matrix with divided values
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            # Divide and round to 2 decimal places
            result = round(element / div, 2)
            # Ensure it's a float with 2 decimal places
            new_row.append(float("{:.2f}".format(element / div)))
        new_matrix.append(new_row)
    
    return new_matrix
