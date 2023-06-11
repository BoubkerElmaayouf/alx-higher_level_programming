#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_a_1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    tup_a_2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    tup_b_1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    tup_b_2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    res = tup_a_1 + tup_b_1, tup_a_2 + tup_b_2
    return res
