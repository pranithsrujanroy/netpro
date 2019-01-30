# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:30:46 2019

@author: Pranith Srujan Roy
"""

"""
Question:
    
Printing your machine’s name and IPv4 address? 
"""

import socket

def print_machine_info():
    """
    socket.gethostname returns a string containing the hostname of the machine
    where the Python interpreter is currently executing.
    socket.getfqdn returns a fully qualified domain name if it's available
    or gethostname otherwise. 
    """
    name = socket.getfqdn()
    ip = socket.gethostbyname(name)
    print("Host name: "+name+" and IPv4 address: "+ip)

if __name__== "__main__":
    print_machine_info()
