#!/usr/bin/python
import subprocess
import re
import sys

def arping(ipaddress="10.0.1.1"):
    p = subprocess.Popen('/usr/bin/arping -c 2 %s' % ipaddress,
            shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read()
    result = out.split()
    print result    
    for item in result:
        if ':' in item:
            print item

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for ip in sys.argv[1:]:
            print 'arping', ip
            arping(ip)
    else:
        arping()
