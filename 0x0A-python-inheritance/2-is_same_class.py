#!/usr/bin/python3
""" FUNCTION """


def is_same_class(obj, a_class):
    """ This function returns true if the objects is
    exactly an instance of the specified
    class , otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
