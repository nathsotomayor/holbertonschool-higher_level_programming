#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 1:
        print("{:d} argument: ".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments: ".format(len(sys.argv) - 1))
    num_args = len(sys.argv)
    for i in range(1, num_args):
        print("{:d}: {}".format(i, str(sys.argv[i])))
