#!/usr/bin/python3
"""returns a key with the biggest integer value."""


def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    res = float('-inf')
    best_key = None

    for key, value in a_dictionary.items():
        if not isinstance(value, int):
            return None
        if value > res:
            res = value
            best_key = key

    return best_key
