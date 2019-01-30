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
    except socket.error, e:
        print "Error creating socket: %s" % e
        sys.exit(1)
    print("Default socket timeout: "+str(s.gettimeout()))
    s.settimeout(5)
    print("Current socket timeout: "+str(s.gettimeout()))
    try:
        while(True):
            c,addr = s.accept()
    except socket.timeout, e:
        print "Socket error: "+str(e)

if __name__ == "__main__":
    test_socket_timeout()