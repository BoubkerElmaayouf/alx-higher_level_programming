#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_val = my_list[0]
        for index in my_list:
            if max_val < index:
                max_val = index
        return max_val
    else:
        return None
