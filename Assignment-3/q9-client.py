# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 10:52:31 2019

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

def start_client():
    ip = '127.0.0.1'
    port = 6789
    message = b'hello server...echo me this message!'
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 0))
    s.sendto(message, (ip, port))
    data, addr = s.recvfrom(1024)
    print("Client received: %s" %data)

if __name__ == "__main__":
    start_client()

