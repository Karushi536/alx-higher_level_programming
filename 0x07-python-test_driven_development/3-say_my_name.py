#!/usr/bin/python3
"""This module provides a function to print a person's name."""


def say_my_name(first_name, last_name=""):
    """
    Print a person's name.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person. Defaults to "".

    Returns:
        None

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
