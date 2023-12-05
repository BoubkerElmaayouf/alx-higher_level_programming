#!/usr/bin/python3
""" Class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ init new rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)

        def __str__(self):
            strg = "[" + str(self.__class__.name__) + "] "
            strg += str(self.width) + "/" + str(self.height)
            return strg

        def area(self):
            """ RETURNS THE AREA IF THE RECTANGE """
            return self.width * sekf.height

