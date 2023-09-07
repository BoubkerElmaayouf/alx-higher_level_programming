#!/usr/bin/python3
""" Define print_square function"""


def print_square(size):
    """
    print a square by # sign and the size is the len of the square

    Args
        size: the len of the square

    Raises:
        TypeError: if size is not an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
