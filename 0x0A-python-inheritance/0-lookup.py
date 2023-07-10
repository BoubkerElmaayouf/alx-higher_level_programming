#!/usr/bin/python3
"""Definding an aboj attribute lookup function"""


def lookup(obj):
    """
     this function returns the list of
     available attributes and
     methods of an object:
     """
    return dir(obj)
