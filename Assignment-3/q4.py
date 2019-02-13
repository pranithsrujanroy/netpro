# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:36:47 2019

@author: Pranith Srujan Roy
"""

"""
Question: 
    Finding the service name, given the port and protocol of the remote host (server)?
"""

import socket

def find_service_name(port=80, protocol='udp'):
    try:
        print("Given port no is %d and protocol is %s" %(port, protocol))
        serv = socket.getservbyport(port, protocol)
        print("Service name: "+str(serv))
    except socket.error as e:
        print(str(e))
if __name__ == "__main__":
    find_service_name()