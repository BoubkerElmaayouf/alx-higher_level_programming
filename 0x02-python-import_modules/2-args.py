#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv)
    if arg_len == 1:
        print("0 arguments.")
    elif arg_len > 1:
        print("{:d} argument{:s}".format(
            arg_len - 1,
            "s:" if arg_len > 2 else ":"
            ))
    for i in range(1, arg_len):
        print("{:d}: {:s}".format(i, argv[i]))
