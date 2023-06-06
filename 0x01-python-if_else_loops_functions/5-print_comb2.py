#!/usr/bin/python3
for nmbr in range(0, 100):
    if nmbr == 99:
        print("{}".format(nmbr))
    else:
        print("{:02}".format(nmbr), end=", ")
