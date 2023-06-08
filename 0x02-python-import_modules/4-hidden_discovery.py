#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hid
    for x in range(len(dir(hid))):
        if (dir(hid)[x][:2] == "__"):
            continue
        print(dir(hid)[x])
