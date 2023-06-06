#!/usr/bin/python3
for letters in range(ord('a'), ord('z') + 1):
    if chr(letters) not in ['e', 'q']:
        print("{}".format(chr(letters)), end='')
