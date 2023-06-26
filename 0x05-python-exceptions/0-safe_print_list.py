#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        pass
    print("")
    if i < x - 1:
        return (i + 1)
    else:
        return (x)
