# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:42:22 2019

@author: Pranith Srujan Roy
"""
"""
Question:
    Setting  and  getting  the  default socket  timeout,  
    the  program  should include how to handle the socket error gracefully?
"""

import socket
import sys
def test_socket_timeout():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Error creating socket: %s" % msg)
        sys.exit(1)
    print("Default socket timeout: "+str(s.gettimeout()))
    s.settimeout(5)
    print("Current socket timeout: "+str(s.gettimeout()))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = 12345
    host = socket.gethostname()
    s.bind((host, port))
    s.listen(1)
    try:
        while(True):
            print("Waiting for connection from client..")
            c,addr = s.accept()
    except socket.timeout as msg:
        print("Socket error: %s" % msg)

if __name__ == "__main__":
    test_socket_timeout()