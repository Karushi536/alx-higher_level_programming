#!/usr/bin/python3
"""Defines a square."""


class Square:
    """A class defining a square."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Note:
            The size attribute is a private instance attribute,
            denoted by the use of double underscores.
        """
        self.__size = size
