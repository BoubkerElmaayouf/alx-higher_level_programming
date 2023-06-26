#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        pass
    finally:
        print("")
        return (i + 1) if i < x - 1 else x
