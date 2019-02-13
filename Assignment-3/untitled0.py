# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 09:59:20 2019

Modifying sockets send/receive buffer size and changing the socket to blocking/non-blocking mode?
"""

import socket, sys


def client(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    bytecount = (bytecount + 15) // 16 * 16  # round up to a multiple of 16
    message = b'capitalize this!'  # 16-byte message to repeat over and over

    print('Sending', bytecount, 'bytes of data, in chunks of 16 bytes')
    sock.connect((host, port))
    sock.setblocking(False)
    sent = 0
    while sent < bytecount:
        sock.sendall(message)
        sent += len(message)
        print('\r  %d bytes sent' % (sent,))
        sys.stdout.flush()

    print()
    sock.shutdown(socket.SHUT_WR)

    print('Receiving all the data the server sends back')

    received = 0
    while True:
        data = sock.recv(42)
        if not received:
            print('  The first data received says', repr(data))
        if not data:
            break
        received += len(data)
        print('\r  %d bytes received' % (received,))

    print()
    sock.close()

if __name__ == '__main__':
    client('localhost', 12345, 1024)
    