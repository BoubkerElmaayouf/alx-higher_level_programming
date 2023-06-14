#!/usr/bin/python3
def uniq_add(my_list=[]):
    nums_sum = 0
    for x in set(my_list):
        nums_sum += x
    return nums_sum
