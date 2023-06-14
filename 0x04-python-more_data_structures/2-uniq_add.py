#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        unique_nums = {x for x in my_list}
        nums_sum = sum(unique_nums)
    return nums_sum
