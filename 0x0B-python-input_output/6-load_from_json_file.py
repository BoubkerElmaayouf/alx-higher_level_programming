#!/usr/bin/python3
""" Defining A Function """

import json


def load_from_json_file(filename):
    """
    this function that creates
    an Object from a “JSON file”
    """
    with open(filename) as f:
        return json.load(f)
