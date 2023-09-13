#!/usr/bin/python3
""" Defining a function """


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
    and returns the number
    of characters written """

    with open(filename, mode="w", encoding="utf-8") as f:
        counter = f.write(text)
        return (counter)
