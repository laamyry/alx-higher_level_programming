#!/usr/bin/python3

def uppercase(str):
    for m in range(len(str)):
        if ord(str[m]) >= 97 and ord(str[m]) < 123:
            lttr = 32
        else:
            lttr = 0
        print("{:c}".format(ord(str[m]) - lttr), end='')
    print()
