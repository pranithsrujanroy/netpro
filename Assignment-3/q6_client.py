# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:47:06 2019

@author: ammum
"""

import socket
SEND_BUFF_SIZE = 4098
RECV_BUFF_SIZE = 2048
def start_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    sock.connect((host, 1235))
    sock.setblocking(0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUFF_SIZE)
    data = b'foobar\n'*1024*1024
    print('Sending data')
    assert sock.send(data)==len(data)
    print("Data sent")
    
if __name__ == "__main__":
    start_client()