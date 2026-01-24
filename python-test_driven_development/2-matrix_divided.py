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
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    
    # Check if matrix is empty
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    
    # Check if matrix contains only lists
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
    
    # Check if matrix is not empty and first row exists
    if len(matrix) > 0 and len(matrix[0]) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    
    # Check all rows have the same size
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        
        # Check all elements in each row are integers or floats
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
            new_row.append(result)
        new_matrix.append(new_row)
    
    return new_matrix
