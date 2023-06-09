#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    m = len(sys.argv)
    total = 0
    for n in range(1, m):
        total += int(sys.argv[n])
    print(total)
