#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv

    # start count from 1
    args_num = len(argv)
    sum = 0
    i = 1

    # when no args are entered
    if args_num == 0:
        print(0)
    else:
        while i != args_num:
            sum += int(argv[i])
            i += 1
        print("{}".format(sum))
