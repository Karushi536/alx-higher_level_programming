#!/usr/bin/python3
"""This module provides a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix (list of list of int or float): The matrix to be divided.
        div (int or float): The number to divide each element of the matrix by.

    Returns:
        list of list of float: A new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   if each row of the matrix does not have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.

    """
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div, rounded to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)

    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
