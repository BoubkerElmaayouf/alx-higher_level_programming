#!/usr/bin/python3
""" DECLARING A NEW CLASS """


class BaseGeometry:
    """ init a new class """

    def area(self):
        """ Raise an  Error """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != init:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
