# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 10:52:12 2019

@author: Student
"""

"""
Question:
    Write a simple UDP echo client/server application with the help of TCP
socket object. The server wait for the client to be connected and send
some data to the server. When the data is received, the server echoes the
data to the client.
"""

import socket
"""
def start_server():
    s = socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = 1234
    s.bind(('', port))
    print('udp echo server ready')
    while 1:
        data, addr = s.recvfrom(1024)
        print('server received %r from %r' % (data, addr))
        s.sendto(data, addr)

if __name__ == "__main__":
    start_server()
"""

ip = '127.0.0.1'
port = 6789
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip, port))
data, addr = s.recvfrom(1024)
print("Server received: %s" %data)
s.sendto(data, addr)