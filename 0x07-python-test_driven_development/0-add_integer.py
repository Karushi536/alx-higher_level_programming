#!/usr/bin/python3
"""This module provides a function to add two integers."""


def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float. Defaults to 98.

    Returns:
        int: The addition of a and b as integers.

    Raises:
        TypeError: If a or b are not integers or floats.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
