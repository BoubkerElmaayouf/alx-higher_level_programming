#!/usr/bin/python3
""" The Rectangle class """


class Rectangle:
    """ Defining Rectangle class """

    def __init__(self, width=0, height=0):
        """ Start a new Retangle
        args:
        width: intiger
        height: intiger
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get The width Value """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get height Value """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set The Value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the are of the retangle"""
        return (self.__width * self.__height)

    def perimetTher(self):
        """Return the perimeter of the retangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the retangle
        Represent the retangle with #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []
        for i in range(self.__height):
            [r.append('#') for n in range(self.__width)]
            if i != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """Return the string representation of the retangle"""
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)
