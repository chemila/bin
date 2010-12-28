#!/usr/bin/env python
from checksum import create_checksum
from diskwalk import diskwalk
from os.path import getsize
import sys

def findDupes(path = '/tmp'):
    dup = []
    record = {}
    d = diskwalk(path)
    files = d.enumeratePaths()
    for file in files:
        compound_key = (getsize(file),create_checksum(file))
        if compound_key in record:
            dup.append(file)
        else:
            record[compound_key] = file
    return dup

if __name__ == "__main__":
    assert len(sys.argv) > 1, 'path is required'
    dupes = findDupes(sys.argv[1])
    for dup in dupes:
        print dup + '\r'
