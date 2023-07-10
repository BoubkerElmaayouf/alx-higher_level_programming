#!/usr/bin/python3
"""Definding A Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New Class"""
    def __init__(self, size):
        """init a new class square
        Args:
            size (int)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
