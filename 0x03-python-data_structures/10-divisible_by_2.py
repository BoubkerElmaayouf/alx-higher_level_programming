#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    if my_list:
        for index in my_list:
            if index % 2 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
    return my_list
