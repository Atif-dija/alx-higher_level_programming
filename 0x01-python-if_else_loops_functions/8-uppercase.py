#!/usr/bin/python3
for c in str:
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")

