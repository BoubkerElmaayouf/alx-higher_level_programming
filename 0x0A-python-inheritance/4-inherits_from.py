#!/usr/bin/python3
""" Function  to check """


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an
    instance of a class that inherited (directly or indeirectly)
    from the specified class, otherwize False
    """
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
