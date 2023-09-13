#!/usr/bin/python3
""" Defining a function """


def append_write(filename="", text=""):
    """
     function that appends a string at the
     end of a text file (UTF8) and
     returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        wf = f.write(text)
        return (wf)
