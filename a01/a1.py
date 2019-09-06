#!/usr.bin/python
# script for comp435 assignment 1
# parse file and print out number of instances of line

import sys

def main():
    # retreive filename from args
    file = sys.argv[1]

    # input hex and count dict
    inputs = dict()
    counts = dict()

    # open file and read
    with open(file) as f:
        for line in f:
            # clean input and find base 16 int
            x = line.strip()
            i = int(x, 16)
            if len(x) > 1: x = x.lstrip('0')

            # update count
            inputs[i] = x
            counts[i] = counts.get(i, 0) + 1

    # sort keys
    keys = sorted(counts.keys())

    # iterate over sorted keys
    for key in keys:
        count = counts[key]
        if count > 1: print inputs[key], count

if __name__ == '__main__':
    main()