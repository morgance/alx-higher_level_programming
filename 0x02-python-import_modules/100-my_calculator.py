#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    nam = len(sys.argv) - 1
    if nam != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    sums = sys.argv[2]
    if sums != '+' and sums != '-' and sums != '*' and sums != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sums == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sums == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sums == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b )))
