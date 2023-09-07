#!/usr/bin/python3

""" Define a function that says my first and last name"""


def say_my_name(first_name, last_name=""):
    """
    Say this first and last name

    Args:
        first_name: First name
        last_name: Last name (optional)

    Raises:
        TypeError: if first_name or last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
