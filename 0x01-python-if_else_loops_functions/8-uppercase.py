#!/usr/bin/python3

def uppercase(str):
    upper = 0
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upper = 38
        else:
            upper = 0
        print("{}".format(chr(ord(i) - upper)), end='')
    print("".format())
