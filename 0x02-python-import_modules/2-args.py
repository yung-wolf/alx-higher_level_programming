#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args_num = len(sys.argv) - 1

    # print the number of argv arguments
    if args_num == 1:
        print("{} argument:".format(args_num))
        for index in range(args_num):
            print("{}: {}".format(index + 1, sys.argv[index + 1]))
    elif args_num == 0:
        print("{} arguments.".format(args_num))
    else:
        print("{} arguments:".format(args_num))
        for index in range(args_num):
            print("{}: {}".format(index + 1, sys.argv[index + 1]))
