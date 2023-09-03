#!/uer/bin/python3
""" Define a function that say my first and last name"""

def say_my_name(first_name, last_name=""):
    """
    Say this first and last name

    Args:
        first and last names

    Raises:
        TypeError: if the last and first
                    name is not string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("my name is {} {}".format(first_name, last_name))
