#!/usr/bin/python3

for i in range(0, 10):
    for j in range(0, 10):
        if (i != j and i < j):
            print("{}{}".format(i, j), end='')
            if (i + j != 17):
                print(", ".format(), end='')
        j += j
    i += i
print("".format())
