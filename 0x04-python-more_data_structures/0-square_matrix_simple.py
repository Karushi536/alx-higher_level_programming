#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the squre value of all integers in a matrix."""
    new_matrix = [list(map(lambda x: x**2, row)) for row in matrix]
    return new_matrix
