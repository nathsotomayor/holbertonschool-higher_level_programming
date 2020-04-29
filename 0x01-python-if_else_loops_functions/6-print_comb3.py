#!/usr/bin/python3
for numbers1 in range(0, 10):
    for numbers2 in range(numbers1 + 1, 10):
        print("{:d}{:d}".format(numbers1, numbers2),
              end="\n" if numbers1 == 8 and numbers1 + 1 == 9 else ", ")
