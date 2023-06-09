#!/usr/bin/python3

if __name__ == '__main__':

    import sys

    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print(".", end="\n")
    else:
        print(str(num_args) + " argument:", end="\n")
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
