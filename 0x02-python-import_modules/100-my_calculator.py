#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    import calculator_1

    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = args[1]
    a = int(args[0])
    b = int(args[2])
    operations = {
        '+': calculator_1.add,
        '-': calculator_1.sub,
        '*': calculator_1.mul,
        '/': calculator_1.div
    }
    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    result = operations[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
