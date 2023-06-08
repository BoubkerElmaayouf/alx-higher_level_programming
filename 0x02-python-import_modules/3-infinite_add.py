#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv)
    if arg_len == 1:
        print(0)
    elif arg_len > 1:
        res = 0
        for x in range(1, arg_len):
            res = res + int(argv[x])
        print("{:d}".format(res))
