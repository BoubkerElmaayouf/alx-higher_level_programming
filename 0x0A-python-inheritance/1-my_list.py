#!/usr/bin/python3
"""Defining new classs"""


class MyList(list):
    """Starting a new class inherited from the super one"""

    def print_sorted(self):
        print(sorted(self))
