#!/usr.bin/python
# script for comp435 assignment 2
# convert hex strings to binary strings and compute hamming distance

import hashlib

def hammingdistance(hex1,hex2):
    # convert hex strs to binary
    binary1 = bin(int(hex1, 16))
    binary2 = bin(int(hex2, 16))

    # keep only bits
    binary1 = binary1[(binary1.index('b') + 1):]
    binary2 = binary2[(binary2.index('b') + 1):]

    # fill in with 0
    rht_len = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(rht_len)
    binary2 = binary2.zfill(rht_len)

    # find hamming distance
    assert len(binary1) == len(binary2)
    return sum(c1 != c2 for c1, c2 in zip(binary1, binary2))


if __name__ == '__main__':
    print hammingdistance("00ab122", "bb")