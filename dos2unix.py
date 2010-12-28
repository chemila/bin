#!/usr/bin/python
import os, sys
def convert(fname):
    newLines = []
    changed = False

    for line in open(fname, 'rb').readlines():
        if line[-2:] == '\r\n':
            newLines.append(line[:-2] + '\n')
            changed = True

    if changed:
        print 'Converted %s' % fname

    try:
        open(fname, 'wb').writelines(newLines)
    except IOError:
        print 'Write %s denied' % fname

if __name__ == '__main__':
    errorMsg = 'Invalid arguments'
    assert len(sys.argv) == 2, errorMsg

    convert(sys.argv[1])
