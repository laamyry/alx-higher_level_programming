#!/usr/bin/python3
"""reads stdin ln by ln and computes metrics:"""


def print_code_stats(size, codes_status):
    """def print_code_stats"""
    print("File size: {}".format(size))
    for sarot in sorted(codes_status):
        print("{}: {}".format(sarot, codes_status[sarot]))


if __name__ == "__main__":
    import sys

    size = 0
    codes_status = {}
    codes_val = ['200', '301', '400', '401', '403', '404', '405', '500']
    counter = 0

    try:
        for ln in sys.stdin:
            if counter == 10:
                print_code_stats(size, codes_status)
                counter = 1
            else:
                counter += 1

            ln = ln.split()

            try:
                size += int(ln[-1])
            except (IndexError, ValueError):
                pass

            try:
                if ln[-2] in codes_val:
                    if codes_status.get(ln[-2], -1) == -1:
                        codes_status[ln[-2]] = 1
                    else:
                        codes_status[ln[-2]] += 1
            except IndexError:
                pass

        print_code_stats(size, codes_status)

    except KeyboardInterrupt:
        print_code_stats(size, codes_status)
        raise
