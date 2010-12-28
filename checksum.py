#!/usr/bin/env python
import hashlib
import sys

def create_checksum(path):
    """
    Reads in file. Creates checksum of file line by line.
    Returns complete checksum total for file.
    """
    fp = open(path)
    checksum = hashlib.md5()

    while True:
        buffer = fp.read(8192)
        if not buffer: break
        checksum.update(buffer)

    fp.close()
    checksum = checksum.digest()
    return checksum

if __name__ == '__main__':
    assert len(sys.argv) > 1, 'path is required'
    print create_checksum(sys.argv[1])
