#!/usr/bin/python3
"""  function magic_string() that returns a string “BestSchool”
n times the number of the iteration """


def magic_string():
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["BestSchool"] * magic_string.count)
