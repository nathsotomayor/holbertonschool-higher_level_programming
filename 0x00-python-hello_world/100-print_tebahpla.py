#!/usr/bin/python3
for idx in range(122, 96, -1):
    if idx % 2 == 1:
        char = idx - 32
    else:
        char = idx
    print("{:c}".format(char), end="")
