#!/usr/bin/python3
for x in range(0, 9):
    for y in range(x + 1, 10):
        sep = ", "
        if x == 8:
            sep = "\n"
        print("{:d}{:d}".format(x, y), end=sep)
