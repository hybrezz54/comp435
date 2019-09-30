#!/usr.bin/python
# script for comp435 assignment 2
# find a collision for first n bytes of two generated images

import hashlib
import random
import string

def find_collision(n):
    # dict for str-hash pair
    hashed_msgs = {}
    # counter = 0

    # generate random strings
    letters = string.ascii_letters + string.digits
    m = ''.join(random.choice(letters) for i in range(16)).encode('ascii')

    # generate hash and update
    h = hashlib.sha256(m).digest()
    hashed_msgs[h[:n]] = m

    while True:
        # keep generating strings until collision
        letters = string.ascii_letters + string.digits
        m = ''.join(random.choice(letters) for i in range(16)).encode('ascii')
        h = hashlib.sha256(m).digest()

        # check for collision
        if h[:n] in hashed_msgs:
            break

        # update otherwise
        hashed_msgs[h[:n]] = m
        # counter += 1

    # print counter
    return m, hashed_msgs[h[:n]]

if __name__ == '__main__':
    print find_collision(2)