#!/usr/bin/python3
""" FUNCTION TO CHECK """


def is_kind_of_class(obj, a_class):
    """ This function returns True if the object
    is an instance of, or if the object is an instance
    of a class that inherited from, the specified class
    otherwize false
    Args:
    ogj : to be checked
    a_class: the class
    """
    if isinstance(obj, a_class):
        return True
    return False
