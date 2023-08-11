#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    
    # Get number of args to program
    num_args = len(sys.argv) - 1

    # If args is not equal to expected
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # Assign var <a> & <b> w/ nums and cast to ints
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sys.argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sys.argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif sys.argv[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
