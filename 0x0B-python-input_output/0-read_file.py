#!/usr/bin/python3
"""Defining a function"""


def read_file(filename=""):
    """this function reads from file and print to
    stdout"""

    with open(filename, mode="r", encoding="utf-8") as f:
        rf = f.read()
        print("{}".format(rf), end="")
