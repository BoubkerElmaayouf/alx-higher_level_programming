#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_container = []
    for i in range(list_length):
        try:
            div_res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_res = 0
        except ZeroDivisionError:
            print("division by 0")
            div_res = 0
        except IndexError:
            print("out of range")
            div_res = 0
        finally:
            res_container.append(div_res)
    return res_container
