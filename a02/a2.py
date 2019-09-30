#!/usr.bin/python
# script for comp435 assignment 2
# hash a message with different algorithms

import hashlib

def main(msg):
    print(msg)
    # h = msg.encode()
    
    # SHA1
    m = hashlib.sha1(msg)
    print(m.hexdigest())

    # SHA256
    m = hashlib.sha256(msg)
    print(m.hexdigest())

    # MD5
    m = hashlib.md5(msg)
    print(m.hexdigest())

if __name__ == '__main__':
    main("ab122")