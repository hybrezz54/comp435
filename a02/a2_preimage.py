#!/usr.bin/python
# script for comp435 assignment 2
# find a collision for first n bytes of given image

import hashlib
import random
import string

def find_preimage(target, n):
    letters = string.ascii_letters + string.digits
    # counter = 0

    while True:
        # generate random string
        matched = ''.join(random.choice(letters) for i in range(16))
        matched = matched.encode('ascii')

        # generate hash
        hashed = hashlib.sha256(matched).digest()

        # check for first n bytes
        if hashed[:n] == target[:n]:
            break

        # counter += 1

    # print counter
    return matched

if __name__ == '__main__':
    msg = "The quick brown fox jumps over the lazy dog."
    hashed = hashlib.sha256(msg.encode('ascii'))
    print find_preimage(hashed.digest(), 2)