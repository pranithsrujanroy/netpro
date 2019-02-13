# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 09:58:59 2019

@author: Student
Modifying sockets send/receive buffer size and changing the socket to blocking/non-blocking mode?

"""

import argparse, socket, sys

def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1024)
    sock.bind((host, port))
    sock.listen(1)
    print('Listening at', sock.getsockname())
    while True:
        sc, sockname = sock.accept()
        print('Processing up to 1024 bytes at a time from', sockname)
        n = 0
        while True:
            data = sc.recv(1024)
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            sc.sendall(output)  # send it back uppercase
            n += len(data)
            print('\r  %d bytes processed so far' % (n,))
            sys.stdout.flush()
        print()
        sc.close()
        print('  Socket closed')
        return 0

if __name__ == '__main__':
    
    server('localhost', 12345)