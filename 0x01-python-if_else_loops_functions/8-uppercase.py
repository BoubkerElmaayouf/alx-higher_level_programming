#!/usr/bin/python3
def uppercase(str):
    res = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            res += chr(ord(c) - 32)
        else:
            res += c
    print("{}".format(res))
