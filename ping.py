#!/usr/bin/env python
from threading import Thread
import subprocess
from Queue import Queue
import sys
import re

def pinger(i, iq, mq):
    """Pings subnet"""
    while True:
        ip = iq.get()

        print "Thread %s: Pinging %s" % (i, ip)

        ret = subprocess.call("ping -c 1 %s" % ip,
               shell=True,
               stdout=open('/dev/null', 'w'),
               stderr=subprocess.STDOUT)

        if ret == 0:
            print "%s: is alive" % ip
            mq.put(ip)
        else:
            print "%s: did not respond" % ip

        iq.task_done()
    

def arping(i, oq):
    """grabs a valid IP address from a queue and gets macaddr"""
    while True:
        ip = oq.get()

        p = subprocess.Popen("arping -c 1 %s" % ip,
                shell=True,
                stdout=subprocess.PIPE)
        out = p.stdout.read()
        #match and extract mac address from stdout
        result = out.split()
        pattern = re.compile(":")
        macaddr = None
        for item in result:
            if re.search(pattern, item):
                macaddr = item
        print "IP Address: %s | Mac Address: %s " % (ip, macaddr)

        oq.task_done()

if __name__ == '__main__':
    num_threads = 10
    iq = Queue()
    mq = Queue()

    ips = []

    for i in range(20):
        ips.append('10.207.10.%d' % i)

    for i in range(num_threads):
        worker = Thread(target=pinger, args=(i, iq, mq))
        worker.setDaemon(True)
        worker.start()

    for i in range(num_threads):
        worker = Thread(target=arping, args=(i, mq))
        worker.setDaemon(True)
        worker.start()

    for ip in ips:
        iq.put(ip)

    print "Main Thread Waiting"
    iq.join()
    mq.join()
    print "Done"
    sys.exit(0)

