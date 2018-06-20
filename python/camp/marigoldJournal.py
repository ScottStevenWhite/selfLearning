#Python program to implement client side of chat room.
import socket
import select
import sys
import time
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#if len(sys.argv) != 3:
#    print "Correct usage: script, IP address, port number"
#    exit()
IP_address = "128.10.12.154"#str(sys.argv[1])
Port = 56423#int(sys.argv[2])
server.connect((IP_address, Port))

def delayprint(s):
    for c in message:
        sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(.1)
 
while True:
 
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]
 
    """ There are two possible input situations. Either the
    user wants to give  manual input to send to other people,
    or the server is sending a message  to be printed on the
    screen. Select returns from sockets_list, the stream that
    is reader for input. So for example, if the server wants
    to send a message, then the if condition will hold true
    below.If the user wants to send a message, the else
    condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
	    delayprint(message)
        else:
            message = sys.stdin.readline()
            server.send(message)
            #sys.stdout.write("<You>")
            #sys.stdout.write(message)
            sys.stdout.flush()
server.close()
