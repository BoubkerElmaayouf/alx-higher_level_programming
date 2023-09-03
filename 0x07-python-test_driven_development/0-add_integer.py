#!/usr/bin/python3
def add_integer(a, b=98):
    """
    this is a function to add two  numbers

    Return a + b

    a and b must be integers or floats

    Raises:
        TypeError: if they are not float or integers
    """
    if((not isinstance(a,int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if((not isinstance(b,int) and not isinstance(b,float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
