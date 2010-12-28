#!/usr/bin/env python
############################################################################
# Server side: open a TCP/IP socket on a port, listen for a message from
# a client, and send an echo reply; this is a simple one-shot listen/reply
# conversation per client, but it goes into an infinite loop to listen for
# more clients
# a remote machine, or on same computer if it uses 'localhost' for server
############################################################################
from socket import *
myHost = ''
myPort = 50007
# get socket constructor and constants
# server machine, '' means local host
# listen on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

while True:
	connection, address = sockobj.accept( )
	print 'Server connected by', address
	while True:
		data = connection.recv(1024)
		if not data: break
		connection.send('Echo=>' + data)
	connection.close( )

