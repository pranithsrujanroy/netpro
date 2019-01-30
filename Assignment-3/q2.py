# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:36:11 2019

@author: Pranith Srujan Roy
"""
"""
Question:
    Retrieve a remote machine’s IP address and  convert the  IP address to different format?
"""

import socket
from binascii import hexlify

def get_remote_machine_ip(remote_host):
    try:
        ip = socket.gethostbyname(remote_host)
        return ip
    except socket.error, err_msg:
        print("%s: %s", (remote_host, err_msg))
        
def convert_ipv4(ipv4):
    packed_ip = socket.inet_aton(ipv4)
    unpacked_ip = socket.inet_ntoa(packed_ip)
    """
    hexlify function of the binascii module helps to represent the binary data in a
    hexadecimal format.
    """
    print "IP Address: %s => Packed: %s, Unpacked: %s"\
    %(ipv4, hexlify(packed_ip), unpacked_ip)

if __name__ == "__main__":
    remote_host = "www.google.com"
    remote_host_ip = get_remote_machine_ip(remote_host);
    print("IP address of www.google.com is: "+str(remote_host_ip))
    convert_ipv4(remote_host_ip)