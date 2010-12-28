#!/usr/bin/env python
############################################################################
# Client side: use sockets to send data to the server, and print server's
# reply to each message line; 'localhost' means that the server is running
# on the same machine as the client, which lets us test client and server
# on one machine; to test over the Internet, run a server on a remote
# machine, and set serverHost or argv[1] to machine's domain name or IP addr;
# Python sockets are a portable BSD socket interface, with object methods
# for the standard socket calls available in the sytstem's C library;
############################################################################
import sys
from socket import *
serverHost = 'localhost'
serverPort = 50007
# portable socket interface plus constants
# server name, or: 'starship.python.net'
# non-reserved port used by the server
message = ['Hello network world']
if len(sys.argv) > 1:
	serverHost = sys.argv[1]
	if len(sys.argv) > 2:
		message = sys.argv[2:]

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))
	
for line in message:
	sockobj.send(line)
	data = sockobj.recv(1024)
	print 'Client received:', repr(data)
sockobj.close( )

