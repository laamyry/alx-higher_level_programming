#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    argc = len(sys.argv)
    if argc < 2:
        print(f"{argc - 1} arguments.")
    else:
        if argc == 2:
            print(f"{argc - 1} argument:")
        else:
            print(f"{argc - 1} arguments:")
        for m, argument in enumerate(sys.argv[1:], 1):
            print(f"{m}: {argument}")
