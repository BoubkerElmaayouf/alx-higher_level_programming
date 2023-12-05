#!/usr/bin/python3
""" DECLARING A CLASS """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ INITIALIZING CLASS Rectange """

    def __init__(self, width, height):
        """ init new rectangle,
        ARGS:
        width and hieght
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
