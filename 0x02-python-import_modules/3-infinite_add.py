#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_inf = 0
    num_args = len(sys.argv)
    for i in range(1, num_args):
        sum_inf += int(sys.argv[i])
    print("{:d}".format(sum_inf))
